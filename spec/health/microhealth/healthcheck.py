from abc import abstractmethod

from spec.health.microhealth.healthcheck_response import HealthcheckResponse


class Healthcheck:

    @abstractmethod
    def call(self) -> HealthcheckResponse:
        pass
