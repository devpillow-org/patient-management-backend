import multiprocessing
import sys

bind = "0.0.0.0:8000"
workers = multiprocessing.cpu_count() * 2 + 1
worker_class = "uvicorn_worker.UvicornWorker"
pythonpath = sys.executable
