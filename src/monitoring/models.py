from dataclasses import dataclass, field
from datetime import datetime
from typing import Optional
import socket
import uuid
from src.monitoring.enums import PipelineStatus


@dataclass
class PipelineExecution:
    """
    Represents a single pipeline execution.
    """

    execution_id: str = field(default_factory=lambda: str(uuid.uuid4()))

    pipeline_name: str = ""
    layer: str = ""

    start_time: datetime = field(default_factory=datetime.utcnow)
    end_time: Optional[datetime] = None

    duration_seconds: Optional[float] = None

    rows_read: int = 0
    rows_written: int = 0
    rows_rejected: int = 0

    status: PipelineStatus = PipelineStatus.RUNNING
    # status: str = "RUNNING"

    error_message: Optional[str] = None

    hostname: str = field(default_factory=socket.gethostname)

    airflow_run_id: Optional[str] = None

    created_at: datetime = field(default_factory=datetime.utcnow)