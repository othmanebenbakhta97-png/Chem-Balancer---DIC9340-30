"""Configuration du backend Chem-Balancer."""
import os
from pydantic_settings import BaseSettings
from functools import lru_cache


class Settings(BaseSettings):
    """Paramètres de configuration chargés depuis les variables d'environnement."""
    
    # OpenAI
    openai_api_key: str = ""
    
    # Supabase
    supabase_url: str = ""
    supabase_key: str = ""
    
    # Server
    host: str = "0.0.0.0"
    port: int = 8000
    
    # LLM Configuration
    llm_model: str = "gpt-4"
    llm_temperature: float = 0.7
    llm_max_tokens: int = 500
    
    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


@lru_cache()
def get_settings() -> Settings:
    """Retourne les paramètres de configuration (singleton)."""
    return Settings()