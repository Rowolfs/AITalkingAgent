import os
import yaml
from dotenv import load_dotenv

with open("../config.yaml","r",encoding="utf-8") as f:
    config = yaml.safe_load(f)


try:
    secret_path = os.environ.get("BOT_TOKEN_FILE","/run/secrets.env")
    with open(secret_path, "r") as f:
        token = f.read().strip()[6:]
    print("Token loaded:", token[:4]+ "...")
    
except FileNotFoundError:
    load_dotenv()
    token = os.getenv("TOKEN")
    print("Token loaded:", token[:4]+ "...")
