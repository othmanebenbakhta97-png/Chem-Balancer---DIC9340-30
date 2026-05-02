"""Service de logique chimique - parsing et validation."""
from typing import Optional
from app.models.chemistry import Molecule, ChemicalEquation
from app.schemas.schemas import (
    EquationInput, 
    ValidationResponse, 
    ElementError,
    MoleculeInput
)


class ChemistryService:
    """Service pour la manipulation des équations chimiques."""
    
    @staticmethod
    def validate_equation(equation: EquationInput) -> ValidationResponse:
        """
        Valide une équation chimique et retourne le diagnostic.
        
        Args:
            equation: Équation à valider
            
        Returns:
            ValidationResponse avec le résultat et les erreurs éventuelles
        """
        # Convertir les entrées en objets Molecule
        reactants = [
            Molecule(formula=m.formula, coefficient=m.coefficient)
            for m in equation.reactants
        ]
        products = [
            Molecule(formula=m.formula, coefficient=m.coefficient)
            for m in equation.products
        ]
        
        # Créer l'équation chimique
        chem_eq = ChemicalEquation(reactants=reactants, products=products)
        
        # Vérifier l'équilibre
        is_balanced, errors = chem_eq.is_balanced()
        
        if is_balanced:
            return ValidationResponse(
                balanced=True,
                message="Équation correctement équilibrée ! La loi de conservation de la masse est respectée."
            )
        else:
            # Construire le message d'erreur
            error_details = [ElementError(**e) for e in errors]
            
            # Message descriptif
            if len(errors) == 1:
                e = errors[0]
                side = "réactifs" if e["difference"] > 0 else "produits"
                msg = f"Déséquilibre détecté : il y a {abs(e['difference'])} atome(s) de {e['element']} en trop du côté des {side}."
            else:
                elements = ", ".join([e["element"] for e in errors])
                msg = f"Déséquilibres détectés pour les éléments : {elements}."
            
            return ValidationResponse(
                balanced=False,
                message=msg,
                errors=error_details
            )
    
    @staticmethod
    def get_error_detail(equation: EquationInput) -> Optional[str]:
        """
        Retourne un détail technique sur l'erreur pour le LLM.
        
        Args:
            equation: Équation à analyser
            
        Returns:
            Message technique décrivant l'erreur ou None si équilibrée
        """
        reactants = [
            Molecule(formula=m.formula, coefficient=m.coefficient)
            for m in equation.reactants
        ]
        products = [
            Molecule(formula=m.formula, coefficient=m.coefficient)
            for m in equation.products
        ]
        
        chem_eq = ChemicalEquation(reactants=reactants, products=products)
        is_balanced, errors = chem_eq.is_balanced()
        
        if is_balanced:
            return None
        
        # Construire un message technique
        details = []
        for e in errors:
            if e["difference"] > 0:
                details.append(f"il manque {e['difference']} atome(s) de {e['element']} du côté des produits")
            else:
                details.append(f"il y a {abs(e['difference'])} atome(s) de {e['element']} en trop du côté des produits")
        
        return "; ".join(details)
    
    @staticmethod
    def format_equation_latex(equation: EquationInput) -> str:
        """
        Formate l'équation pour l'affichage LaTeX.
        
        Args:
            equation: Équation à formater
            
        Returns:
            Chaîne LaTeX pour render avec Katex
        """
        def format_molecule(m: MoleculeInput) -> str:
            formula = m.formula
            # Convertir les indices numériques en format LaTeX
            # H2O -> H_2O
            import re
            formula = re.sub(r'([A-Z][a-z]?)(\d+)', r'\1_\2', formula)
            # Gérer les parenthèses: (SO4)3 -> (SO_4)_3
            formula = re.sub(r'\)([\d]+)', r')_\1', formula)
            return formula
        
        reactants = " + ".join([format_molecule(m) for m in equation.reactants])
        products = " + ".join([format_molecule(m) for m in equation.products])
        
        return f"{reactants} \\rightarrow {products}"