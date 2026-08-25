
import logging
from datetime import datetime
from flask import request

logging.basicConfig(
    filename = 'app.log',
    # level = logging.INFO,
    level = logging.DEBUG,
    format = '%(asctime)s - %(levelname)s - %(message)s',
)

def log_request():
   
    logging.info(f"Method: {request.method} PATH: {request.path} ")    # Logging Method and Path to app.log

def log_error(message):

    logging.error(f"Error: {message}")

def log_info(message):
    
    logging.info(f"Info: {message}")

