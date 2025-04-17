import logging

from fastapi import APIRouter, FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes.item_router import router as item_router

from opentelemetry.sdk.resources import Resource
from opentelemetry.sdk._logs import LoggerProvider, LoggingHandler
from opentelemetry.sdk._logs.export import BatchLogRecordProcessor
from opentelemetry.exporter.otlp.proto.grpc._log_exporter import OTLPLogExporter

from opentelemetry.instrumentation.fastapi import FastAPIInstrumentor
from opentelemetry.instrumentation.requests import RequestsInstrumentor

from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor
from opentelemetry.exporter.otlp.proto.grpc.trace_exporter import OTLPSpanExporter

from opentelemetry.sdk.metrics import MeterProvider
from opentelemetry.sdk.metrics.export import PeriodicExportingMetricReader
from opentelemetry.exporter.otlp.proto.grpc.metric_exporter import OTLPMetricExporter

from opentelemetry import trace, metrics

resource = Resource(attributes={"service.name": "fastapi-backend"})
meter = metrics.get_meter("fastapi-meter")

request_counter = meter.create_counter(
    name="fastapi_requests_total",
    description="Total number of FastAPI requests",
    unit="1",
)

# --- Tracing ---
# trace.set_tracer_provider(TracerProvider(resource=resource))
# tracer_provider = trace.get_tracer_provider()
# tracer_exporter = OTLPSpanExporter(endpoint="http://otel-collector:4317", insecure=True)
# tracer_provider.add_span_processor(BatchSpanProcessor(tracer_exporter))
trace.set_tracer_provider(TracerProvider(resource=resource))
tracer_provider = trace.get_tracer_provider()
tracer_provider.add_span_processor(
    BatchSpanProcessor(
        OTLPSpanExporter(
            endpoint="http://otel-collector-service:4317",
            insecure=True,
        )
    )
)

# --- Metrics ---
metric_exporter = OTLPMetricExporter(
    endpoint="http://otel-collector-service:4317", insecure=True
)
metric_reader = PeriodicExportingMetricReader(metric_exporter)

metrics.set_meter_provider(
    MeterProvider(resource=resource, metric_readers=[metric_reader])
)

# --- Logging ---
log_exporter = OTLPLogExporter(
    endpoint="http://otel-collector-service:4317",
    insecure=True,
)

log_provider = LoggerProvider(resource=resource)
log_provider.add_log_record_processor(BatchLogRecordProcessor(log_exporter))

otel_handler = LoggingHandler(level=logging.INFO, logger_provider=log_provider)
logging.getLogger().addHandler(otel_handler)
logging.getLogger().setLevel(logging.INFO)

# --- FastAPI App ---
app = FastAPI()
FastAPIInstrumentor.instrument_app(app)
RequestsInstrumentor().instrument()

api_router = APIRouter(prefix="/api")


@api_router.get("/")
def root():
    logging.getLogger(__name__).info("Hit root endpoint")
    request_counter.add(1, {"endpoint": "/"})
    return {"message": "Hello from Azure!"}


@api_router.get("/health")
def health_check():
    logging.getLogger(__name__).info("Health check pinged")
    request_counter.add(1, {"endpoint": "/health"})
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
    allow_origin_regex=r"https://.*\.azurestaticapps\.net$",
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
