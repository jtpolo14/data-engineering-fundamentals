# Session 01: SQL for Data Engineers — Beyond SELECT *

Welcome to the first session of **Data Engineering Fundamentals**! You already know basic SQL — now it's time to write the kind of SQL that data engineers use every day.

**This session is FREE.**

---

## Learning Objectives

By the end of this session, you will be able to:

- Write Common Table Expressions (CTEs) to break complex queries into readable steps
- Use window functions (ROW_NUMBER, RANK, LAG, LEAD) for advanced analytics
- Understand when to use subqueries vs JOINs
- Read EXPLAIN plans to identify slow queries
- Apply aggregate patterns beyond basic COUNT and SUM

---

## Why This Matters for Data Engineers

As an analyst, you write SQL to answer questions. As a data engineer, you write SQL to:

- **Build transformations** that run nightly to populate dashboards
- **Optimize queries** that process millions of rows efficiently
- **Create data models** that analysts downstream depend on

The difference isn't just what you write — it's how efficiently and reliably it runs at scale.

---

## Setup

For this session, you'll need:

1. [DB Browser for SQLite](https://sqlitebrowser.org/) — free, no installation hassle
2. The exercise `.sql` files in the `exercises/` folder

Open DB Browser, create a new database, and run the setup script below to create sample data:

```sql
-- Create sample banking tables
CREATE TABLE accounts (
    account_id INTEGER PRIMARY KEY,
    customer_name TEXT NOT NULL,
    account_type TEXT NOT NULL,
    opened_date DATE NOT NULL,
    branch TEXT NOT NULL
);

CREATE TABLE transactions (
    transaction_id INTEGER PRIMARY KEY,
    account_id INTEGER,
    transaction_date DATE NOT NULL,
    amount DECIMAL(10,2) NOT NULL,
    transaction_type TEXT NOT NULL,
    category TEXT,
    description TEXT,
    FOREIGN KEY (account_id) REFERENCES accounts(account_id)
);

-- Insert sample accounts
INSERT INTO accounts VALUES (1, 'Jane Smith', 'Checking', '2023-01-15', 'Downtown');
INSERT INTO accounts VALUES (2, 'John Doe', 'Savings', '2023-02-20', 'Midtown');
INSERT INTO accounts VALUES (3, 'Alice Johnson', 'Checking', '2022-11-01', 'Downtown');
INSERT INTO accounts VALUES (4, 'Bob Williams', 'Savings', '2023-06-10', 'Uptown');
INSERT INTO accounts VALUES (5, 'Carol Davis', 'Checking', '2023-03-05', 'Midtown');

-- Insert sample transactions
INSERT INTO transactions VALUES (1, 1, '2024-01-05', 1500.00, 'Deposit', 'Payroll', 'Monthly salary');
INSERT INTO transactions VALUES (2, 1, '2024-01-08', -45.99, 'Withdrawal', 'Utilities', 'Electric bill');
INSERT INTO transactions VALUES (3, 1, '2024-01-12', -120.00, 'Withdrawal', 'Shopping', 'Online purchase');
INSERT INTO transactions VALUES (4, 2, '2024-01-03', 2000.00, 'Deposit', 'Transfer', 'Savings deposit');
INSERT INTO transactions VALUES (5, 2, '2024-01-15', -500.00, 'Withdrawal', 'Transfer', 'Transfer to checking');
INSERT INTO transactions VALUES (6, 3, '2024-01-02', 3200.00, 'Deposit', 'Payroll', 'Monthly salary');
INSERT INTO transactions VALUES (7, 3, '2024-01-10', -89.50, 'Withdrawal', 'Utilities', 'Internet bill');
INSERT INTO transactions VALUES (8, 3, '2024-01-18', -250.00, 'Withdrawal', 'Shopping', 'Groceries');
INSERT INTO transactions VALUES (9, 3, '2024-01-22', -75.00, 'Withdrawal', 'Dining', 'Restaurant');
INSERT INTO transactions VALUES (10, 4, '2024-01-07', 1000.00, 'Deposit', 'Transfer', 'Monthly savings');
INSERT INTO transactions VALUES (11, 4, '2024-01-20', 500.00, 'Deposit', 'Transfer', 'Bonus deposit');
INSERT INTO transactions VALUES (12, 5, '2024-01-04', 2800.00, 'Deposit', 'Payroll', 'Monthly salary');
INSERT INTO transactions VALUES (13, 5, '2024-01-09', -150.00, 'Withdrawal', 'Utilities', 'Water bill');
INSERT INTO transactions VALUES (14, 5, '2024-01-14', -320.00, 'Withdrawal', 'Shopping', 'Electronics');
INSERT INTO transactions VALUES (15, 5, '2024-01-25', -60.00, 'Withdrawal', 'Dining', 'Coffee shop');
INSERT INTO transactions VALUES (16, 1, '2024-02-05', 1500.00, 'Deposit', 'Payroll', 'Monthly salary');
INSERT INTO transactions VALUES (17, 2, '2024-02-03', 2000.00, 'Deposit', 'Transfer', 'Savings deposit');
INSERT INTO transactions VALUES (18, 3, '2024-02-02', 3200.00, 'Deposit', 'Payroll', 'Monthly salary');
INSERT INTO transactions VALUES (19, 3, '2024-02-15', -400.00, 'Withdrawal', 'Shopping', 'Clothing');
INSERT INTO transactions VALUES (20, 5, '2024-02-04', 2800.00, 'Deposit', 'Payroll', 'Monthly salary');
```

---

## Topic 1: Common Table Expressions (CTEs)

A CTE is a temporary named result set that you can reference within a query. Think of it as creating a "mini table" that only exists for that one query.

### Why CTEs Matter

Without CTEs, complex queries become deeply nested and hard to read. CTEs let you break logic into named, sequential steps.

### Basic CTE Syntax

```sql
WITH cte_name AS (
    SELECT ...
    FROM ...
    WHERE ...
)
SELECT *
FROM cte_name;
```

### Example: Monthly Spending Summary

```sql
-- Without CTE (messy nested subquery)
SELECT customer_name, total_spent
FROM (
    SELECT a.customer_name, SUM(ABS(t.amount)) as total_spent
    FROM accounts a
    JOIN transactions t ON a.account_id = t.account_id
    WHERE t.transaction_type = 'Withdrawal'
    GROUP BY a.customer_name
) sub
WHERE total_spent > 200;

-- With CTE (clean and readable)
WITH spending AS (
    SELECT
        a.customer_name,
        SUM(ABS(t.amount)) as total_spent
    FROM accounts a
    JOIN transactions t ON a.account_id = t.account_id
    WHERE t.transaction_type = 'Withdrawal'
    GROUP BY a.customer_name
)
SELECT customer_name, total_spent
FROM spending
WHERE total_spent > 200
ORDER BY total_spent DESC;
```

### Chaining Multiple CTEs

You can chain CTEs to build complex logic step by step:

```sql
WITH deposits AS (
    SELECT account_id, SUM(amount) as total_deposits
    FROM transactions
    WHERE transaction_type = 'Deposit'
    GROUP BY account_id
),
withdrawals AS (
    SELECT account_id, SUM(ABS(amount)) as total_withdrawals
    FROM transactions
    WHERE transaction_type = 'Withdrawal'
    GROUP BY account_id
)
SELECT
    a.customer_name,
    COALESCE(d.total_deposits, 0) as deposits,
    COALESCE(w.total_withdrawals, 0) as withdrawals,
    COALESCE(d.total_deposits, 0) - COALESCE(w.total_withdrawals, 0) as net_flow
FROM accounts a
LEFT JOIN deposits d ON a.account_id = d.account_id
LEFT JOIN withdrawals w ON a.account_id = w.account_id
ORDER BY net_flow DESC;
```

---

## Topic 2: Window Functions

Window functions perform calculations across a set of rows related to the current row — without collapsing rows like GROUP BY does.

### ROW_NUMBER — Assign Sequential Numbers

```sql
-- Number each transaction per account by date
SELECT
    t.transaction_id,
    a.customer_name,
    t.transaction_date,
    t.amount,
    ROW_NUMBER() OVER (
        PARTITION BY t.account_id
        ORDER BY t.transaction_date
    ) as transaction_number
FROM transactions t
JOIN accounts a ON t.account_id = a.account_id;
```

### RANK and DENSE_RANK — Rank with Ties

```sql
-- Rank customers by total deposits
WITH customer_deposits AS (
    SELECT
        a.customer_name,
        SUM(t.amount) as total_deposits
    FROM accounts a
    JOIN transactions t ON a.account_id = t.account_id
    WHERE t.transaction_type = 'Deposit'
    GROUP BY a.customer_name
)
SELECT
    customer_name,
    total_deposits,
    RANK() OVER (ORDER BY total_deposits DESC) as deposit_rank
FROM customer_deposits;
```

### LAG and LEAD — Access Previous/Next Rows

```sql
-- Show each transaction alongside the previous transaction amount
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
    ) as change_from_previous
FROM transactions t
JOIN accounts a ON t.account_id = a.account_id
ORDER BY a.customer_name, t.transaction_date;
```

### Running Totals

```sql
-- Calculate a running balance for each account
SELECT
    a.customer_name,
    t.transaction_date,
    t.amount,
    t.transaction_type,
    SUM(t.amount) OVER (
        PARTITION BY t.account_id
        ORDER BY t.transaction_date
        ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW
    ) as running_balance
FROM transactions t
JOIN accounts a ON t.account_id = a.account_id
ORDER BY a.customer_name, t.transaction_date;
```

---

## Topic 3: Subqueries vs JOINs

### When to Use Subqueries

- Filtering based on aggregate results
- EXISTS/NOT EXISTS checks
- Single-value lookups

```sql
-- Find accounts with above-average total deposits
SELECT a.customer_name, a.account_type
FROM accounts a
WHERE a.account_id IN (
    SELECT account_id
    FROM transactions
    WHERE transaction_type = 'Deposit'
    GROUP BY account_id
    HAVING SUM(amount) > (
        SELECT AVG(total)
        FROM (
            SELECT SUM(amount) as total
            FROM transactions
            WHERE transaction_type = 'Deposit'
            GROUP BY account_id
        )
    )
);
```

### When to Use JOINs

- Combining columns from multiple tables
- When you need data from both sides
- Generally better performance for large datasets

---

## Topic 4: Query Performance Basics

### Using EXPLAIN

```sql
-- See how SQLite plans to execute your query
EXPLAIN QUERY PLAN
SELECT a.customer_name, SUM(t.amount)
FROM accounts a
JOIN transactions t ON a.account_id = t.account_id
GROUP BY a.customer_name;
```

### Index Basics

```sql
-- Create an index to speed up transaction lookups by date
CREATE INDEX idx_transactions_date ON transactions(transaction_date);

-- Create a composite index for common query patterns
CREATE INDEX idx_transactions_account_date
ON transactions(account_id, transaction_date);
```

**Key rule**: Index columns that appear in WHERE, JOIN, and ORDER BY clauses.

---

## Hands-On Exercises

Complete the exercises in the `exercises/` folder:

1. **`01_window_functions.sql`** — Practice ROW_NUMBER, RANK, LAG/LEAD, and running totals
2. **`02_ctes_subqueries.sql`** — Build multi-step queries using CTEs and subqueries
3. **`03_performance_tuning.sql`** — Analyze and optimize slow queries

After attempting each exercise, check your work against the files in `solutions/`.

---

## Key Takeaways

1. **CTEs make complex SQL readable** — Name your steps, don't nest them
2. **Window functions are essential** — ROW_NUMBER, RANK, LAG/LEAD, running totals
3. **Choose the right tool** — Subqueries for filtering, JOINs for combining
4. **Performance matters** — Use EXPLAIN and indexes on large datasets

---

## What's Next?

In [Session 2: Introduction to Apache Airflow](../session02-airflow-intro/README.md), you'll learn how to schedule and orchestrate these SQL transformations so they run automatically. Session 2 is also free!

---

**Ready for the next session?** Head to [Session 02: Introduction to Apache Airflow](../session02-airflow-intro/README.md)
