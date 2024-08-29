import logging
import os

log_directory = os.path.join(os.path.dirname(os.path.dirname(__file__)), "logs")
os.makedirs(log_directory, exist_ok=True)

# Полный путь к файлу логов
log_file_path = os.path.join(log_directory, "project.log")

# Настройка логирования
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[logging.FileHandler(log_file_path, mode="w"), logging.StreamHandler()],  # Также выводим логи в консоль
)

# Создание логгера, который можно использовать в других модулях
logger = logging.getLogger("widget_1")
