import json
from collections import defaultdict
from typing import Dict, List

from demo.flask.app.main import app
from spec.health.microhealth.healthcheck import Healthcheck
from spec.health.microhealth.healthcheck_response import (
    HealthcheckSummary,
    HealthcheckResponse,
    HealthcheckStatus,
    EMPTY_HEALTHCHECK_SUMMARY_DOWN,
    EMPTY_HEALTHCHECK_SUMMARY_UP)
from spec.health.microhealth.standard_healthchecks import LivelinessHealthcheck, DiskSpaceHealthcheck

healthchecks_registry: Dict = {}
healthchecks_registry_by_type: Dict[str, List[Healthcheck]] = {}
healthchecker = Healthcheck()

healthchecks_registry['disk'] = DiskSpaceHealthcheck
healthchecks_registry['live'] = LivelinessHealthcheck
healthchecks_registry_by_type['liveliness'] = [LivelinessHealthcheck]


def get_health():
    # noinspection PyBroadException
    try:
        app.logger.debug('/health')
        healthcheck_responses = []
        for check in healthchecks_registry.values():
            healthcheck_responses.append(check().call())
        healthcheck_summary = HealthcheckSummary.call(healthcheck_responses)
        if healthcheck_summary.status == HealthcheckStatus.DOWN:
            return healthcheck_summary.to_json(), 503
        else:
            return healthcheck_summary.to_json(), 200
    except:
        app.logger.error('Failed healthcheck', exc_info=True)
        return EMPTY_HEALTHCHECK_SUMMARY_DOWN.to_json(), 500


def get_health_live():
    # noinspection PyBroadException
    try:
        app.logger.debug('/health/live')
        healthcheck_responses = []
        for check in healthchecks_registry_by_type.get('liveliness', []):
            healthcheck_responses.append(check().call())
        healthcheck_summary = HealthcheckSummary.call(healthcheck_responses)
        if healthcheck_summary.status == HealthcheckStatus.DOWN:
            return healthcheck_summary.to_json(), 503
        else:
            return healthcheck_summary.to_json(), 200
    except:
        app.logger.error('Failed healthcheck liveliness', exc_info=True)
        return EMPTY_HEALTHCHECK_SUMMARY_DOWN.to_json(), 500


def get_health_ready():
    # noinspection PyBroadException
    try:
        app.logger.debug('/health/ready')
        healthcheck_responses = []
        for check in healthchecks_registry_by_type.get('readiness', []):
            healthcheck_responses.append(check().call())
        healthcheck_summary = HealthcheckSummary.call(healthcheck_responses)
        if healthcheck_summary.status == HealthcheckStatus.DOWN:
            return healthcheck_summary.to_json(), 503
        else:
            return healthcheck_summary.to_json(), 200
    except:
        app.logger.error('Failed healthcheck ready', exc_info=True)
        return EMPTY_HEALTHCHECK_SUMMARY_DOWN.to_json(), 500
