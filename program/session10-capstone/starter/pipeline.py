"""
Capstone Starter: Banking Analytics Pipeline

Complete the TODO sections to build a full ETL pipeline.
"""

import pandas as pd
import json
import sqlite3
from datetime import datetime


# ============================================================
# EXTRACT
# ============================================================

def extract_transactions(filepath: str) -> pd.DataFrame:
    """Extract transactions from CSV file.

    TODO:
    - Read the CSV file into a DataFrame
    - Print the number of rows extracted
    - Return the DataFrame
    """
    pass


def extract_customers(filepath: str) -> pd.DataFrame:
    """Extract customers from JSON file.

    TODO:
    - Read the JSON file into a DataFrame
    - Print the number of customers extracted
    - Return the DataFrame
    """
    pass


# ============================================================
# TRANSFORM
# ============================================================

def clean_transactions(df: pd.DataFrame) -> pd.DataFrame:
    """Clean and validate transaction data.

    TODO:
    - Remove duplicate transaction_ids
    - Convert transaction_date to datetime
    - Ensure amount is numeric
    - Drop rows with null account_id
    - Print how many rows were cleaned/removed
    - Return the cleaned DataFrame
    """
    pass


def enrich_transactions(transactions: pd.DataFrame, customers: pd.DataFrame) -> pd.DataFrame:
    """Enrich transactions with customer data.

    TODO:
    - Left join transactions with customers on account_id
    - Add a 'month' column (YYYY-MM format)
    - Add a 'is_debit' boolean column (True if amount < 0)
    - Return the enriched DataFrame
    """
    pass


# ============================================================
# LOAD
# ============================================================

def load_to_database(df: pd.DataFrame, table_name: str, db_path: str = "banking.db"):
    """Load DataFrame into SQLite database.

    TODO:
    - Connect to SQLite database
    - Write DataFrame to the specified table (replace if exists)
    - Print the number of rows loaded
    - Close the connection
    """
    pass


# ============================================================
# QUALITY CHECKS
# ============================================================

def run_quality_checks(db_path: str = "banking.db"):
    """Run data quality checks on loaded data.

    TODO:
    - Check that the transactions table has rows
    - Check that there are no null account_ids
    - Check that all transaction dates are valid
    - Check that deposits are positive and withdrawals are negative
    - Print PASS/FAIL for each check
    """
    pass


# ============================================================
# MAIN
# ============================================================

if __name__ == "__main__":
    print("=" * 50)
    print("Banking Analytics Pipeline")
    print(f"Run date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 50)

    # TODO: Call your functions in order:
    # 1. Extract transactions and customers
    # 2. Clean transactions
    # 3. Enrich transactions with customer data
    # 4. Load to database
    # 5. Run quality checks
    # 6. Print summary

    print("\nPipeline complete!")
