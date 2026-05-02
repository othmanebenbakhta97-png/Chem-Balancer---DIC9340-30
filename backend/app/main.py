"""Point d'entrée principal de l'API Chem-Balancer."""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.endpoints import router
from app.config import get_settings


# Créer l'application FastAPI
app = FastAPI(
    title="Chem-Balancer API",
    description="API pour le Système Tutoriel Intelligent d'aide à l'équilibrage d'équations chimiques",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

# Configurer CORS pour le frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://localhost:3000", "*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Inclure les routes
app.include_router(router)


@app.get("/")
async def root():
    """Page d'accueil de l'API."""
    return {
        "name": "Chem-Balancer API",
        "version": "1.0.0",
        "docs": "/docs",
        "health": "/api/health"
    }


if __name__ == "__main__":
    import uvicorn
    settings = get_settings()
    uvicorn.run(
        "app.main:app",
        host=settings.host,
        port=settings.port,
        reload=True
    )