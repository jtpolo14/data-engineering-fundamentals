-- Solution 3: Performance Tuning

-- 3a. EXPLAIN QUERY PLAN analysis
EXPLAIN QUERY PLAN
SELECT a.customer_name, t.transaction_date, t.amount
FROM accounts a
JOIN transactions t ON a.account_id = t.account_id
WHERE t.transaction_date >= '2024-02-01'
ORDER BY t.amount DESC;

-- Observations:
-- Without indexes, SQLite performs a SCAN on both tables (full table scan).
-- It scans all rows in transactions, then looks up each matching account.
-- The ORDER BY requires a temporary B-tree for sorting.
-- This is fine for 20 rows but would be slow with millions.


-- 3b. Index to improve the query
CREATE INDEX idx_transactions_date ON transactions(transaction_date);

-- Now EXPLAIN QUERY PLAN will show:
-- SEARCH transactions USING INDEX idx_transactions_date
-- instead of SCAN TABLE transactions
-- The database can jump directly to rows >= '2024-02-01'.


-- 3c. Rewritten efficient query
-- Original uses a subquery that scans transactions twice.
-- Rewrite with a JOIN to a CTE:
WITH high_value_accounts AS (
    SELECT DISTINCT account_id
    FROM transactions
    WHERE amount > 1000
)
SELECT t.*
FROM transactions t
JOIN high_value_accounts hva ON t.account_id = hva.account_id
ORDER BY t.transaction_date;

-- This scans transactions once for the CTE, then uses
-- the small result set for the JOIN.


-- 3d. Composite index
CREATE INDEX idx_transactions_account_type
ON transactions(account_id, transaction_type);

-- Why composite is better than two separate indexes:
-- A composite index (account_id, transaction_type) stores data sorted
-- by account_id first, then by transaction_type within each account_id.
-- For a query like WHERE account_id = 1 AND transaction_type = 'Deposit',
-- the database can find the exact rows in a single index lookup.
--
-- With two separate indexes, the database would either:
-- 1. Use one index and scan the results for the other condition, OR
-- 2. Use both indexes separately and intersect the results
-- Both approaches are slower than the single composite index.


-- 3e. CHALLENGE: Branch transaction summary for January 2024

-- First, create helpful indexes
CREATE INDEX idx_transactions_date_account
ON transactions(transaction_date, account_id);

-- The query
SELECT
    a.branch,
    ROUND(AVG(t.amount), 2) as avg_transaction_amount,
    COUNT(DISTINCT a.account_id) as unique_customers
FROM accounts a
JOIN transactions t ON a.account_id = t.account_id
WHERE t.transaction_date >= '2024-01-01'
  AND t.transaction_date < '2024-02-01'
GROUP BY a.branch
ORDER BY avg_transaction_amount DESC;
