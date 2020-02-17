from abc import abstractmethod

from spec.health.src.healthcheck_response import HealthcheckResponse


class Healthcheck:

    @abstractmethod
    def call(self) -> HealthcheckResponse:
        pass
