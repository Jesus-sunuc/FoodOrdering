import json
import logging
import os
from fastapi import APIRouter, FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes.item_router import router as item_router

os.makedirs("/var/log/api", exist_ok=True)

class JsonFormatter(logging.Formatter):
    def format(self, record):
        log_record = {
            "time": self.formatTime(record, self.datefmt),
            "level": record.levelname,
            "message": record.getMessage(),
            "logger": record.name,
        }
        return json.dumps(log_record)

json_formatter = JsonFormatter()

file_handler = logging.FileHandler("/var/log/api/fastapi.log")
file_handler.setFormatter(json_formatter)

stream_handler = logging.StreamHandler()
stream_handler.setFormatter(json_formatter)

logging.basicConfig(
    level=logging.INFO,
    handlers=[file_handler, stream_handler]
)

logger = logging.getLogger(__name__)
logger.info("FastAPI application started.")

app = FastAPI()

api_router = APIRouter(prefix="/api")

@api_router.get("/")
def root():
    logger.info("Root endpoint hit")
    return {"message": "Hello from Azure!"}

@api_router.get("/health")
def health_check():
    logger.info("Health check endpoint hit")
    return {"status": "Healthy"}



api_router.include_router(item_router)

app.include_router(api_router)

origins = [
    "http://localhost:4173",
    "http://lunchbox6.duckdns.org",
    "http://localhost:5173",
    "https://yellow-island-0e74ba610.6.azurestaticapps.net",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
