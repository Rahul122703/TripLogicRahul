from fastapi import FastAPI
from app.routers import suppliers, services
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.include_router(suppliers.router)
app.include_router(services.router)

origins = [
    "http://localhost:5173",
    "http://127.0.0.1:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"status": "Backend running"}
