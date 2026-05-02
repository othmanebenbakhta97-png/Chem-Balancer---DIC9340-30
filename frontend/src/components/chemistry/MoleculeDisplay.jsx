import { InlineMath } from 'react-katex'
import React from 'react'

/**
 * Convertit une formule chimique en format LaTeX pour Katex
 * H2O -> H_2O
 * Fe2(SO4)3 -> Fe_2(SO_4)_3
 */
function formulaToLatex(formula) {
  if (!formula) return ''
  
  let latex = formula
  
  // Convertir les indices numériques après les éléments
  // H2 -> H_2, Fe2 -> Fe_2, etc.
  latex = latex.replace(/([A-Z][a-z]?)(\d+)/g, '$1_{$2}')
  
  // Gérer les parenthèses avec indices: (SO4)3 -> (SO_4)_3
  latex = latex.replace(/\)\((\d+)/g, ')}_{$1')
  latex = latex.replace(/\)([\d]+)/g, ')}_{$1}')
  
  return latex
}

/**
 * Composant pour afficher une molécule avec rendu Katex
 */
export function MoleculeDisplay({ formula, coefficient = 1, showCoefficient = true }) {
  const latex = formulaToLatex(formula)
  
  return (
    <span className="molecule-display">
      {showCoefficient && coefficient > 1 && (
        <span className="molecule-coefficient">{coefficient}</span>
      )}
      <InlineMath math={latex} />
    </span>
  )
}

/**
 * Composant pour afficher une équation complète
 */
export function EquationDisplay({ reactants, products, coefficients }) {
  // reactants et products sont des tableaux de formules
  // coefficients est un tableau dans l'ordre: [r1, r2, ..., p1, p2, ...]
  
  const allMolecules = [...reactants, ...products]
  const isProduct = (index) => index >= reactants.length
  
  return (
    <div className="equation-display">
      <div className="equation-side">
        {reactants.map((formula, idx) => (
          <React.Fragment key={`r-${idx}`}>
            {idx > 0 && <span className="equation-operator">+</span>}
            <MoleculeDisplay 
              formula={formula} 
              coefficient={coefficients[idx] || 1}
            />
          </React.Fragment>
        ))}
      </div>
      
      <span className="equation-operator">→</span>
      
      <div className="equation-side">
        {products.map((formula, idx) => {
          const coeffIdx = reactants.length + idx
          return (
            <React.Fragment key={`p-${idx}`}>
              {idx > 0 && <span className="equation-operator">+</span>}
              <MoleculeDisplay 
                formula={formula} 
                coefficient={coefficients[coeffIdx] || 1}
              />
            </React.Fragment>
          )
        })}
      </div>
    </div>
  )
}

export default MoleculeDisplay