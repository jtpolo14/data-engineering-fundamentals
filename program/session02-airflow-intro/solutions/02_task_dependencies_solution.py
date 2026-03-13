"""
Solution 2: Task Dependencies DAG
"""

from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.operators.bash import BashOperator


default_args = {
    'owner': 'data_engineer',
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}


def extract_accounts():
    print("Extracting 5 accounts from source...")


def extract_transactions():
    print("Extracting 20 transactions from source...")


def validate_data():
    print("Validating data... All records passed checks.")


def transform_data():
    print("Transforming data... Applied business rules.")


def generate_report():
    today = datetime.now().strftime('%Y-%m-%d')
    print(f"Report generated: banking_report_{today}.pdf")


with DAG(
    dag_id='banking_data_pipeline',
    default_args=default_args,
    description='Banking data pipeline with complex dependencies',
    schedule_interval=None,
    start_date=datetime(2024, 1, 1),
    catchup=False,
    tags=['banking', 'pipeline'],
) as dag:

    task_extract_accounts = PythonOperator(
        task_id='extract_accounts',
        python_callable=extract_accounts,
    )

    task_extract_transactions = PythonOperator(
        task_id='extract_transactions',
        python_callable=extract_transactions,
    )

    task_validate = PythonOperator(
        task_id='validate_data',
        python_callable=validate_data,
    )

    task_transform = PythonOperator(
        task_id='transform_data',
        python_callable=transform_data,
    )

    task_notify = BashOperator(
        task_id='send_notification',
        bash_command='echo "Pipeline notification sent at $(date)"',
    )

    task_report = PythonOperator(
        task_id='generate_report',
        python_callable=generate_report,
    )

    # Parallel extracts -> validate -> transform
    [task_extract_accounts, task_extract_transactions] >> task_validate >> task_transform

    # Both transform and notify must complete before report
    [task_transform, task_notify] >> task_report
