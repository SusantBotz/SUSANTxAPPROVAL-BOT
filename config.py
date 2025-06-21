import os
from typing import List

API_ID = os.environ.get("API_ID", "21134445")
API_HASH = os.environ.get("API_HASH", "231c18ea7273824491d6bf05425ab74e")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
ADMIN = int(os.environ.get("ADMIN", "8156708830"))

LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1002758342066"))
NEW_REQ_MODE = os.environ.get("NEW_REQ_MODE", "True").lower() == "true"  # Set "True" For accept new requests

DB_URI = os.environ.get("DB_URI", "mongodb+srv://susantxbotz:vGmf4pFy1MEijuZF@cluster0.viyjnvi.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
DB_NAME = os.environ.get("DB_NAME", "susant-botz")

IS_FSUB = os.environ.get("IS_FSUB", "True").lower() == "true"  # Set "True" For Enable Force Subscribe
AUTH_CHANNELS = list(map(int, os.environ.get("AUTH_CHANNEL", "-1002618578974 -1002131408527").split())) # Add Multiple channel ids
