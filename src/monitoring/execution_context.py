from dataclasses import dataclass, field
from datetime import datetime, UTC
from typing import Optional
import socket
import uuid


@dataclass
class ExecutionContext:
    """
    Stores metadata about a pipeline execution.
    """

    execution_id: str = field(
        default_factory=lambda: str(uuid.uuid4())
    )

    pipeline_name: str = ""

    layer: str = ""

    hostname: str = field(
        default_factory=socket.gethostname
    )

    start_time: datetime = field(
        default_factory=lambda: datetime.now(UTC)
    )

    airflow_run_id: Optional[str] = None