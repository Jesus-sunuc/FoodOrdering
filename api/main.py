from fastapi import APIRouter, FastAPI
from routes.item_router import router as item_router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()


@app.get("/")
def root():
    return {"message": "Hello from Azure!"}


# origins = [
#     "https://yellow-island-0e74ba610.6.azurestaticapps.net",
#     "http://localhost:5173",
# ]

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

router = APIRouter(prefix="/api")

app.include_router(item_router, prefix="/api")
