import logging
import os
from fastapi import APIRouter, FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes.item_router import router as item_router

os.makedirs("/var/log/api", exist_ok=True)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler("/api:/var/log/api:ro"), # var/log/api/fastapi.log"),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger(__name__)
logger.info("FastAPI application started.")

app = FastAPI()

api_router = APIRouter(prefix="/api")


@api_router.get("/")
def root():
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
