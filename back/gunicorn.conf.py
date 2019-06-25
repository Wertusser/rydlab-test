import multiprocessing
import os

port = os.environ.get('PORT', '8080')
workers = int(os.environ.get('HTTP_WORKERS', multiprocessing.cpu_count()))
debug = os.environ.get('DEBUG', False)
timeout = os.environ.get("TIMEOUT", 90)
