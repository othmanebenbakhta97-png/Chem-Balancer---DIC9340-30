"""Schémas Pydantic pour la validation des données API."""
from pydantic import BaseModel, Field
from typing import Optional


class MoleculeInput(BaseModel):
    """Formule chimique avec coefficient optionnel."""
    formula: str = Field(..., description="Formule chimique (ex: H2O, Fe2(SO4)3)")
    coefficient: int = Field(default=1, ge=1, description="Coefficient stœchiométrique")


class EquationInput(BaseModel):
    """Équation chimique complète."""
    reactants: list[MoleculeInput] = Field(..., description="Liste des réactifs")
    products: list[MoleculeInput] = Field(..., description="Liste des produits")


class ElementError(BaseModel):
    """Erreur de déséquilibre pour un élément."""
    element: str
    reactant_count: int
    product_count: int
    difference: int


class ValidationResponse(BaseModel):
    """Réponse de validation d'équation."""
    balanced: bool
    message: str
    errors: list[ElementError] = Field(default_factory=list)


class HintRequest(BaseModel):
    """Requête pour obtenir un indice."""
    equation: EquationInput
    equation_id: int = Field(default=1, description="ID de l'équation pour le LLM simulé")
    user_level: str = Field(default="débutant", description="Niveau de l'utilisateur")
    current_attempt: dict = Field(default_factory=dict, description="État actuel de la tentative")
    error_detail: Optional[str] = Field(default=None, description="Détail de l'erreur si disponible")


class HintResponse(BaseModel):
    """Réponse avec un indice généré par LLM."""
    hint: str
    hint_level: int = Field(ge=1, le=3, description="Niveau d'indice (1=vague, 3=précis)")


class EquationResponse(BaseModel):
    """Équation formatée pour le frontend."""
    id: int
    formula: str
    reactants: list[str]
    products: list[str]
    solution: list[int] = Field(description="Coefficients corrects")
    difficulty: str