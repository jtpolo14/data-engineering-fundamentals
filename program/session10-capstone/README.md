# Session 10: Capstone — End-to-End Data Pipeline

Welcome to the final session of **Data Engineering Fundamentals**! In this capstone, you'll bring everything together to build a complete data pipeline from source to analytics-ready data.

**This is a paid session.** [View pricing](../README.md#pricing)

---

## Learning Objectives

By the end of this session, you will be able to:

- Architect an end-to-end data pipeline
- Extract data from multiple sources (CSV files + JSON API)
- Transform data with Python and dbt models
- Load data into a local warehouse (SQLite/DuckDB)
- Orchestrate the pipeline with Apache Airflow
- Add data quality checks at each stage

---

## The Project: Banking Analytics Pipeline

You'll build a pipeline that processes banking transaction data from two sources:

1. **CSV file** — Historical transactions (`data/sample_transactions.csv`)
2. **JSON file** — Customer records (`data/sample_customers.json`)

### Pipeline Architecture

```
[CSV File] ---\                                    /--- [staging models]
               >--- Extract --- Transform --- Load --- [intermediate models]
[JSON File] --/         |           |          |   \--- [marts models]
                        |           |          |
                   Validate    Clean &     DuckDB/    Quality
                    schema     enrich      SQLite     checks
                        \           |          /
                         \--- Airflow DAG ---/
```

### Deliverables

1. **Python extraction scripts** — Read from both sources
2. **Transformation logic** — Clean, validate, enrich
3. **dbt models** — Staging, intermediate, and marts layers
4. **Airflow DAG** — Orchestrate the full pipeline
5. **Data quality checks** — Validation at each stage

---

## Getting Started

### Starter Code

The `starter/` directory contains skeleton files to get you going:

- `pipeline.py` — Pipeline functions with TODOs
- `dag.py` — Airflow DAG skeleton
- `models/staging.sql` — First dbt model template

### Sample Data

The `data/` directory contains:

- `sample_transactions.csv` — 100 banking transactions
- `sample_customers.json` — 10 customer records

### Requirements

```bash
pip install -r requirements.txt
```

---

## Step-by-Step Guide

### Step 1: Extract (45 min)
- Read transactions from CSV using Pandas
- Read customers from JSON
- Validate that both sources loaded correctly

### Step 2: Transform (60 min)
- Clean transaction data (handle nulls, fix types, remove duplicates)
- Enrich with customer data (join on account_id)
- Calculate derived fields (running balances, category summaries)

### Step 3: Load (30 min)
- Create target tables in SQLite/DuckDB
- Load transformed data with upsert logic
- Verify row counts and data integrity

### Step 4: dbt Models (45 min)
- Create staging models from raw loaded tables
- Build intermediate models with business logic
- Create marts models for analytics consumption

### Step 5: Orchestrate (30 min)
- Wire everything into an Airflow DAG
- Set up task dependencies
- Add error handling and retries

### Step 6: Quality Checks (30 min)
- Add validation after extraction
- Add quality checks after transformation
- Add integrity checks after loading

---

## Solution

A complete working solution is in the `solution/` directory. Try to build it yourself first!

---

## What You've Learned

After completing this program, you can:

- Write production SQL (window functions, CTEs, optimization)
- Orchestrate workflows with Apache Airflow
- Build ETL/ELT pipelines in Python
- Design dimensional data models
- Work with cloud data platforms
- Ensure data quality with automated testing
- Transform warehouse data with dbt
- Architect end-to-end data pipelines

**You're ready for a Junior/Mid-Level Data Engineer role.**

---

## Next Steps

- Add this capstone to your portfolio (GitHub)
- Extend the pipeline with real APIs or cloud services
- Explore advanced topics: streaming, Spark, Kafka

---

**Congratulations on completing Data Engineering Fundamentals!**
