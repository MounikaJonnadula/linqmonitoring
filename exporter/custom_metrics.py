from prometheus_client import start_http_server, Gauge
import random
import time

cpu_temp = Gauge('custom_cpu_temperature_celsius', 'Simulated CPU temperature')
error_rate = Gauge('custom_error_rate', 'Simulated Error Rate')

def generate_metrics():
    while True:
        cpu_temp.set(random.uniform(60, 90))
        error_rate.set(random.random())
        time.sleep(5)

if __name__ == '__main__':
    start_http_server(5000)
    generate_metrics()
