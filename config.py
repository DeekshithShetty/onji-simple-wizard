import os

DEBUG = os.getenv("ENVIRONMENT") == "DEV"
APPLICATION_ROOT = os.getenv("APPLICATION_ROOT", "/")
HOST = os.getenv("APPLICATION_HOST", "0.0.0.0")
PORT = int(os.getenv("PORT", "5000"))
