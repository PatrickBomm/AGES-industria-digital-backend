from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
from app.database import models
from app.database.database import engine
from app.api.routers import example_router


# Starts the models for our database
models.Base.metadata.create_all(bind=engine)

def init_app() -> FastAPI:
    app = FastAPI(title="Industria Digital Backend")
    # Include routers from our application
    app.include_router(example_router.router)
    # Include the CORS middleware.
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_methods=["OPTIONS", "GET", "POST", "PUT", "DELETE", "PATCH"],
        allow_headers=["*"]
    )
    return app


app = init_app()
