import logging

from opentelemetry import logs
from opentelemetry.sdk.logs import LoggerProvider, LoggingHandler
from opentelemetry.sdk.logs.export import OTLPLogExporter, BatchLogRecordProcessor
from opentelemetry.sdk.resources import Resource

resource = Resource(attributes={"service.name": "fastapi-backend"})

logs.set_logger_provider(LoggerProvider(resource=resource))
logger_provider = logs.get_logger_provider()

exporter = OTLPLogExporter(
    endpoint="http://otel-collector-service.lunchbox.svc.cluster.local:4317",
    insecure=True,
)

logger_provider.add_log_record_processor(BatchLogRecordProcessor(exporter))
otel_handler = LoggingHandler(level=logging.INFO, logger_provider=logger_provider)
logging.getLogger().addHandler(otel_handler)
logging.getLogger().setLevel(logging.INFO)

from fastapi import APIRouter, FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes.item_router import router as item_router

app = FastAPI()
api_router = APIRouter(prefix="/api")


@api_router.get("/")
def root():
    logging.getLogger(__name__).info("Hit root endpoint")
    return {"message": "Hello from Azure!"}


@api_router.get("/health")
def health_check():
    logging.getLogger(__name__).info("Health check pinged")
    return {"status": "Healthy"}


api_router.include_router(item_router)
app.include_router(api_router)

# CORS
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
