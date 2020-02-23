# python-microprofile

## open trace

## Introduction (from microprofile-opentracing-spec-1.3.3)
Distributed tracing allows you to trace the flow of a request across service boundaries.
This specification specifically addresses the problem of making it easy to instrument services with distributed tracing function, given an existing distributed tracing system in the environment.
This specification specifically does not address the problem of defining, implementing, or configuring the underlying distributed tracing system. The proposal assumes an environment where all services use a common OpenTracing implementation (all Zipkin compatible, all Jaeger compatible, ...).

## Rationale (from microprofile-opentracing-spec-1.3.3)
In order for a distributed tracing system to be effective and usable, two things are required
1. The different services in the environment must agree on the mechanism for transferring correlation ids across services.
2. The different services in the environment should produce their trace records in format that is consumable by the storage service for distributed trace records.
Without the first, some services will not be included in the trace records associated with a request. Without the second, custom code would need to be written to present the information about a full request flow.


There are existing distributed tracing systems that provide a server for distributed trace record storage and viewing, and application libraries for instrumenting microservices. The problem is that the different distributed tracing systems use implementation specific mechanisms for propagating correlation IDs and for formatting trace records, so once a microservice chooses a distributed tracing implementation library to use for its instrumentation, all other microservices in the environment are locked into the same choice.


https://github.com/eclipse/microprofile-opentracing/releases

## The Challenge
Use the opentrace standard (including python library) and integrate in python with the microprofile standard and annotations
Currently microprofile only supports opentracing, what opentracing will be merging with opencensus to add metrics as well.

https://opentracing.io/specification/

## Implementation
The implementation will based on  https://github.com/opentracing/opentracing-python

The following library has been found: opentracing-utils

* No extrenal dependencies, only ![opentracing-python](https://github.com/zalando-zmon/opentracing-utils).
* No threadlocals. Either pass spans explicitly or fallback to callstack frames inspection!
* Context agnostic, so no external context implementation dependency (no Tornado, Flask, Django etc …).
* Try to be less verbose - just add the @trace decorator.
* Could be more verbose when needed, without complexity - just accept **kwargs and get the span passed to your traced functions via @trace(pass_span=True).
* Support asyncio/async-await coroutines. (drop support for py2.7)
* Support gevent
* Ability to add OpenTracing support to external libs/frameworks/clients:
        Django (via OpenTracingHttpMiddleware)
        Flask (via trace_flask())
        Requests (via trace_requests())
        SQLAlchemy (via trace_sqlalchemy())
        
## API Examples
```python
# Normal traced function
@trace()
def trace_me():
    pass

# Traced function with access to created span in ``kwargs``
@trace(operation_name='user.operation', pass_span=True)
def user_operation(user, op, **kwargs):
    current_span = extract_span_from_kwargs(**kwargs)

    current_span.set_tag('user.id', user.id)

    # Then do stuff ...

    # trace_me will have ``current_span`` as its parent.
    trace_me()

# Traced function using ``follows_from`` instead of ``child_of`` reference.
@trace(use_follows_from=True)
def trace_me_later():
    pass


# Start a fresh trace - any parent spans will be ignored
@trace(operation_name='epoch', ignore_parent_span=True)
def start_fresh():

    user = {'id': 1}

    # trace decorator will handle trace heirarchy
    user_operation(user, 'create')

    # trace_me will have ``epoch`` span as its parent.
    trace_me()

```
