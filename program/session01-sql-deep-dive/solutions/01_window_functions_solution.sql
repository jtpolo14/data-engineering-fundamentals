-- Solution 1: Window Functions

-- 1a. ROW_NUMBER per account
SELECT
    a.customer_name,
    t.transaction_date,
    t.amount,
    ROW_NUMBER() OVER (
        PARTITION BY t.account_id
        ORDER BY t.transaction_date
    ) as transaction_number
FROM transactions t
JOIN accounts a ON t.account_id = a.account_id
ORDER BY a.customer_name, t.transaction_date;


-- 1b. RANK by total withdrawals
WITH account_withdrawals AS (
    SELECT
        a.customer_name,
        SUM(ABS(t.amount)) as total_withdrawals
    FROM accounts a
    JOIN transactions t ON a.account_id = t.account_id
    WHERE t.transaction_type = 'Withdrawal'
    GROUP BY a.customer_name
)
SELECT
    customer_name,
    total_withdrawals,
    RANK() OVER (ORDER BY total_withdrawals DESC) as withdrawal_rank
FROM account_withdrawals;


-- 1c. LAG for previous transaction comparison
SELECT
    a.customer_name,
    t.transaction_date,
    t.amount,
    LAG(t.amount) OVER (
        PARTITION BY t.account_id
        ORDER BY t.transaction_date
    ) as previous_amount,
    t.amount - LAG(t.amount) OVER (
        PARTITION BY t.account_id
        ORDER BY t.transaction_date
    ) as amount_change
FROM transactions t
JOIN accounts a ON t.account_id = a.account_id
ORDER BY a.customer_name, t.transaction_date;


-- 1d. Running balance
SELECT
    a.customer_name,
    t.transaction_date,
    t.amount,
    SUM(t.amount) OVER (
        PARTITION BY t.account_id
        ORDER BY t.transaction_date
        ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW
    ) as running_balance
FROM transactions t
JOIN accounts a ON t.account_id = a.account_id
ORDER BY a.customer_name, t.transaction_date;


-- 1e. CHALLENGE: Largest single-day spending per account
WITH ranked_spending AS (
    SELECT
        a.customer_name,
        t.transaction_date,
        t.amount,
        ROW_NUMBER() OVER (
            PARTITION BY t.account_id
            ORDER BY t.amount ASC  -- most negative = largest spending
        ) as spend_rank
    FROM transactions t
    JOIN accounts a ON t.account_id = a.account_id
    WHERE t.transaction_type = 'Withdrawal'
)
SELECT customer_name, transaction_date, amount
FROM ranked_spending
WHERE spend_rank = 1
ORDER BY amount ASC;
