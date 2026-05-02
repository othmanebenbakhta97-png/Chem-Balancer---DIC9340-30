"""Modèles de données pour la chimie."""
import re
from dataclasses import dataclass, field
from typing import Optional


@dataclass
class Atom:
    """Représente un atome avec son symbole et son nombre."""
    symbol: str
    count: int = 1
    
    def __repr__(self) -> str:
        return f"Atom({self.symbol}: {self.count})"


@dataclass
class Molecule:
    """Représente une molécule avec sa formule et ses atomes décomposés."""
    formula: str
    atoms: dict[str, int] = field(default_factory=dict)
    coefficient: int = 1
    
    def __post_init__(self):
        """Parse la formule si les atomes ne sont pas fournis."""
        if not self.atoms:
            self.atoms = Molecule.parse_formula(self.formula)
    
    @staticmethod
    def parse_formula(formula: str) -> dict[str, int]:
        """
        Parse une formule chimique et retourne un dictionnaire {élément: count}.
        
        Gère:
        - Les indices: H2O -> H:2, O:1
        - Les parenthèses: Fe2(SO4)3 -> Fe:2, S:3, O:12
        - Les coefficients implicites (toujours 1)
        
        Args:
            formula: Formule chimique brute (ex: "H2O", "Fe2(SO4)3")
            
        Returns:
            Dict {symbole: nombre_d'atomes}
        """
        atoms: dict[str, int] = {}
        
        def parse_group(formula: str, multiplier: int = 1) -> None:
            """Parse récursivement un groupe chimique."""
            i = 0
            while i < len(formula):
                char = formula[i]
                
                if char.isupper():
                    # Début d'un élément
                    symbol = char
                    i += 1
                    
                    # Vérifier si lettre minuscule (Fe, Ca, etc.)
                    if i < len(formula) and formula[i].islower():
                        symbol += formula[i]
                        i += 1
                    
                    # Lire le nombre (si présent)
                    num_match = re.match(r'(\d*)', formula[i:])
                    if num_match and num_match.group(1):
                        count = int(num_match.group(1))
                        i += len(num_match.group(1))
                    else:
                        count = 1
                    
                    atoms[symbol] = atoms.get(symbol, 0) + count * multiplier
                    
                elif char == '(':
                    # Trouver le groupe correspondant
                    depth = 1
                    start = i + 1
                    i = start
                    while depth > 0 and i < len(formula):
                        if formula[i] == '(':
                            depth += 1
                        elif formula[i] == ')':
                            depth -= 1
                        i += 1
                    
                    group = formula[start:i-1]
                    
                    # Lire le multiplicateur après la parenthèse
                    num_match = re.match(r'(\d*)', formula[i:])
                    if num_match and num_match.group(1):
                        group_mult = int(num_match.group(1))
                        i += len(num_match.group(1))
                    else:
                        group_mult = 1
                    
                    parse_group(group, multiplier * group_mult)
                    
                elif char.isdigit():
                    # Nombre sans élément (erreur de format, on ignore)
                    i += 1
                else:
                    i += 1
        
        parse_group(formula)
        return atoms
    
    def get_total_atoms(self) -> dict[str, int]:
        """
        Retourne le nombre total d'atomes en tenant compte du coefficient.
        
        Returns:
            Dict {symbole: nombre_total}
        """
        return {elem: count * self.coefficient for elem, count in self.atoms.items()}
    
    def __repr__(self) -> str:
        return f"Molecule({self.formula}, coeff={self.coefficient}, atoms={self.atoms})"


@dataclass
class ChemicalEquation:
    """Représente une équation chimique complète."""
    reactants: list[Molecule]
    products: list[Molecule]
    
    def get_reactant_atoms(self) -> dict[str, int]:
        """Retourne le décompte total des atomes côté réactifs."""
        total: dict[str, int] = {}
        for mol in self.reactants:
            for elem, count in mol.get_total_atoms().items():
                total[elem] = total.get(elem, 0) + count
        return total
    
    def get_product_atoms(self) -> dict[str, int]:
        """Retourne le décompte total des atomes côté produits."""
        total: dict[str, int] = {}
        for mol in self.products:
            for elem, count in mol.get_total_atoms().items():
                total[elem] = total.get(elem, 0) + count
        return total
    
    def is_balanced(self) -> tuple[bool, list[dict]]:
        """
        Vérifie si l'équation est équilibrée.
        
        Returns:
            Tuple (est_équilibrée, liste_erreurs)
        """
        reactant_atoms = self.get_reactant_atoms()
        product_atoms = self.get_product_atoms()
        
        all_elements = set(reactant_atoms.keys()) | set(product_atoms.keys())
        errors = []
        
        for elem in sorted(all_elements):
            r_count = reactant_atoms.get(elem, 0)
            p_count = product_atoms.get(elem, 0)
            
            if r_count != p_count:
                diff = r_count - p_count
                errors.append({
                    "element": elem,
                    "reactant_count": r_count,
                    "product_count": p_count,
                    "difference": diff
                })
        
        return len(errors) == 0, errors
    
    def __repr__(self) -> str:
        r = " + ".join([f"{m.coefficient if m.coefficient > 1 else ''}{m.formula}" for m in self.reactants])
        p = " + ".join([f"{m.coefficient if m.coefficient > 1 else ''}{m.formula}" for m in self.products])
        return f"{r} -> {p}"