import React, { useState, useEffect } from 'react'
import { EquationDisplay } from './chemistry/MoleculeDisplay'
import { FeedbackPanel } from './FeedbackPanel'
import { HintSelector } from './HintSelector'

/**
 * Interface principale d'exercice pour l'équilibrage d'équations
 * Nouveau flux: Sélection d'indice -> Auto-validation
 */
export function ExerciseInterface({ 
  equation, 
  onValidate, 
  onHint,
  isLoading = false,
  feedback = null
}) {
  // État des coefficients saisis par l'utilisateur
  const [coefficients, setCoefficients] = useState([])
  // État pour le niveau d'indice sélectionné
  const [selectedHintLevel, setSelectedHintLevel] = useState(1)
  // État pour savoir si on a demandé un indice
  const [hasRequestedHint, setHasRequestedHint] = useState(false)
  
  // Initialiser les coefficients à 1 pour chaque molécule
  useEffect(() => {
    if (equation) {
      const totalMolecules = equation.reactants.length + equation.products.length
      setCoefficients(Array(totalMolecules).fill(1))
      setHasRequestedHint(false)
      setSelectedHintLevel(1)
    }
  }, [equation])
  
  // Gérer le changement d'un coefficient
  const handleCoefficientChange = (index, value) => {
    const newCoefficients = [...coefficients]
    const num = parseInt(value) || 1
    newCoefficients[index] = Math.max(1, num) // Minimum 1
    setCoefficients(newCoefficients)
  }
  
  // Gérer la demande d'indice avec niveau
  const handleHintRequest = (level) => {
    setSelectedHintLevel(level)
    setHasRequestedHint(true)
    
    if (onHint) {
      onHint(level)
    }
  }
  
  // Gérer la validation automatique après l'indice
  const handleValidate = () => {
    if (onValidate) {
      onValidate(coefficients)
    }
  }
  
  if (!equation) {
    return (
      <div className="exercise-card">
        <div className="loading">
          <div className="spinner"></div>
        </div>
      </div>
    )
  }
  
  const difficultyClass = `difficulty-${equation.difficulty}`
  
  return (
    <div className="exercise-card">
      <div className="exercise-header">
        <span className="exercise-title">Équation #{equation.id}</span>
        <span className={`exercise-difficulty ${difficultyClass}`}>
          {equation.difficulty}
        </span>
      </div>
      
      <div className="instructions">
        <strong>Consigne :</strong>
        Ajustez les coefficients stœchiométriques pour équilibrer l'équation.
        Cliquez sur "Vérifier" pour valider, ou demandez un indice d'abord.
      </div>
      
      <EquationDisplay
        reactants={equation.reactants}
        products={equation.products}
        coefficients={coefficients}
      />
      
      {/* Sélecteur d'indice - NOUVEAU FLUX */}
      {!hasRequestedHint && !feedback && (
        <div className="hint-section">
          <HintSelector 
            onSelect={handleHintRequest}
            currentLevel={selectedHintLevel}
            disabled={isLoading}
          />
        </div>
      )}
      
      <div className="button-group">
        <button 
          className="btn btn-primary" 
          onClick={handleValidate}
          disabled={isLoading}
        >
          Vérifier
        </button>
      </div>
      
      {isLoading && (
        <div className="loading" style={{ marginTop: '1rem' }}>
          <div className="spinner"></div>
        </div>
      )}
      
      {feedback && (
        <FeedbackPanel 
          type={feedback.type} 
          title={feedback.title}
        >
          <p>{feedback.message}</p>
          {feedback.details && (
            <ul style={{ marginLeft: '1.5rem', marginTop: '0.5rem' }}>
              {feedback.details.map((detail, idx) => (
                <li key={idx}>{detail}</li>
              ))}
            </ul>
          )}
        </FeedbackPanel>
      )}
    </div>
  )
}

export default ExerciseInterface