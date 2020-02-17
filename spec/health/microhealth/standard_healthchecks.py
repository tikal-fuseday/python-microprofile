import shutil

from spec.health.microhealth.healthcheck import Healthcheck
from spec.health.microhealth.healthcheck_response import HealthcheckResponse


class LivelinessHealthcheck(Healthcheck):
    def call(self):
        return HealthcheckResponse.up('liveliness', None)


class DiskSpaceHealthcheck(Healthcheck):
    def call(self):
        total_space, used_space, free_space = shutil.disk_usage('/')
        healthy = (used_space / total_space) < 0.9
        data = {'total': total_space, 'used': used_space, 'free': free_space}
        if healthy:
            return HealthcheckResponse.up('disk_space', data)
        else:
            return HealthcheckResponse.down('disk_space', data)
