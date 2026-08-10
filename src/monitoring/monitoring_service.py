from datetime import datetime, UTC

from src.monitoring.execution_context import ExecutionContext
from src.monitoring.metrics_collector import MetricsCollector
from src.monitoring.models import PipelineExecution


class MonitoringService:
    """
    Coordinates monitoring during a pipeline execution.
    """

    def __init__(
        self,
        pipeline_name: str,
        layer: str,
    ):

        self.context = ExecutionContext(
            pipeline_name=pipeline_name,
            layer=layer,
        )

        self.metrics = MetricsCollector()

    def finish(self) -> PipelineExecution:
        """
        Build the final PipelineExecution object.
        """

        end_time = datetime.now(UTC)

        duration = (
            end_time - self.context.start_time
        ).total_seconds()

        return PipelineExecution(

            execution_id=self.context.execution_id,

            pipeline_name=self.context.pipeline_name,

            layer=self.context.layer,

            start_time=self.context.start_time,

            end_time=end_time,

            duration_seconds=duration,

            rows_read=self.metrics.rows_read,

            rows_written=self.metrics.rows_written,

            rows_rejected=self.metrics.rows_rejected,

            status=self.metrics.status,

            error_message=self.metrics.error_message,

            hostname=self.context.hostname,

            airflow_run_id=self.context.airflow_run_id,
        )