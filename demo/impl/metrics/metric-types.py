from enum import Enum


class MetricTypes(Enum):
    # A concurrent gauge counts the number of parallel invocations of
    # a target (method). Upon entering the target the value is increased.
    # It is decreased again upon exiting the target.
    CONCURRENT_GAUGE = 'concurrent gauge'

    # A Counter monotonically increases its values.
    # An example could be the number of Transactions committed.
    COUNTER = 'counter'

    # A Gauge has values that 'arbitrarily' goes up/down at each
    # sampling. An example could be CPU load
    GAUGE = 'gauge'

    # A Meter measures the rate at which a set of events occur.
    # An example could be amount of Transactions per Hour.
    METERED = 'meter'

    # A Histogram calculates the distribution of a value.
    HISTOGRAM = 'histogram'

    # A timer aggregates timing durations and provides duration
    # statistics, plus throughput statistics
    TIMER = 'timer'

    # A simple timer aggregates timing durations
    SIMPLE_TIMER = 'simple timer'

    # Invalid - Placeholder
    INVALID = 'invalid'

    @staticmethod
    def metric_from(string):
        for t in MetricTypes:
            if t.value == string:
                return t
        return MetricTypes.INVALID

# assert(MetricTypes.CONCURRENT_GAUGE == MetricTypes.metric_from('concurrent gauge'))
