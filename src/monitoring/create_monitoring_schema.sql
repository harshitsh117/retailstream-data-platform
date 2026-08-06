CREATE SCHEMA IF NOT EXISTS monitoring;

CREATE TABLE IF NOT EXISTS monitoring.pipeline_execution (

    execution_id UUID PRIMARY KEY,

    pipeline_name VARCHAR(100) NOT NULL,

    layer VARCHAR(50) NOT NULL,

    status VARCHAR(20) NOT NULL,

    start_time TIMESTAMPTZ NOT NULL,

    end_time TIMESTAMPTZ,

    duration_seconds DOUBLE PRECISION,

    rows_read BIGINT,

    rows_written BIGINT,

    rows_rejected BIGINT,

    error_message TEXT,

    hostname VARCHAR(255),

    airflow_run_id VARCHAR(255),

    created_at TIMESTAMPTZ NOT NULL
);