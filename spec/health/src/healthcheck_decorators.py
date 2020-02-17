import functools
import logging

from spec.health.src.healthcheck_response import HealthcheckResponse



def healthcheck(func):
    @functools.wraps(func)
    def wrapper_healthcheck_check(*args, **kwargs) -> HealthcheckResponse:
        logging.debug('Running healthcheck check')
        res = func(*args, **kwargs)
        if res.status == 'UP':
            logging.debug(f'Healthcheck check {res.name} is UP')
        else:
            logging.warning(f'Healthcheck check {res.name} is DOWN')
        return res

    return wrapper_healthcheck_check

