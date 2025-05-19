import logging.config
import settings


logging.config.dictConfig(settings.LOGGING)
logger = logging.getLogger(__name__)