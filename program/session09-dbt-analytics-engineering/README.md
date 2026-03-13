# Session 09: Analytics Engineering with dbt

Welcome to Session 9 of **Data Engineering Fundamentals**! In this session, you'll learn to use dbt (data build tool) to transform data in your warehouse using SQL.

**This is a paid session.** [View pricing](../README.md#pricing)

---

## Learning Objectives

By the end of this session, you will be able to:

- Explain what analytics engineering is and where dbt fits in the stack
- Set up a dbt project with models, tests, and documentation
- Choose the right materialization (table, view, incremental, ephemeral)
- Write and run dbt tests for data quality
- Use Jinja templating and macros for DRY SQL

---

## Topics Covered

### 1. What is Analytics Engineering?
- The role between data engineering and data analysis
- How dbt fits alongside Airflow and Python pipelines
- The ELT pattern: load raw, transform with dbt

### 2. dbt Project Structure
- Models: SQL SELECT statements that define transformations
- Staging, intermediate, and marts layers
- Sources and refs: managing dependencies
- Project configuration (dbt_project.yml, profiles.yml)

### 3. Materializations
- Table: full rebuild every run
- View: always up-to-date, no storage
- Incremental: only process new/changed rows
- Ephemeral: inline CTE, no database object

### 4. Testing & Documentation
- Schema tests: unique, not_null, accepted_values, relationships
- Custom data tests as SQL queries
- Auto-generated documentation with `dbt docs generate`
- Column-level descriptions in YAML

### 5. Jinja & Macros
- Jinja basics: variables, conditionals, loops in SQL
- Built-in macros (ref, source, config)
- Writing custom macros for reusable logic
- When to use macros vs when to keep it simple

---

## Exercises

1. **`01_first_dbt_model.sql`** — Write staging and marts models for banking transactions
2. **`02_testing_docs.yml`** — Define schema tests and documentation for your models
3. **`03_incremental_models.sql`** — Convert a full-refresh model to an incremental model

---

## Prerequisites

- Sessions 1, 4, and 5 completed
- dbt-core installed (`pip install dbt-core dbt-duckdb`)

---

**Next:** [Session 10: Capstone Project](../session10-capstone/README.md)
