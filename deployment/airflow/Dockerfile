FROM apache/airflow:2.10.0-python3.11

USER root

RUN apt-get update && \
    apt-get install -y \
        git \
        curl \
        wget && \
    rm -rf /var/lib/apt/lists/*

USER airflow

COPY deployment/airflow/requirements.txt /tmp/requirements.txt

RUN pip install --no-cache-dir -r /tmp/requirements.txt