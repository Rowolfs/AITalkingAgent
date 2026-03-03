import os
import sys
import yaml
from logger import logger
from dotenv import load_dotenv

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CONFIG_PATH = os.path.join(BASE_DIR, "..", "config.yaml")

config = ""
try:
    with open(CONFIG_PATH,"r",encoding="utf-8") as f:
        config = yaml.safe_load(f)
except FileNotFoundError:
    logger.error("Config file not found")
    sys.exit(1)


try:
    secret_path = os.environ.get("BOT_TOKEN_FILE","/run/secrets.env")
    with open(secret_path, "r") as f:
        token = f.read().strip()[6:]
    print("Token loaded:", token[:4]+ "...")
    
except FileNotFoundError:
    load_dotenv()
    token = os.getenv("TOKEN")
    print("Token loaded:", token[:4]+ "...")
    
