from enum import Enum


class MetricUnits(Enum):
    NONE = "none"

    BITS = "bits"

    KILOBITS = "kilobits"

    MEGABITS = "megabits"

    GIGABITS = "gigabits"

    KIBIBITS = "kibibits"

    MEBIBITS = "mebibits"

    GIBIBITS = "gibibits"

    BYTES = "bytes"

    KILOBYTES = "kilobytes"

    MEGABYTES = "megabytes"

    GIGABYTES = "gigabytes"

    NANOSECONDS = "nanoseconds"

    MICROSECONDS = "microseconds"

    MILLISECONDS = "milliseconds"

    SECONDS = "seconds"

    MINUTES = "minutes"

    HOURS = "hours"

    DAYS = "days"

    PERCENT = "percent"

    PER_SECOND = "per_second"

    @staticmethod
    def unit_from(string):
        for t in MetricUnits:
            if t.value == string:
                return t
        return MetricUnits.NONE
