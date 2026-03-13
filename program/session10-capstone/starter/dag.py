"""
Capstone Starter: Airflow DAG for Banking Pipeline

TODO: Wire the pipeline functions into an Airflow DAG with proper dependencies.
"""

from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator


default_args = {
    'owner': 'data_engineer',
    'retries': 2,
    'retry_delay': timedelta(minutes=5),
}


# TODO: Import or define your pipeline functions here


# TODO: Define the DAG
# - dag_id: 'banking_analytics_pipeline'
# - schedule: '@daily'
# - start_date: datetime(2024, 1, 1)
# - catchup: False


# TODO: Define tasks for each pipeline stage:
# 1. extract_transactions_task
# 2. extract_customers_task
# 3. clean_data_task
# 4. enrich_data_task
# 5. load_data_task
# 6. quality_checks_task


# TODO: Set dependencies:
# - Both extracts run in parallel
# - Clean runs after both extracts
# - Enrich runs after clean
# - Load runs after enrich
# - Quality checks run after load
