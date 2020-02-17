# MicroProfile Health

## Motivation

Health checks are used to probe the state of a computing node from another machine (i.e. kubernetes service controller) with the primary target being cloud infrastructure environments where automated processes maintain the state of computing nodes.

In this scenario, _health checks are used to determine if a computing node needs to be discarded (terminated, shutdown)_ and eventually replaced by another (healthy) instance.

It’s not intended (although could be used) as a monitoring solution for human operators.

## Proposed solution

The proposed solution breaks down into two parts:

- A health check protocol and wireformat
- A Python API to implement health check procedures

## Detailed design

#### Protocol

This project defines a protocol (wireformat, semantics and possible forms of interactions) between system components that need to determine the “liveliness” of computing nodes in a bigger architecture.
A detailed description of the health check protocol can be found in the [companion document](https://github.com/eclipse/microprofile-health/tree/master/spec/src/main/asciidoc/protocol-wireformat.adoc).

#### API Usage

The main API to provide health check procedures on the application level is the `HealthCheck` interface:

```python
class Healthcheck:

    @abstractmethod
    def call(self) -> HealthcheckResponse:
        pass
```

Applications are expected to provide health check procedures (implementation of a `HealthCheck`), which will be used by the framework or runtime hosting the application to verify the healthiness of the computing node.

The runtime will `call()` the `HealthCheck` which in turn creates a `HealthCheckResponse` that signals the health status to a consuming end:

```python
@dataclass
class HealthcheckResponse:
    status: HealthcheckStatus
    checks: List[HealthcheckCheck]

    @staticmethod
    def up(checks=None):
        return HealthcheckResponse(HealthcheckStatus.UP, checks)

    @staticmethod
    def down(checks=None):
        return HealthcheckResponse(HealthcheckStatus.DOWN, checks)
```

#### Constructing `HealthCheckResponse`s

Application level code is expected to use one of static methods on `HealthCheckResponse` to retrieve a `HealthCheckResponse` object:

```python
livelinessResponse = HealthcheckResponse.up('liveliness', {'foo', 'bar'})
```

#### Integration with CDI

Within CDI contexts, beans that implement `HealthCheck` and annotated with `@Health` are discovered automatically and are invoked by the framework or runtime when the outermost protocol entry point (i.e. `http://HOST:PORT/health`) receives an inbound request.

```python
@healthcheck
class CheckDiskSpace(Healthcheck) {

    def call() -> HealtchcheckResponse:
        [...]
        
```

#### On the wire

It's the responsibility of the runtime to gather all `HealthCheckResponse` s for `HealthCheck` s known to the runtime. This means an inbound HTTP request will lead to a series of invocations
 on health check procedures and the runtime will provide a composite response, with a single overall status, i.e.:

```json
  {
    "status": "UP",
    "checks": [
      {
        "name": "first-check",
        "status": "UP",
        "data": {
          "key": "foo",
          "foo": "bar"
        }
      },
      {
          "name": "second-check",
          "status": "UP"
      }
    ]
  }
```

The link: [companion object](https://github.com/eclipse/microprofile-health/tree/master/spec/src/main/asciidoc/protocol-wireformat.adoc) contains further information on forms of interaction and the wireformat.
