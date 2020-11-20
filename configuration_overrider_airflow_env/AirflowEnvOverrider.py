import logging

from airflow.models import Variable
from configuration_overrider.abstract_overrider import AbstractOverrider

log = logging.getLogger(__name__)


class AirflowEnvOverrider(AbstractOverrider):

    def get(self, key) -> str:
        log.info(f"[get|in] ({key})")
        result = None
        try:
            result = Variable.get(key)
        except KeyError as x:
            log.debug(f"airflow environment variable not found: {key}", exc_info=x)

        log.info(f"[get|out] => {result if result is not None else 'None'}")
        return result