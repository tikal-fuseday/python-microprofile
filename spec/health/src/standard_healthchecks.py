import shutil

from spec.health.src.healthcheck_response import HealthcheckResponse

LIVELINESS_HEALTHCHECKS = HealthcheckResponse.up('liveliness', None)


def diskspace_healthcheck():
    total_space, used_space, free_space = shutil.disk_usage('/')
    healthy = (used_space / total_space) < 0.9
    data = {'total': total_space, 'used': used_space, 'free': free_space}
    if healthy:
        return HealthcheckResponse.up('disk_space', data)
    else:
        return HealthcheckResponse.down('disk_space', data)
