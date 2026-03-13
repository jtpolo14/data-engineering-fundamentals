# Session 02: Introduction to Apache Airflow & Orchestration

Welcome to Session 2 of **Data Engineering Fundamentals**! In this session, you'll learn why orchestration matters and write your first Apache Airflow DAG.

**This session is FREE.**

---

## Learning Objectives

By the end of this session, you will be able to:

- Explain what data orchestration is and why it matters
- Describe Airflow's core architecture (scheduler, webserver, metadata DB)
- Define key concepts: DAGs, tasks, operators, dependencies
- Set up Airflow locally using Docker Compose
- Write and trigger your first DAG

---

## What is Data Orchestration?

As an analyst, you might manually run SQL queries or scripts each morning. As a data engineer, you need those processes to:

- **Run automatically** on a schedule (daily, hourly, etc.)
- **Handle failures** gracefully (retry, alert, skip)
- **Run in order** (don't transform data before extracting it)
- **Scale** as you add more pipelines

**Orchestration** is the automation and coordination of these data workflows. Apache Airflow is the most widely-used orchestration tool in data engineering.

---

## Airflow Architecture

```
                    +-----------+
                    |  Web UI   |  (Monitor DAGs, view logs)
                    +-----+-----+
                          |
                    +-----+-----+
                    | Scheduler |  (Decides when to run tasks)
                    +-----+-----+
                          |
                    +-----+-----+
                    |  Executor |  (Runs the actual tasks)
                    +-----+-----+
                          |
                    +-----+-----+
                    | Metadata  |  (Stores state in PostgreSQL/SQLite)
                    |    DB     |
                    +-----------+
```

- **Scheduler** — Monitors all DAGs and triggers tasks when dependencies are met
- **Web Server** — The UI where you monitor, trigger, and debug DAGs
- **Executor** — Runs your tasks (locally, on Celery workers, or Kubernetes)
- **Metadata DB** — Stores DAG definitions, run history, and task states

---

## Core Concepts

### DAG (Directed Acyclic Graph)

A DAG defines your workflow — what tasks run and in what order. "Directed" means tasks have a defined sequence. "Acyclic" means no circular dependencies.

```
Extract  -->  Transform  -->  Load
                                \
                                 --> Send Report
```

### Tasks

A task is a single unit of work within a DAG. Each box above is a task.

### Operators

Operators define what a task actually does:

- **PythonOperator** — Runs a Python function
- **BashOperator** — Runs a shell command
- **SQLExecuteQueryOperator** — Runs a SQL query
- **EmailOperator** — Sends an email

### Task Dependencies

You define the order tasks run using `>>` (downstream) or `<<` (upstream):

```python
extract >> transform >> load  # extract runs first, then transform, then load
```

---

## Setting Up Airflow with Docker

### Step 1: Install Docker Desktop

Download and install [Docker Desktop](https://www.docker.com/products/docker-desktop/). Make sure it's running before proceeding.

### Step 2: Create a Docker Compose File

Create a file called `docker-compose.yml`:

```yaml
version: '3.8'
x-airflow-common:
  &airflow-common
  image: apache/airflow:2.8.1
  environment:
    &airflow-common-env
    AIRFLOW__CORE__EXECUTOR: LocalExecutor
    AIRFLOW__DATABASE__SQL_ALCHEMY_CONN: postgresql+psycopg2://airflow:airflow@postgres/airflow
    AIRFLOW__CORE__FERNET_KEY: ''
    AIRFLOW__CORE__DAGS_ARE_PAUSED_AT_CREATION: 'true'
    AIRFLOW__CORE__LOAD_EXAMPLES: 'false'
  volumes:
    - ./dags:/opt/airflow/dags
    - ./logs:/opt/airflow/logs
  depends_on:
    postgres:
      condition: service_healthy

services:
  postgres:
    image: postgres:13
    environment:
      POSTGRES_USER: airflow
      POSTGRES_PASSWORD: airflow
      POSTGRES_DB: airflow
    healthcheck:
      test: ["CMD", "pg_isready", "-U", "airflow"]
      interval: 10s
      retries: 5
    ports:
      - "5432:5432"

  airflow-init:
    <<: *airflow-common
    entrypoint: /bin/bash
    command:
      - -c
      - |
        airflow db migrate
        airflow users create \
          --username admin \
          --firstname Admin \
          --lastname User \
          --role Admin \
          --email admin@example.com \
          --password admin
    depends_on:
      postgres:
        condition: service_healthy

  airflow-webserver:
    <<: *airflow-common
    command: webserver
    ports:
      - "8080:8080"
    healthcheck:
      test: ["CMD", "curl", "--fail", "http://localhost:8080/health"]
      interval: 30s
      timeout: 10s
      retries: 5

  airflow-scheduler:
    <<: *airflow-common
    command: scheduler
```

### Step 3: Start Airflow

```bash
# Create the dags and logs directories
mkdir -p dags logs

# Initialize and start Airflow
docker compose up airflow-init
docker compose up -d

# Wait ~30 seconds, then open http://localhost:8080
# Login: admin / admin
```

### No Docker? No Problem

If you can't run Docker, you can still follow along:
- Read through the code examples
- Use the [Airflow Playground](https://airflow.apache.org/) docs for reference
- The exercises include expected output screenshots

---

## Your First DAG

Create a file called `dags/my_first_dag.py`:

```python
from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.operators.bash import BashOperator


# Define default arguments for all tasks
default_args = {
    'owner': 'data_engineer',
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}


def extract_data():
    """Simulate extracting banking transaction data."""
    print("Extracting transaction data from source system...")
    transactions = [
        {"id": 1, "account": "12345", "amount": 150.00, "type": "deposit"},
        {"id": 2, "account": "12345", "amount": -45.99, "type": "withdrawal"},
        {"id": 3, "account": "67890", "amount": 2000.00, "type": "deposit"},
    ]
    print(f"Extracted {len(transactions)} transactions")
    return transactions


def transform_data():
    """Simulate transforming transaction data."""
    print("Transforming transaction data...")
    print("- Validating amounts")
    print("- Categorizing transactions")
    print("- Calculating running balances")
    print("Transformation complete!")


def load_data():
    """Simulate loading data into a warehouse."""
    print("Loading transformed data into warehouse...")
    print("- Inserting into fact_transactions table")
    print("- Updating dim_accounts table")
    print("Load complete!")


# Define the DAG
with DAG(
    dag_id='my_first_banking_etl',
    default_args=default_args,
    description='A simple banking ETL pipeline',
    schedule_interval='@daily',
    start_date=datetime(2024, 1, 1),
    catchup=False,
    tags=['banking', 'etl'],
) as dag:

    # Define tasks
    task_extract = PythonOperator(
        task_id='extract_transactions',
        python_callable=extract_data,
    )

    task_transform = PythonOperator(
        task_id='transform_transactions',
        python_callable=transform_data,
    )

    task_load = PythonOperator(
        task_id='load_to_warehouse',
        python_callable=load_data,
    )

    task_notify = BashOperator(
        task_id='send_notification',
        bash_command='echo "ETL pipeline completed successfully at $(date)"',
    )

    # Set dependencies
    task_extract >> task_transform >> task_load >> task_notify
```

### Running Your DAG

1. Save the file to your `dags/` folder
2. Open the Airflow UI at `http://localhost:8080`
3. Find `my_first_banking_etl` in the DAG list
4. Toggle the DAG ON (click the toggle switch)
5. Click the play button to trigger a manual run
6. Click on the DAG name to see the graph view and task logs

---

## Understanding DAG Parameters

| Parameter | Purpose | Example |
|-----------|---------|---------|
| `dag_id` | Unique name for the DAG | `'my_first_banking_etl'` |
| `schedule_interval` | How often to run | `'@daily'`, `'@hourly'`, `'0 6 * * *'` |
| `start_date` | When the DAG becomes active | `datetime(2024, 1, 1)` |
| `catchup` | Run missed intervals? | `False` (usually) |
| `default_args` | Shared task settings | retries, owner, etc. |

### Common Schedules

| Preset | Cron Equivalent | Meaning |
|--------|----------------|---------|
| `@daily` | `0 0 * * *` | Midnight every day |
| `@hourly` | `0 * * * *` | Top of every hour |
| `@weekly` | `0 0 * * 0` | Midnight every Sunday |
| `None` | — | Manual trigger only |

---

## Hands-On Exercises

Complete the exercises in the `exercises/` folder:

1. **`01_first_dag.py`** — Build a DAG that extracts account balances, calculates daily summaries, and prints a report
2. **`02_task_dependencies.py`** — Create a DAG with branching paths and multiple dependency chains

After attempting each exercise, check your work against the files in `solutions/`.

---

## Key Takeaways

1. **Orchestration automates and coordinates** your data workflows
2. **DAGs define what runs and in what order** — no circular dependencies
3. **Operators define what tasks do** — Python, Bash, SQL, and more
4. **Dependencies use `>>`** — `extract >> transform >> load`
5. **Airflow UI** is where you monitor, trigger, and debug

---

## What's Next?

You've completed both free sessions! You now have intermediate SQL skills and understand how Airflow orchestrates data pipelines.

In [Session 3: Python for Data Engineering](../session03-python-for-de/README.md), you'll learn to use Python and Pandas for data extraction, transformation, and loading — the core of what a data engineer does daily.

**Ready to continue?** [View pricing and enroll](../README.md#pricing) to unlock Sessions 3-10.

---

**Questions?** Open an issue on [GitHub](https://github.com/jtpolo14/data-engineering-fundamentals)
