# Session 03: Python for Data Engineering

Welcome to Session 3 of **Data Engineering Fundamentals**! In this session, you'll learn to use Python and Pandas for the kind of data work that data engineers do daily.

**This is a paid session.** [View pricing](../README.md#pricing)

---

## Learning Objectives

By the end of this session, you will be able to:

- Use Pandas to read and write CSV, JSON, and Parquet files
- Filter, group, merge, and transform DataFrames
- Extract data from REST APIs using the `requests` library
- Handle large files with chunked reading and memory management
- Manage project dependencies with virtual environments

---

## Topics Covered

### 1. Pandas for Data Engineers
- Reading/writing multiple file formats (CSV, JSON, Parquet)
- DataFrame operations: filtering, selecting, sorting
- GroupBy and aggregations for transaction summaries
- Merging DataFrames (left join, inner join, anti-join patterns)

### 2. Working with APIs
- Making GET/POST requests with `requests`
- Parsing JSON responses into DataFrames
- Handling pagination and rate limiting
- Error handling for unreliable endpoints

### 3. File Processing at Scale
- Chunked reading for large CSVs
- Memory profiling and optimization
- Data type optimization (downcasting, categoricals)
- When to use Parquet over CSV

### 4. Environment Management
- Creating virtual environments with `venv`
- Managing dependencies with `requirements.txt`
- Reproducible environments for pipeline code

---

## Exercises

1. **`01_pandas_basics.py`** — Load banking transaction CSVs, merge with account data, calculate monthly summaries
2. **`02_file_processing.py`** — Process a large transaction file in chunks, convert between formats
3. **`03_api_extraction.py`** — Extract data from a mock banking API, handle pagination, save results

---

## Prerequisites

- Sessions 1-2 completed
- Basic Python knowledge (see [Python Fundamentals](../../section1-foundations/lecture01/README.md))

---

**Next:** [Session 04: Data Modeling & Warehouse Design](../session04-data-modeling/README.md)
