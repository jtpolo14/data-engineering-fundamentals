"""
Exercise 1: Build Your First DAG

Create a DAG called 'daily_account_summary' that:
1. Extracts account balance data (use the provided function)
2. Calculates a daily summary (total deposits, total withdrawals, net change)
3. Prints a formatted report

Requirements:
- DAG should run daily
- Use PythonOperator for all tasks
- Set retries to 2 with a 3-minute delay
- Tasks must run in order: extract -> calculate -> report
"""

from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator


# -- PROVIDED: Use this data in your extract task --
SAMPLE_BALANCES = [
    {"account_id": 1, "customer": "Jane Smith", "balance": 1284.01, "deposits": 1500.00, "withdrawals": 215.99},
    {"account_id": 2, "customer": "John Doe", "balance": 1500.00, "deposits": 2000.00, "withdrawals": 500.00},
    {"account_id": 3, "customer": "Alice Johnson", "balance": 2785.50, "deposits": 3200.00, "withdrawals": 414.50},
    {"account_id": 4, "customer": "Bob Williams", "balance": 1500.00, "deposits": 1500.00, "withdrawals": 0.00},
    {"account_id": 5, "customer": "Carol Davis", "balance": 2270.00, "deposits": 2800.00, "withdrawals": 530.00},
]


# TODO: Define your default_args


# TODO: Write the extract_balances function
# It should print the number of accounts extracted


# TODO: Write the calculate_summary function
# It should calculate and print:
#   - Total deposits across all accounts
#   - Total withdrawals across all accounts
#   - Net change (deposits - withdrawals)
#   - Account with the highest balance


# TODO: Write the print_report function
# It should print a formatted report like:
#   === Daily Account Summary ===
#   Date: 2024-01-15
#   Accounts Processed: 5
#   Total Deposits: $11,000.00
#   Total Withdrawals: $1,660.49
#   Net Change: $9,339.51
#   Top Account: Alice Johnson ($2,785.50)
#   =============================


# TODO: Define the DAG and tasks with proper dependencies
