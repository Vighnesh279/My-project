# EXP-09: System Monitoring Using Prometheus and Grafana

## Aim

To monitor system performance and service health using Prometheus, Node Exporter, and Grafana.

## Tools Used

- Ubuntu Linux
- Docker
- Prometheus
- Node Exporter
- Grafana

## Implementation

1. Started Node Exporter in Docker to collect system metrics.
2. Configured Prometheus to scrape Node Exporter metrics.
3. Verified the Node Exporter target in Prometheus.
4. Queried CPU utilization, available memory, and filesystem metrics using PromQL.
5. Connected Grafana to Prometheus as a data source.
6. Created a Grafana dashboard for system monitoring.
7. Configured a high-CPU alert rule with an 80% threshold.

## Access URLs

- Prometheus: `http://localhost:9090`
- Prometheus Targets: `http://localhost:9090/targets`
- Grafana: `http://localhost:3000`
- Node Exporter metrics: `http://localhost:9100/metrics`

## PromQL Queries

### CPU Utilization

```promql
100 * (1 - avg by (instance) (rate(node_cpu_seconds_total{mode="idle"}[5m])))
```

### Available Memory

```promql
node_memory_MemAvailable_bytes
```

### Root Filesystem Size

```promql
node_filesystem_size_bytes{mountpoint="/"}
```

## Alert Configuration

- Alert name: `EXP09-High-CPU-Usage`
- Condition: CPU utilization above 80%
- Pending period: 1 minute

## Evidence

The `Submission` folder contains the screenshot collection PDF documenting the monitoring experiment.

## Result

Prometheus successfully collected Node Exporter metrics, and Grafana was connected to Prometheus for visualization. CPU, memory, and filesystem metrics were queried, and a high-CPU alert rule was configured.

The `prometheus.yml` file in this repository documents the experiment configuration.
