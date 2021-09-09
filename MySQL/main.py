from fastapi import FastAPI, APIRouter
from app.routes import Property
from starlette.middleware.cors import CORSMiddleware

origins = [
    "*",
]

app = FastAPI(debug=True, title="Habi_Backend Property",
              docs_url="/Property/docs", openapi_url="/Property/openapi.json")

api_router = APIRouter()
api_router.include_router(Property.router, prefix="/property/search", tags=["Property"])
app.include_router(api_router)
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_methods=["*"],
    allow_headers=["*"],
)
