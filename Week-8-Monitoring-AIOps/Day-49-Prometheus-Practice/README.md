**Day 49 – Prometheus Learning and Practical Practice**

**Objective**

Install Prometheus using Docker and explore its dashboard, target health, and metrics using PromQL queries.

**Topics Covered**

- Prometheus installation using Docker
- Prometheus web interface
- Target health monitoring
- PromQL basics
- Metrics collection
- Process memory monitoring

**Practical Implementation**

- Downloaded the `prom/prometheus` Docker image.
- Created and started a Prometheus container.
- Accessed the dashboard at `http://localhost:9090`.
- Opened Status → Target health.
- Verified that the Prometheus target was UP.

**Docker Command**

```bash
docker run -d --name prometheus -p 9090:9090 prom/prometheus
```

**PromQL Queries Practiced**

1. `up`
   - Result: 1
   - Verified that the Prometheus target was healthy.

2. `prometheus_build_info`
   - Result: 1
   - Observed Prometheus version 3.16.0.

3. `count({__name__=~".+"})`
   - Result: 692
   - Counted matching metric time series.

4. `process_resident_memory_bytes`
   - Result: 107143168 bytes
   - Observed Prometheus process memory usage (approximately 102.1 MiB).

**Key Learnings**

- Prometheus collects and stores metrics as time-series data.
- Target health indicates whether a configured target is being scraped successfully.
- PromQL is used to query Prometheus metrics.
- The `up` metric helps monitor target availability.
- Process metrics provide information about Prometheus resource usage.

**Outcome**

Successfully ran Prometheus using Docker, verified target health, and practiced querying metrics using PromQL.
