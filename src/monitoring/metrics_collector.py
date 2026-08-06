from dataclasses import dataclass
from typing import Optional
from src.monitoring.enums import PipelineStatus


@dataclass
class MetricsCollector:
    """
    Collects runtime metrics for a pipeline execution.
    """

    rows_read: int = 0

    rows_written: int = 0

    rows_rejected: int = 0

    status: PipelineStatus = PipelineStatus.RUNNING
    # status: str = "RUNNING"

    error_message: Optional[str] = None

    def mark_success(self) -> None:
        """
        Mark pipeline execution as successful.
        """
        self.status = PipelineStatus.SUCCESS

    def mark_failure(self, error: str) -> None:
        """
        Mark pipeline execution as failed.
        """
        self.status = PipelineStatus.FAILED
        self.error_message = error