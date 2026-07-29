# RetailStream Data Platform

Enterprise-grade Batch Data Engineering Platform built using:

- Apache Spark
- Apache Airflow
- MinIO
- Delta Lake
- PostgreSQL
- dbt
- Apache Superset
- Docker


# Configuration Framework

## Purpose

The Configuration Framework provides a centralized mechanism for loading,
validating, and accessing configuration throughout the RetailStream platform.

## Responsibilities

- Load YAML configuration files
- Load environment variables
- Validate configuration
- Provide a single API for configuration access

## Consumers

- Data Generator
- Airflow
- Spark
- Source Systems
- Monitoring
- Warehouse