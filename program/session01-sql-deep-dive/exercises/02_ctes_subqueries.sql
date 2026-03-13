-- Exercise 2: CTEs and Subqueries
-- Use the banking tables created in the session README setup script.

-- 2a. Write a CTE that calculates total deposits and total withdrawals per account,
-- then SELECT only accounts where withdrawals exceed 20% of deposits.
-- Expected columns: customer_name, total_deposits, total_withdrawals, withdrawal_pct



-- 2b. Chain two CTEs:
--   CTE 1: monthly_totals — total amount per account per month
--   CTE 2: month_over_month — use LAG to compare each month's total to the previous
-- Final SELECT: show accounts with a month-over-month decrease.



-- 2c. Use a subquery to find all transactions from accounts that were opened
-- in the Downtown branch. Do NOT use a JOIN.



-- 2d. Use EXISTS to find accounts that have at least one transaction
-- in the 'Dining' category.



-- 2e. CHALLENGE: Write a single query using CTEs that produces a "customer report"
-- showing: customer_name, account_type, total_transactions, total_deposits,
-- total_withdrawals, net_balance, and their rank by net_balance.

