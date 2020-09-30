import logging

logger = logging.getLogger(__name__)


class SpecialFilter(logging.Filter):
    def filter(self, record: logging.LogRecord):
        return True
