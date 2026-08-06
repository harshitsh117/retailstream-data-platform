from src.monitoring.metrics_collector import MetricsCollector
from src.monitoring.enums import PipelineStatus


def test_metrics_success():

    metrics = MetricsCollector()

    metrics.rows_read = 100

    metrics.rows_written = 98

    metrics.rows_rejected = 2

    metrics.mark_success()

    assert metrics.status == PipelineStatus.SUCCESS
    assert metrics.rows_read == 100
    assert metrics.rows_written == 98
    assert metrics.rows_rejected == 2
    assert metrics.error_message is None


def test_metrics_failure():

    metrics = MetricsCollector()

    metrics.mark_failure("Duplicate customer")

    assert metrics.status == "FAILED"
    assert metrics.error_message == "Duplicate customer"