# Session 04: Data Modeling & Warehouse Design

Welcome to Session 4 of **Data Engineering Fundamentals**! In this session, you'll learn how to design the data structures that power dashboards and analytics.

**This is a paid session.** [View pricing](../README.md#pricing)

---

## Learning Objectives

By the end of this session, you will be able to:

- Explain the difference between OLTP and OLAP systems
- Normalize data to 3NF and know when to denormalize
- Design star schemas with fact and dimension tables
- Implement Slowly Changing Dimensions (Type 1, 2, and 3)
- Model a banking data warehouse from scratch

---

## Topics Covered

### 1. OLTP vs OLAP
- Transactional systems vs analytical systems
- Why you can't just query the production database
- The role of the data warehouse

### 2. Normalization
- First, Second, and Third Normal Form (1NF, 2NF, 3NF)
- When normalization helps and when it hurts
- Denormalization for query performance

### 3. Dimensional Modeling
- Fact tables: what happened (transactions, events, measurements)
- Dimension tables: context (who, what, where, when)
- Star schema vs snowflake schema
- Grain: the level of detail in your fact table

### 4. Slowly Changing Dimensions (SCDs)
- Type 1: Overwrite (no history)
- Type 2: Add new row (full history)
- Type 3: Add new column (limited history)
- Choosing the right type for your use case

---

## Exercises

1. **`01_star_schema.sql`** — Design a star schema for the banking transaction data
2. **`02_slowly_changing_dims.sql`** — Implement SCD Type 2 for customer account changes
3. **`03_normalization.sql`** — Normalize a denormalized transactions table to 3NF

---

## Prerequisites

- Sessions 1 and 3 completed

---

**Next:** [Session 05: Building ETL/ELT Pipelines](../session05-etl-elt-pipelines/README.md)
