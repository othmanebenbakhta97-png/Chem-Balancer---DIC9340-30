import React from 'react'

/**
 * Composant de sélection du niveau d'indice
 */
export function HintSelector({ onSelect, currentLevel = 1, disabled = false }) {
  const hintOptions = [
    { level: 1, title: "Indice vague", description: "Orientation générale" },
    { level: 2, title: "Indice moyen", description: "Pointer vers l'élément" },
    { level: 3, title: "Indice précis", description: "Explication de la méthode" }
  ]
  
  return (
    <div className="hint-selector">
      <p className="hint-selector-title">Choisissez un niveau d'indice :</p>
      <div className="hint-options">
        {hintOptions.map(opt => (
          <button
            key={opt.level}
            className={`hint-option ${currentLevel === opt.level ? 'selected' : ''}`}
            onClick={() => onSelect(opt.level)}
            disabled={disabled}
          >
            <span className="hint-level">{opt.level}</span>
            <span className="hint-title">{opt.title}</span>
            <span className="hint-desc">{opt.description}</span>
          </button>
        ))}
      </div>
    </div>
  )
}

export default HintSelector