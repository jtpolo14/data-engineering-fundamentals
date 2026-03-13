# Session 07: Cloud Data Platforms

Welcome to Session 7 of **Data Engineering Fundamentals**! In this session, you'll learn how data engineering works in the cloud.

**This is a paid session.** [View pricing](../README.md#pricing)

---

## Learning Objectives

By the end of this session, you will be able to:

- Compare AWS, GCP, and Azure data services at a high level
- Use object storage (S3/GCS) as a data lake foundation
- Understand cloud data warehouse options (Snowflake, BigQuery, Redshift)
- Distinguish between data lake, data warehouse, and data lakehouse
- Describe Infrastructure as Code basics with Terraform

---

## Topics Covered

### 1. Cloud Data Platform Overview
- AWS vs GCP vs Azure: key services comparison
- When to use which cloud (or multi-cloud)
- Cost considerations for data engineering

### 2. Object Storage as a Data Lake
- S3 (AWS), GCS (Google), Blob Storage (Azure)
- Bucket organization and partitioning strategies
- File formats for the lake: Parquet, ORC, Avro
- Using LocalStack for free local S3 simulation

### 3. Cloud Data Warehouses
- Snowflake: architecture and key concepts
- BigQuery: serverless analytics
- Redshift: AWS-native warehousing
- Choosing the right warehouse for your needs

### 4. Data Lake vs Warehouse vs Lakehouse
- Traditional data warehouse limitations
- Data lake promises and pitfalls
- The lakehouse pattern (Delta Lake, Iceberg, Hudi)

### 5. Infrastructure as Code
- Why IaC matters for data engineering
- Terraform basics: providers, resources, state
- Defining S3 buckets and IAM roles as code

---

## Exercises

1. **`01_s3_data_lake.py`** — Upload/download banking data to a local S3 (LocalStack)
2. **`02_warehouse_queries.sql`** — Write warehouse-optimized queries with partitioning and clustering
3. **`03_cloud_architecture.md`** — Design a cloud architecture diagram for a banking data platform

---

## Prerequisites

- Sessions 4 and 5 completed
- Docker Desktop installed (for LocalStack)

---

**Next:** [Session 08: Data Quality & Testing](../session08-data-quality/README.md)
