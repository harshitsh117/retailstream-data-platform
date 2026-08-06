from enum import Enum


class PipelineStatus(str, Enum):
    """
    Pipeline execution status.
    """

    RUNNING = "RUNNING"
    SUCCESS = "SUCCESS"
    FAILED = "FAILED"