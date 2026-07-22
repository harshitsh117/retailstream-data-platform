from src.project_logging import Logger

logger = Logger.get_logger(__name__)

logger.info("Application Started")
logger.warning("This is a warning")
logger.error("Something went wrong")