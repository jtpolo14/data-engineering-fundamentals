-- Exercise 1: Window Functions
-- Use the banking tables created in the session README setup script.

-- 1a. Use ROW_NUMBER to assign a sequential number to each transaction
-- per account, ordered by transaction_date.
-- Expected columns: customer_name, transaction_date, amount, transaction_number



-- 1b. Use RANK to rank all accounts by their total withdrawal amount (highest first).
-- Expected columns: customer_name, total_withdrawals, withdrawal_rank



-- 1c. Use LAG to show each transaction alongside the previous transaction's amount
-- for the same account. Calculate the difference.
-- Expected columns: customer_name, transaction_date, amount, previous_amount, amount_change



-- 1d. Calculate a running balance for each account ordered by transaction_date.
-- Expected columns: customer_name, transaction_date, amount, running_balance



-- 1e. CHALLENGE: Find the transaction with the largest single-day spending
-- per account using window functions (not GROUP BY).
-- Hint: Use ROW_NUMBER with a specific ORDER BY, then filter for row 1.

