# Session 08: Data Quality & Testing

Welcome to Session 8 of **Data Engineering Fundamentals**! In this session, you'll learn how to ensure the data your pipelines produce is accurate and reliable.

**This is a paid session.** [View pricing](../README.md#pricing)

---

## Learning Objectives

By the end of this session, you will be able to:

- Explain why data quality is a critical part of data engineering
- Implement schema validation and type checking in Python
- Use the Great Expectations framework for automated data testing
- Define data quality metrics: completeness, accuracy, timeliness, consistency
- Build monitoring and alerting patterns for pipeline health

---

## Topics Covered

### 1. Why Data Quality Matters
- Real-world consequences of bad data
- The cost of data issues found late vs early
- Data quality as a shared responsibility

### 2. Schema Validation & Type Checking
- Validating column names, types, and constraints
- Null checks, range checks, uniqueness checks
- Building reusable validation functions in Python

### 3. Great Expectations Framework
- Installing and configuring Great Expectations
- Writing Expectations (expect_column_to_exist, expect_values_to_be_between, etc.)
- Expectation Suites and Checkpoints
- Generating data documentation automatically

### 4. Data Quality Metrics
- Completeness: are all expected records present?
- Accuracy: do values match reality?
- Timeliness: is data arriving on schedule?
- Consistency: do related datasets agree?

### 5. Monitoring & Alerting
- Logging data quality results
- Threshold-based alerting
- Building a simple data quality dashboard
- Integrating quality checks into Airflow DAGs

---

## Exercises

1. **`01_validation_checks.py`** — Build validation functions for banking transaction data
2. **`02_great_expectations.py`** — Create an Expectation Suite for the transactions dataset
3. **`03_monitoring_alerts.py`** — Build a monitoring script that logs quality metrics and alerts on failures

---

## Prerequisites

- Sessions 5 and 6 completed

---

**Next:** [Session 09: Analytics Engineering with dbt](../session09-dbt-analytics-engineering/README.md)
