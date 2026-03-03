import logging
from datetime import datetime
import sys
from logging.handlers import TimedRotatingFileHandler
from pathlib import Path

def setup_logger():
    """Возвращает готовый логгер"""
    logger = logging.getLogger("AITalkingAgent")
    logger.setLevel(logging.DEBUG)
    logger.propagate = False
    
    # Очищаем старые handlers
    logger.handlers.clear()
    
    # Формат
    formatter = logging.Formatter(
        "%(asctime)s [%(levelname)s] %(name)s: %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    )
    
    # Консоль
    console = logging.StreamHandler(sys.stdout)
    console.setLevel(logging.INFO)
    console.setFormatter(formatter)
    logger.addHandler(console)
    
    # Файл с ротацией (ежедневно, 30 дней)
    log_file = Path(f"logs/{datetime.now().strftime("%Y-%m-%d %H:%M:%S")}.log")
    log_file.parent.mkdir(exist_ok=True)
    
    file_handler = TimedRotatingFileHandler(
        log_file, when="midnight", interval=1, backupCount=30
    )
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)
    
    return logger

# Глобальный логгер
logger = setup_logger()
