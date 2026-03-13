-- Exercise 3: Performance Tuning
-- Use the banking tables created in the session README setup script.

-- 3a. Run EXPLAIN QUERY PLAN on the following query and describe what you see:
EXPLAIN QUERY PLAN
SELECT a.customer_name, t.transaction_date, t.amount
FROM accounts a
JOIN transactions t ON a.account_id = t.account_id
WHERE t.transaction_date >= '2024-02-01'
ORDER BY t.amount DESC;

-- Write your observations here as a comment:
--


-- 3b. Create an index that would improve the query above.
-- Then run EXPLAIN QUERY PLAN again and note the difference.



-- 3c. The following query is inefficient. Rewrite it to be faster
-- while producing the same results:
--
-- SELECT * FROM transactions
-- WHERE account_id IN (
--     SELECT account_id FROM transactions
--     WHERE amount > 1000
--     GROUP BY account_id
-- )
-- ORDER BY transaction_date;
--
-- Your improved version:



-- 3d. Create a composite index that would help queries filtering
-- by account_id AND transaction_type together. Explain why a composite
-- index is better than two separate indexes for this pattern.



-- 3e. CHALLENGE: Write the most efficient query you can to answer:
-- "For each branch, what is the average transaction amount and
-- how many unique customers made transactions in January 2024?"
-- Include appropriate indexes.

