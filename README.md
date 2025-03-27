# Linq DevOps Monitoring Solution

## Overview
This project demonstrates a scalable monitoring solution using Prometheus, Alertmanager, Node Exporter, and Grafana.

## Setup Instructions
1. Clone the repo:
   ```
   git clone https://github.com/yourusername/linq-monitoring.git
   cd linq-monitoring
   ```

2. Run custom exporter:
   ```
   python3 exporter/custom_metrics.py
   ```

3. Start services:
   ```
   docker-compose up -d
   ```

4. Access:
   - Prometheus: http://localhost:9090
   - Grafana: http://localhost:3000
   - Alertmanager: http://localhost:9093

## Metrics Visualized
- CPU Usage
- Memory Usage
- Disk Usage
- Custom Metrics
