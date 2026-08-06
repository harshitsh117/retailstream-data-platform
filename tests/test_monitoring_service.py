from src.monitoring.monitoring_service import MonitoringService
from src.monitoring.enums import PipelineStatus


def test_monitoring_service():

    service = MonitoringService(
        pipeline_name="Bronze",
        layer="bronze",
    )

    service.metrics.rows_read = 100

    service.metrics.rows_written = 98

    service.metrics.mark_success()

    execution = service.finish()

    assert execution.pipeline_name == "Bronze"

    assert execution.layer == "bronze"

    assert execution.rows_read == 100

    assert execution.rows_written == 98

    assert execution.status == PipelineStatus.SUCCESS

    assert execution.duration_seconds >= 0