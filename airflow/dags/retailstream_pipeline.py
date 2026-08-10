from datetime import datetime, timedelta

from airflow import DAG
from airflow.operators.python import PythonOperator

from src.orchestration.docker_executor import DockerExecutor


def run_bronze():
    DockerExecutor().run_script("run_spark_bronze.py")


def run_silver():
    DockerExecutor().run_script("run_spark_silver.py")


def run_gold():
    DockerExecutor().run_script("run_spark_gold.py")


def run_warehouse():
    DockerExecutor().run_script("run_warehouse.py")


default_args = {
    "owner": "retailstream",
    "retries": 2,
    "retry_delay": timedelta(minutes=2),
}


with DAG(
    dag_id="retailstream_pipeline",
    description="RetailStream ETL Pipeline",
    start_date=datetime(2026, 1, 1),
    schedule=None,
    catchup=False,
    default_args=default_args,
    tags=["RetailStream"],
) as dag:

    bronze = PythonOperator(
        task_id="bronze",
        python_callable=run_bronze,
    )

    silver = PythonOperator(
        task_id="silver",
        python_callable=run_silver,
    )

    gold = PythonOperator(
        task_id="gold",
        python_callable=run_gold,
    )

    warehouse = PythonOperator(
        task_id="warehouse",
        python_callable=run_warehouse,
    )

    bronze >> silver >> gold >> warehouse