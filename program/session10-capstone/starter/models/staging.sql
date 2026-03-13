-- Capstone Starter: Staging Model for Transactions
--
-- TODO: Write a dbt model that:
-- 1. Selects from the raw transactions table
-- 2. Casts columns to proper types
-- 3. Renames columns to follow your naming convention
-- 4. Adds a loaded_at timestamp
--
-- Materialization: view (staging models are typically views)

-- {{ config(materialized='view') }}

-- SELECT
--     TODO: your columns here
-- FROM {{ source('raw', 'transactions') }}
