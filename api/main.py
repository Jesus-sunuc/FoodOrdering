from fastapi import FastAPI, APIRouter
from fastapi.middleware.cors import CORSMiddleware
from routes.item_router import router as item_router

app = FastAPI()

api_router = APIRouter(prefix="/api")


@api_router.get("/")
def root():
    return {"message": "Hello from Azure!"}


@api_router.get("/health")
def health_check():
    return {"status": "Healthy"}


api_router.include_router(item_router)

app.include_router(api_router)

origins = [
    "http://localhost:4173",
    "http://lunchbox6.duckdns.org",
    "https://yellow-island-0e74ba610.6.azurestaticapps.net",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
