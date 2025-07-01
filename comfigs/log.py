import logging.config
import comfigs.settings as settings


logging.config.dictConfig(settings.LOGGING)
logger = logging.getLogger(__name__)