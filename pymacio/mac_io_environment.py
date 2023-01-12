import logging
import os
from dotenv import load_dotenv

MACIO_API_KEY_ENV = "MACIO_API_KEY"
MACIO_API_URL_ENV = "MACIO_API_URL"

logger = logging.getLogger(__name__)


class MacIoEnvironment:
    def __init__(self, api_key=None, api_url=None):
        if not load_dotenv():
            logger.warning("Error loading .env file")

        if not api_key:
            api_key = os.getenv(MACIO_API_KEY_ENV, None)
        if not api_url:
            api_url = os.getenv(MACIO_API_URL_ENV, None)

        self.output_format = "json"
        self.api_key = api_key
        self.api_url = api_url
        logger.debug(f"Loaded environment information: API Key: {self.api_key}, API Url: {self.api_url}")
