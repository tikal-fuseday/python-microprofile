import json
from typing import Dict, List

from demo.flask.app.main import app
from spec.health.microhealth.healthcheck import Healthcheck
from spec.health.microhealth.healthcheck_response import (
    HealthcheckSummary,
    HealthcheckResponse,
    HealthcheckStatus,
    EMPTY_HEALTHCHECK_SUMMARY_DOWN,
    EMPTY_HEALTHCHECK_SUMMARY_UP)

healthchecks_registry: Dict[str, Healthcheck] = []
healthchecks_registry_by_type: Dict[str, List[Healthcheck]] = []
healthchecker = Healthcheck()


@app.route('/health')
def get_health():
    # noinspection PyBroadException
    try:
        app.logger.debug('/health')
        healthcheck_responses: List[HealthcheckResponse] = list(map(lambda x: x.call(), healthchecks_registry.values()))
        healthcheck_summary = HealthcheckSummary.call(healthcheck_responses)
        if healthcheck_summary.status == HealthcheckStatus.DOWN:
            return json.dumps(healthcheck_summary), 503
        else:
            return json.dumps(healthcheck_summary), 200
    except:
        app.logger.error('Failed healthcheck', exc_info=True)
        return json.dumps(EMPTY_HEALTHCHECK_SUMMARY_DOWN), 500


@app.route('/health/live')
def get_health_live():
    # noinspection PyBroadException
    try:
        app.logger.debug('/health/live')
        healthcheck_responses: List[HealthcheckResponse] = list(
            map(lambda x: x.call(), healthchecks_registry_by_type['liveliness']))
        healthcheck_summary = HealthcheckSummary.call(healthcheck_responses)
        if healthcheck_summary.status == HealthcheckStatus.DOWN:
            return json.dumps(healthcheck_summary), 503
        else:
            return json.dumps(healthcheck_summary), 200
    except:
        app.logger.error('Failed healthcheck liveliness', exc_info=True)
        return json.dumps(EMPTY_HEALTHCHECK_SUMMARY_DOWN), 500


@app.route('/health/ready')
def get_health_ready():
    # noinspection PyBroadException
    try:
        app.logger.debug('/health/ready')
        healthcheck_responses: List[HealthcheckResponse] = list(
            map(lambda x: x.call(), healthchecks_registry_by_type['readiness']))
        healthcheck_summary = HealthcheckSummary.call(healthcheck_responses)
        if healthcheck_summary.status == HealthcheckStatus.DOWN:
            return json.dumps(healthcheck_summary), 503
        else:
            return json.dumps(healthcheck_summary), 200
    except:
        app.logger.error('Failed healthcheck ready', exc_info=True)
        return json.dumps(EMPTY_HEALTHCHECK_SUMMARY_DOWN), 500
