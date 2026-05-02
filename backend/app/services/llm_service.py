"""Service d'intégration LLM pour les indices pédagogiques."""
import os
from typing import Optional
from openai import OpenAI
from app.config import get_settings


# Prompt système pour le tuteur
TUTOR_SYSTEM_PROMPT = """Tu es un tuteur en chimie expert et bienveillant. Ton rôle est d'aider un étudiant à équilibrer une équation chimique en utilisant la loi de conservation de la masse de Lavoisier.

RÈGLES ABSOLUES:
1. Ne donne JAMAIS la réponse directe (ne révèle jamais les coefficients)
2. Guide l'étudiant par des questions et des indices progressifs
3. Adapte ton langage au niveau de l'étudiant:
   - "débutant": utilise un langage simple, des analogies du quotidien
   - "intermédiaire": utilise un vocabulaire chimique de base
   - "avancé": utilise des termes techniques (stœchiométrie, oxydoréduction, etc.)
4. Référence toujours la loi de conservation de la masse: "Rien ne se perd, rien ne se crée"
5. Structure tes indices en 3 niveaux de précision:
   - Niveau 1: Indice vague pour orienter l'attention
   - Niveau 2: Indice pointing vers l'élément spécifique en cause
   - Niveau 3: Explication de la logique de résolution (sans donner la réponse)

Comportement:
- Si l'étudiant fait une erreur, ne corrige pas immédiatement
- Pose des questions pour l'amener à découvrir par lui-même
- Encourage quand il progresse dans le bon chemin
- Sois patient et positif"""


class LLMService:
    """Service pour communiquer avec le LLM OpenAI."""
    
    def __init__(self):
        settings = get_settings()
        api_key = settings.openai_api_key or os.getenv("OPENAI_API_KEY", "")
        
        if not api_key:
            raise ValueError("OPENAI_API_KEY n'est pas configurée")
        
        self.client = OpenAI(api_key=api_key)
        self.model = settings.llm_model
        self.temperature = settings.llm_temperature
        self.max_tokens = settings.llm_max_tokens
    
    def generate_hint(
        self, 
        equation_str: str,
        user_level: str,
        error_detail: Optional[str],
        hint_level: int = 1
    ) -> str:
        """
        Génère un indice pédagogique pour l'étudiant.
        
        Args:
            equation_str: Équation en format lisible
            user_level: Niveau de l'étudiant (débutant, intermédiaire, avancé)
            error_detail: Détail technique de l'erreur
            hint_level: Niveau de précision de l'indice (1-3)
            
        Returns:
            Texte de l'indice généré
        """
        # Construire le contexte
        context = f"Équation à équilibrer: {equation_str}\n"
        context += f"Niveau de l'étudiant: {user_level}\n"
        
        if error_detail:
            context += f"Problème détecté: {error_detail}\n"
        
        # Instructions selon le niveau d'indice
        if hint_level == 1:
            context += "\nGénère un indice de NIVEAU 1 (vague, pour orienter l'attention sans révéler la solution)."
        elif hint_level == 2:
            context += "\nGénère un indice de NIVEAU 2 (plus précis, pointe vers l'élément en cause)."
        else:
            context += "\nGénère un indice de NIVEAU 3 (explication de la méthode, mais sans donner les coefficients)."
        
        try:
            response = self.client.chat.completions.create(
                model=self.model,
                messages=[
                    {"role": "system", "content": TUTOR_SYSTEM_PROMPT},
                    {"role": "user", "content": context}
                ],
                temperature=self.temperature,
                max_tokens=self.max_tokens
            )
            
            return response.choices[0].message.content.strip()
            
        except Exception as e:
            return f"Désolé, je ne peux pas générer d'indice pour le moment. Erreur: {str(e)}"
    
    def check_equation_correct(self, equation_str: str) -> bool:
        """
        Vérifie si l'équation est correctement équilibrée (pour validation finale).
        
        Args:
            equation_str: Équation à vérifier
            
        Returns:
            True si équilibrée, False sinon
        """
        # Cette méthode est optionnelle - la validation se fait côté backend
        # On garde cette méthode pour une validation supplémentaire par LLM
        prompt = f"""Vérifie si cette équation chimique est correctement équilibrée.
Réponds uniquement par "OUI" si elle est équilibrée, "NON" si elle ne l'est pas.

Équation: {equation_str}"""
        
        try:
            response = self.client.chat.completions.create(
                model=self.model,
                messages=[
                    {"role": "system", "content": "Tu es un expert en chimie. Réponds uniquement par OUI ou NON."},
                    {"role": "user", "content": prompt}
                ],
                temperature=0,
                max_tokens=10
            )
            
            answer = response.choices[0].message.content.strip().upper()
            return "OUI" in answer
            
        except Exception:
            return False


# Instance singleton
_llm_service: Optional[LLMService] = None


def get_llm_service() -> LLMService:
    """Retourne l'instance du service LLM (singleton)."""
    global _llm_service
    if _llm_service is None:
        _llm_service = LLMService()
    return _llm_service