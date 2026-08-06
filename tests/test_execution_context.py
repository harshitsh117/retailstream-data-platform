from src.monitoring.execution_context import ExecutionContext


def test_execution_context():
    context = ExecutionContext(
        pipeline_name="Bronze",
        layer="bronze",
    )

    assert context.pipeline_name == "Bronze"
    assert context.layer == "bronze"
    assert context.hostname is not None
    assert context.execution_id is not None
    assert context.airflow_run_id is None
    assert context.start_time is not None