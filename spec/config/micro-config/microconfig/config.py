from abc import ABC, abstractmethod


class ConfigSource(ABC):

    def __init__(self, ordinal):
        self.values = {}
        self.ordinal = ordinal

    @abstractmethod
    def load(self, *args, **kwargs):
        pass

    def get(self, key):
        return self.values.get(key)

    def get_ordinal(self):
        return self.ordinal


class EnvConfigSource(ConfigSource):

    def __init__(self):
        super().__init__(500)

    def load(self, *args, **kwargs):
        import os
        self.values = os.environ.copy()


class PropertiesConfigSource(ConfigSource):

    separator = '='

    def __init__(self, filename):
        super().__init__(400)
        self.filename = filename

    def load(self, *args, **kwargs):
        with open(self.filename) as f:

            for line in f:
                if PropertiesConfigSource.separator in line:
                    # Find the name and value by splitting the string
                    name, value = line.split(PropertiesConfigSource.separator, 1)

                    # Assign key value pair to dict
                    # strip() removes white space from the ends of strings
                    self.values[name.strip()] = value.strip()


class Configuration:

    def __init__(self, *args):
        self.configs = []
        env_config = EnvConfigSource()
        local_configs = {
            env_config.get_ordinal(): env_config
        }

        for _config in args:
            if isinstance(_config, ConfigSource):
                local_configs[_config.get_ordinal()] = _config

        for key in sorted(local_configs.keys(), reverse=True):
            _config = local_configs[key]
            _config.load()
            self.configs.append(_config)

    def get(self, key):
        for _config in self.configs:
            value = _config.get(key)
            if value is not None:
                return value
        return None

    def __getitem__(self, item):
        return self.get(item)


if __name__ == '__main__':
    prop_config = PropertiesConfigSource("conf.properties")
    config = Configuration(prop_config)
    print(config.get('com.tikalk.key1'))
    print(config['PATH'])
