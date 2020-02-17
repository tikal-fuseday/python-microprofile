from dataclasses import dataclass
from enum import Enum
from typing import List


class HealthcheckStatus(Enum):
    UP = 'UP'
    DOWN = 'DOWN'


@dataclass()
class HealthcheckResponse:
    name: str
    status: HealthcheckStatus
    data: dict

    @staticmethod
    def up(name, data=None):
        return HealthcheckResponse(name, HealthcheckStatus.UP, data)

    @staticmethod
    def down(name, data=None):
        return HealthcheckResponse(name, HealthcheckStatus.DOWN, data)


@dataclass
class HealthcheckSummary:
    status: HealthcheckStatus
    checks: List[HealthcheckResponse]

    @staticmethod
    def call(checks: List[HealthcheckResponse] = None):
        down = any(True for check in checks if check.status != 'UP')
        if down:
            return HealthcheckSummary(HealthcheckStatus.DOWN, checks)
        else:
            return HealthcheckSummary(HealthcheckStatus.UP, checks)
