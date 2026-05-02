"""Endpoints API pour Chem-Balancer."""
from fastapi import APIRouter, HTTPException
from typing import Optional
from app.schemas.schemas import (
    EquationInput,
    ValidationResponse,
    HintRequest,
    HintResponse,
    EquationResponse
)
from app.services.chemistry_service import ChemistryService
from app.services.mock_llm_service import get_mock_llm_service


router = APIRouter(prefix="/api", tags=["chem-balancer"])

# Banque d'équations de test (prototype)
EQUATIONS_DB = [
    {
        "id": 1,
        "formula": "H2 + O2 -> H2O",
        "reactants": ["H_2", "O_2"],
        "products": ["H_2O"],
        "solution": [2, 1, 2],  # H2, O2, H2O
        "difficulty": "débutant"
    },
    {
        "id": 2,
        "formula": "Fe + S -> FeS",
        "reactants": ["Fe", "S"],
        "products": ["FeS"],
        "solution": [1, 1, 1],
        "difficulty": "débutant"
    },
    {
        "id": 3,
        "formula": "CH4 + O2 -> CO2 + H2O",
        "reactants": ["CH_4", "O_2"],
        "products": ["CO_2", "H_2O"],
        "solution": [1, 2, 1, 2],
        "difficulty": "intermédiaire"
    },
    {
        "id": 4,
        "formula": "N2 + H2 -> NH3",
        "reactants": ["N_2", "H_2"],
        "products": ["NH_3"],
        "solution": [1, 3, 2],
        "difficulty": "intermédiaire"
    },
    {
        "id": 5,
        "formula": "Fe2O3 + CO -> Fe + CO2",
        "reactants": ["Fe_2O_3", "CO"],
        "products": ["Fe", "CO_2"],
        "solution": [1, 3, 2, 3],
        "difficulty": "avancé"
    }
]


@router.get("/equations", response_model=list[EquationResponse])
async def get_equations(level: Optional[str] = None):
    """
    Récupère la liste des équations disponibles.
    
    Args:
        level: Filtrer par niveau (optionnel)
        
    Returns:
        Liste des équations
    """
    if level:
        return [eq for eq in EQUATIONS_DB if eq["difficulty"] == level]
    return EQUATIONS_DB


@router.get("/equation/{equation_id}", response_model=EquationResponse)
async def get_equation(equation_id: int):
    """
    Récupère une équation spécifique par son ID.
    
    Args:
        equation_id: ID de l'équation
        
    Returns:
        Équation demandée
    """
    for eq in EQUATIONS_DB:
        if eq["id"] == equation_id:
            return eq
    raise HTTPException(status_code=404, detail="Équation non trouvée")


@router.post("/validate", response_model=ValidationResponse)
async def validate_equation(equation: EquationInput):
    """
    Valide une équation chimique.
    
    Vérifie si les coefficients stœchiométriques respectent
    la loi de conservation de la masse.
    
    Args:
        equation: Équation à valider
        
    Returns:
        Résultat de la validation avec erreurs éventuelles
    """
    return ChemistryService.validate_equation(equation)


@router.post("/hint", response_model=HintResponse)
async def get_hint(request: HintRequest, hint_level: int = 1):
    """
    Génère un indice pédagogique pour aider l'étudiant.
    
    Utilise le service LLM simulé (pas de clé API requise).
    
    Args:
        request: Données de la requête (équation, niveau, erreur)
        hint_level: Niveau de précision de l'indice (1-3)
        
    Returns:
        Indice généré
    """
    try:
        # Utiliser le service LLM simulé (pas de clé OpenAI requise)
        mock_llm = get_mock_llm_service()
        
        # Récupérer l'ID de l'équation depuis la requête ou utiliser 1 par défaut
        equation_id = getattr(request, 'equation_id', 1)
        
        # Générer l'indice simulé
        hint_text = mock_llm.get_hint(
            equation_id=equation_id,
            hint_level=hint_level,
            user_level=request.user_level
        )
        
        return HintResponse(hint=hint_text, hint_level=hint_level)
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erreur lors de la génération de l'indice: {str(e)}")


@router.get("/health")
async def health_check():
    """Vérification de santé de l'API."""
    return {"status": "healthy", "service": "chem-balancer-api"}