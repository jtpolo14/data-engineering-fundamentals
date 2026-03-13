"""
Exercise 2: Task Dependencies

Create a DAG called 'banking_data_pipeline' with the following task structure:

    extract_accounts ----\
                          >--- validate_data --- transform_data ---\
    extract_transactions -/                                         >--- generate_report
                                                                   /
                                        send_notification ---------

Requirements:
- extract_accounts and extract_transactions should run IN PARALLEL
- validate_data runs AFTER both extracts complete
- transform_data runs AFTER validation
- send_notification runs independently (no upstream dependencies)
- generate_report runs AFTER both transform_data AND send_notification complete
- Schedule: None (manual trigger only)
- Use BashOperator for send_notification, PythonOperator for everything else
"""

from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.operators.bash import BashOperator


# TODO: Define default_args


# TODO: Write task functions
# extract_accounts: print "Extracting 5 accounts from source..."
# extract_transactions: print "Extracting 20 transactions from source..."
# validate_data: print "Validating data... All records passed checks."
# transform_data: print "Transforming data... Applied business rules."
# generate_report: print "Report generated: banking_report_YYYY-MM-DD.pdf"


# TODO: Define the DAG with schedule=None


# TODO: Define all tasks


# TODO: Set up the dependency chain described above
# Hint: You can set multiple upstream dependencies like:
#   task_c.set_upstream([task_a, task_b])
# Or equivalently:
#   [task_a, task_b] >> task_c
