import json
from typing import Dict, Iterator

from demo.flask.app.main import app
from spec.health.src.healthcheck import Healthcheck
from spec.health.src.healthcheck_response import HealthcheckSummary, HealthcheckResponse

healthchecks_registry: Dict[str, Healthcheck] = []
healthchecker = Healthcheck()


@app.route('/health')
def get_health():
    app.logger.debug('/health')
    healthcheck_responses: Iterator[HealthcheckResponse] = map(lambda x: x.call(), healthchecks_registry.values())
    healthcheck_summary = HealthcheckSummary.call(healthcheck_responses)
    return json.dumps(healthcheck_summary)
