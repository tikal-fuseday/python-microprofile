# Microprofile - Config

Configuration is an essential part of Microprofile implementation.
## Specifications
The full spec can be found here: [1.4 Spec](https://download.eclipse.org/microprofile/microprofile-config-1.4/microprofile-config-spec.pdf).

Out of the full spec, we are implementing the basics:
* **ConfigSource** abstract class which reads configuration from a single source.
* Each source is defining its ordinal.
* Main configuration that serves values from all sources according to the ordinal. Values from higher ordinal overwrites lower ordinal configuration source.
* Out of the box the default sources includes:
    * Command line arguments (default ordinal=400)
    * Environment variables (default ordinal=300)
    * Properties file (default ordinal=100)

## Usage
### Installation
`pip install microconfig-0.0.1.tar.gz`

### Usage
In order to use the default config sources:
```python
from microconfig.config import Configuration

conf = Configuration()
val1 = conf.get("key1")
val2 = conf["key2"]
```

To use properties file config source:

```python
from microconfig.config import Configuration, PropertiesConfigSource

prop_conf = PropertiesConfigSource("conf.properties")
conf = Configuration(prop_conf)
val1 = conf.get("com.tikal.key1") # From properties file 
val2 = conf.get("PATH") # From environment variable
```