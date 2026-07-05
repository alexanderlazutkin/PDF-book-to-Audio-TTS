import os
from dotenv import load_dotenv

# Подгрузим .env
load_dotenv()

# === Бэкенд LLM ===
# "lmstudio" — локальная LMStudio (OpenAI-совместимый API, по умолчанию)
# "ollama"   — локальная Ollama
# "openai"   — облачный OpenAI API
LLM_BACKEND = os.getenv("LLM_BACKEND", "lmstudio").strip().lower()

# === LMStudio (локальная модель) ===
# OpenAI-совместимый эндпоинт LMStudio (вкладка Developer → Start Server).
LMSTUDIO_BASE_URL = os.getenv("LMSTUDIO_BASE_URL", "http://localhost:1234/v1")
# Идентификатор модели, как он показан в LMStudio. LMStudio принимает
# произвольное имя загруженной модели, но точнее указать то, что выдаёт
# GET /v1/models в LMStudio.
LMSTUDIO_MODEL = os.getenv("LMSTUDIO_MODEL", "qwen3.6-35b-a3b-mtp")
LMSTUDIO_API_KEY = os.getenv("LMSTUDIO_API_KEY", "lm-studio")

# === Ollama (локальная модель) ===
OLLAMA_BASE_URL = os.getenv("OLLAMA_BASE_URL", "http://localhost:11434/v1")
OLLAMA_MODEL = os.getenv("OLLAMA_MODEL", "llama3.1:8b")
OLLAMA_API_KEY = os.getenv("OLLAMA_API_KEY", "ollama")

# === OpenAI (облако) ===
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")
OPENAI_MODEL = os.getenv("OPENAI_MODEL", "gpt-5-nano")

# === Общие настройки LLM ===
LLM_TEMPERATURE = float(os.getenv("LLM_TEMPERATURE", "0"))
LLM_TIMEOUT = int(os.getenv("LLM_TIMEOUT", "600"))
MAX_CONTENT_TOKENS = int(os.getenv("MAX_CONTENT_TOKENS", "9500"))

# === Пути ===
BOOK_PATH = os.getenv("BOOK_PATH", "./data/book.txt")
OUT_DIR = os.getenv("OUT_DIR", "./out")

# === Настройки для SpeechKit ===
SPEECHKIT_CHUNK_SIZE = 200


def get_llm_config() -> dict:
    """
    Возвращает конфигурацию LLM в зависимости от выбранного бэкенда.

    Возвращает словарь:
      - base_url: str
      - api_key:  str
      - model:    str
    """
    if LLM_BACKEND == "lmstudio":
        return {
            "base_url": LMSTUDIO_BASE_URL,
            "api_key": LMSTUDIO_API_KEY,
            "model": LMSTUDIO_MODEL,
        }
    if LLM_BACKEND == "ollama":
        return {
            "base_url": OLLAMA_BASE_URL,
            "api_key": OLLAMA_API_KEY,
            "model": OLLAMA_MODEL,
        }
    # OpenAI по умолчанию
    return {
        "base_url": None,
        "api_key": OPENAI_API_KEY,
        "model": OPENAI_MODEL,
    }
