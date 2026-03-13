"""
Solution 1: Daily Account Summary DAG
"""

from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator


SAMPLE_BALANCES = [
    {"account_id": 1, "customer": "Jane Smith", "balance": 1284.01, "deposits": 1500.00, "withdrawals": 215.99},
    {"account_id": 2, "customer": "John Doe", "balance": 1500.00, "deposits": 2000.00, "withdrawals": 500.00},
    {"account_id": 3, "customer": "Alice Johnson", "balance": 2785.50, "deposits": 3200.00, "withdrawals": 414.50},
    {"account_id": 4, "customer": "Bob Williams", "balance": 1500.00, "deposits": 1500.00, "withdrawals": 0.00},
    {"account_id": 5, "customer": "Carol Davis", "balance": 2270.00, "deposits": 2800.00, "withdrawals": 530.00},
]


default_args = {
    'owner': 'data_engineer',
    'retries': 2,
    'retry_delay': timedelta(minutes=3),
}


def extract_balances():
    """Extract account balance data."""
    print(f"Extracted {len(SAMPLE_BALANCES)} accounts")
    for account in SAMPLE_BALANCES:
        print(f"  Account {account['account_id']}: {account['customer']} - ${account['balance']:,.2f}")
    return SAMPLE_BALANCES


def calculate_summary():
    """Calculate daily summary statistics."""
    total_deposits = sum(a['deposits'] for a in SAMPLE_BALANCES)
    total_withdrawals = sum(a['withdrawals'] for a in SAMPLE_BALANCES)
    net_change = total_deposits - total_withdrawals
    top_account = max(SAMPLE_BALANCES, key=lambda a: a['balance'])

    print(f"Total Deposits: ${total_deposits:,.2f}")
    print(f"Total Withdrawals: ${total_withdrawals:,.2f}")
    print(f"Net Change: ${net_change:,.2f}")
    print(f"Top Account: {top_account['customer']} (${top_account['balance']:,.2f})")


def print_report():
    """Print a formatted daily report."""
    total_deposits = sum(a['deposits'] for a in SAMPLE_BALANCES)
    total_withdrawals = sum(a['withdrawals'] for a in SAMPLE_BALANCES)
    net_change = total_deposits - total_withdrawals
    top_account = max(SAMPLE_BALANCES, key=lambda a: a['balance'])

    print("=" * 35)
    print("=== Daily Account Summary ===")
    print(f"Date: {datetime.now().strftime('%Y-%m-%d')}")
    print(f"Accounts Processed: {len(SAMPLE_BALANCES)}")
    print(f"Total Deposits: ${total_deposits:,.2f}")
    print(f"Total Withdrawals: ${total_withdrawals:,.2f}")
    print(f"Net Change: ${net_change:,.2f}")
    print(f"Top Account: {top_account['customer']} (${top_account['balance']:,.2f})")
    print("=" * 35)


with DAG(
    dag_id='daily_account_summary',
    default_args=default_args,
    description='Daily summary of account balances',
    schedule_interval='@daily',
    start_date=datetime(2024, 1, 1),
    catchup=False,
    tags=['banking', 'summary'],
) as dag:

    task_extract = PythonOperator(
        task_id='extract_balances',
        python_callable=extract_balances,
    )

    task_calculate = PythonOperator(
        task_id='calculate_summary',
        python_callable=calculate_summary,
    )

    task_report = PythonOperator(
        task_id='print_report',
        python_callable=print_report,
    )

    task_extract >> task_calculate >> task_report
