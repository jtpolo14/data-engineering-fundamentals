# Session 05: Building ETL/ELT Pipelines

Welcome to Session 5 of **Data Engineering Fundamentals**! In this session, you'll build a complete data pipeline from extraction through loading.

**This is a paid session.** [View pricing](../README.md#pricing)

---

## Learning Objectives

By the end of this session, you will be able to:

- Explain the difference between ETL and ELT approaches
- Extract data from CSVs, APIs, and databases using Python
- Transform data with cleaning, deduplication, and business logic
- Load data into SQLite/PostgreSQL databases
- Build idempotent, logged, and error-handled pipelines

---

## Topics Covered

### 1. ETL vs ELT
- Traditional ETL: transform before loading
- Modern ELT: load raw, transform in the warehouse
- When to use which approach

### 2. Extract
- Reading from flat files (CSV, JSON, Parquet)
- Pulling from REST APIs with pagination
- Querying source databases
- Incremental vs full extraction

### 3. Transform
- Data cleaning: nulls, duplicates, type casting
- Business logic: categorization, calculations, enrichment
- Validation: schema checks, range checks, referential integrity
- Logging and audit trails

### 4. Load
- Inserting into databases (SQLite, PostgreSQL)
- Upsert patterns (insert or update)
- Bulk loading for performance
- Idempotency: safe to re-run without duplicates

---

## Exercises

1. **`01_extract_csv_api.py`** — Extract banking data from CSV files and a mock API
2. **`02_transform_clean.py`** — Clean, validate, and enrich transaction data
3. **`03_load_database.py`** — Load transformed data into SQLite with upsert logic

---

## Prerequisites

- Sessions 1, 3, and 4 completed

---

**Next:** [Session 06: Airflow in Practice](../session06-airflow-dags/README.md)
