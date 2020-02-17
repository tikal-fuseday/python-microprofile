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

### Base Metrics
Microprofile divides base-metrics into two categories: [required](https://github.com/eclipse/microprofile-metrics/blob/master/spec/src/main/asciidoc/required-metrics.adoc#required-metrics) and [optional](https://github.com/eclipse/microprofile-metrics/blob/master/spec/src/main/asciidoc/required-metrics.adoc#thread-pool-stats).
As you can see, many of these metrics are Java specific and deal with the JVM. In this POC we will treat all these metrics as optional.

### Vendor Metrics (Optional)
// TODO

### Application Metrics (Optional) 
// TODO