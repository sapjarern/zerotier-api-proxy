import multiprocessing
import requests

bind = "0.0.0.0:8000"
workers = multiprocessing.cpu_count() * 2 + 1
timeout = 120
loglevel = "debug"
accesslog = "logs/guni_accesslog.log"
errorlog = "logs/guni_error.log"
# on_starting = on_starting
# worker_int = worker_int
capture_output = True
