# Session 06: Airflow in Practice — Building Production DAGs

Welcome to Session 6 of **Data Engineering Fundamentals**! In this session, you'll build production-grade Airflow DAGs with branching, sensors, and error handling.

**This is a paid session.** [View pricing](../README.md#pricing)

---

## Learning Objectives

By the end of this session, you will be able to:

- Use PythonOperator, BashOperator, and SQL operators effectively
- Implement conditional logic with BranchPythonOperator
- Wait for external events with Sensors (FileSensor, HttpSensor)
- Configure retries, SLAs, and alerting for production reliability
- Build a multi-step ETL DAG that handles failures gracefully

---

## Topics Covered

### 1. Operators Deep Dive
- PythonOperator: passing arguments, return values, XCom
- BashOperator: running shell commands and scripts
- SQL operators: executing queries against databases
- Custom operators: when and how to build your own

### 2. Task Dependencies & Trigger Rules
- Advanced dependency patterns
- Trigger rules: all_success, one_success, all_done, none_failed
- Dynamic task generation

### 3. Branching & Conditional Logic
- BranchPythonOperator for if/else workflows
- ShortCircuitOperator for conditional skipping
- Choosing paths based on data conditions

### 4. Sensors
- FileSensor: wait for a file to appear
- HttpSensor: wait for an API to respond
- Sensor timeout and poke intervals
- Sensor modes: poke vs reschedule

### 5. Error Handling & Reliability
- Retries and exponential backoff
- on_failure_callback for alerting
- SLAs and SLA miss callbacks
- Task-level and DAG-level error handling

---

## Exercises

1. **`01_etl_dag.py`** — Build a full ETL DAG using the pipeline from Session 5
2. **`02_branching_and_sensors.py`** — Create a DAG that waits for a file, then branches based on content
3. **`03_error_handling_dag.py`** — Add retries, alerts, and SLAs to a production DAG

---

## Prerequisites

- Sessions 2, 3, and 5 completed

---

**Next:** [Session 07: Cloud Data Platforms](../session07-cloud-platforms/README.md)
