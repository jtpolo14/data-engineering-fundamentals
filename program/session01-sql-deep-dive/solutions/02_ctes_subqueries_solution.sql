-- Solution 2: CTEs and Subqueries

-- 2a. Accounts where withdrawals exceed 20% of deposits
WITH account_flows AS (
    SELECT
        a.customer_name,
        SUM(CASE WHEN t.transaction_type = 'Deposit' THEN t.amount ELSE 0 END) as total_deposits,
        SUM(CASE WHEN t.transaction_type = 'Withdrawal' THEN ABS(t.amount) ELSE 0 END) as total_withdrawals
    FROM accounts a
    JOIN transactions t ON a.account_id = t.account_id
    GROUP BY a.customer_name
)
SELECT
    customer_name,
    total_deposits,
    total_withdrawals,
    ROUND(total_withdrawals * 100.0 / total_deposits, 1) as withdrawal_pct
FROM account_flows
WHERE total_withdrawals > total_deposits * 0.2
ORDER BY withdrawal_pct DESC;


-- 2b. Month-over-month changes using chained CTEs
WITH monthly_totals AS (
    SELECT
        t.account_id,
        a.customer_name,
        strftime('%Y-%m', t.transaction_date) as month,
        SUM(t.amount) as monthly_total
    FROM transactions t
    JOIN accounts a ON t.account_id = a.account_id
    GROUP BY t.account_id, a.customer_name, strftime('%Y-%m', t.transaction_date)
),
month_over_month AS (
    SELECT
        customer_name,
        month,
        monthly_total,
        LAG(monthly_total) OVER (
            PARTITION BY account_id
            ORDER BY month
        ) as previous_month_total,
        monthly_total - LAG(monthly_total) OVER (
            PARTITION BY account_id
            ORDER BY month
        ) as month_change
    FROM monthly_totals
)
SELECT customer_name, month, monthly_total, previous_month_total, month_change
FROM month_over_month
WHERE month_change < 0
ORDER BY month_change ASC;


-- 2c. Subquery: transactions from Downtown accounts (no JOIN)
SELECT *
FROM transactions
WHERE account_id IN (
    SELECT account_id
    FROM accounts
    WHERE branch = 'Downtown'
)
ORDER BY transaction_date;


-- 2d. EXISTS: accounts with Dining transactions
SELECT a.customer_name, a.account_type
FROM accounts a
WHERE EXISTS (
    SELECT 1
    FROM transactions t
    WHERE t.account_id = a.account_id
    AND t.category = 'Dining'
);


-- 2e. CHALLENGE: Full customer report
WITH transaction_summary AS (
    SELECT
        t.account_id,
        COUNT(*) as total_transactions,
        SUM(CASE WHEN t.transaction_type = 'Deposit' THEN t.amount ELSE 0 END) as total_deposits,
        SUM(CASE WHEN t.transaction_type = 'Withdrawal' THEN ABS(t.amount) ELSE 0 END) as total_withdrawals
    FROM transactions t
    GROUP BY t.account_id
),
customer_report AS (
    SELECT
        a.customer_name,
        a.account_type,
        ts.total_transactions,
        ts.total_deposits,
        ts.total_withdrawals,
        ts.total_deposits - ts.total_withdrawals as net_balance
    FROM accounts a
    JOIN transaction_summary ts ON a.account_id = ts.account_id
)
SELECT
    customer_name,
    account_type,
    total_transactions,
    total_deposits,
    total_withdrawals,
    net_balance,
    RANK() OVER (ORDER BY net_balance DESC) as balance_rank
FROM customer_report
ORDER BY balance_rank;
