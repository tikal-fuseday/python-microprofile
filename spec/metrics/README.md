# Python-Microprofile

Inspired by [Eclipse Microprofile Metrics](https://github.com/eclipse/microprofile-metrics) we want to develop the metrics portion of microprofiling for languages other than Java.
This POC will focus on microprofile-metrics for webservices.

The metrics will be stored in a local registry and will be exposed to the monitoring server via /metrics route.

## Metrics Setup
Metrics that are exposed need to be configured in the server. On top of the pure metrics, metadata needs to be provided.

The following three sets of sub-resource (scopes) are exposed.

base: metrics that all MicroProfile vendors have to provide, these metrics will be exposed under `/metrics/base`

vendor: vendor specific metrics (optional), these metrics will be exposed under `/metrics/vendor`

application: application-specific metrics (optional), these metrics will be exposed under `/metrics/application`

## Base Metrics
Microprofile divides base-metrics into two categories: [required](https://github.com/eclipse/microprofile-metrics/blob/master/spec/src/main/asciidoc/required-metrics.adoc#required-metrics) and [optional](https://github.com/eclipse/microprofile-metrics/blob/master/spec/src/main/asciidoc/required-metrics.adoc#thread-pool-stats).
As you can see, many of these metrics are Java specific and deal with the JVM. In this POC we will treat all these metrics as optional and instead, try to come up with a broader, more generic set of base-metrics.

### CPU Utilization
* CPU usage in percentage
and breakdown by:
* (optional) processes executing in user mode (percentage)
* (optional) processes executing in kernel mode (percentage)

### Memory
Two metrics will be published:
* total memory (bytes)
* used memory (bytes)

### Disk
Two metrics will be published:
* disk space total (bytes)
* disk space used (bytes)

### Network
* packets transmitted, received (count)
* bytes transmitted, received (bytes)
* (optional) packets dropped by the driver on transmit, receive (count)
* (optional) total number of sockets in kernel socket lists (count);
* (optional) TCP sockets currently in use (count);
* (optional) UDP sockets currently in use (count)

## Vendor Metrics (Optional)
// TODO

## Application Metrics (Optional) 
// TODO

## Metrics Tags
We want to be able to standartize metric-names, meaning, for an outbound HTTP call we'll want to publish a metric called: 
`outbound_http_latency_seconds`. The way to differentiate between different outbound calls will be by tags (labels).

Tags are also useful to expose: app-name, instance-id, cluster-name, service-name, region/zone and etc.

Example:  `outbound_http_latency_seconds{region="eu-west-1",path="/foo"}`