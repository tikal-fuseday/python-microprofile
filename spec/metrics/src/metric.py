import abc
import six


@six.add_metaclass(abc.ABCMeta)
class Metric:
    def __init__(self, name, unit, metric_type, desc='', display_name='', reusable=False):
        self.name = name
        self.unit = unit
        self.type = metric_type
        self.desc = desc
        self.display_name = display_name
        self.reusable = reusable
