from spec.health.src.healthcheck_response import HealthcheckResponse

LIVELINESS_HEALTHCHECKS = HealthcheckResponse.up('liveliness', None)
