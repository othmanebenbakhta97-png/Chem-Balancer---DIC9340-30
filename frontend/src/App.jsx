import React, { useState, useEffect, useCallback } from 'react'
import { Header } from './components/Header'
import { ExerciseInterface } from './components/ExerciseInterface'
import { chemApi } from './services/api'

function App() {
  // État de l'application
  const [currentEquation, setCurrentEquation] = useState(null)
  const [equations, setEquations] = useState([])
  const [currentIndex, setCurrentIndex] = useState(0)
  const [isLoading, setIsLoading] = useState(false)
  const [feedback, setFeedback] = useState(null)
  const [stats, setStats] = useState({ solved: 0, total: 0, correct: 0, errors: [] })
  const [hintLevel, setHintLevel] = useState(1)
  const [showSuccessModal, setShowSuccessModal] = useState(false)
  const [showResults, setShowResults] = useState(false)
  const [sessionResults, setSessionResults] = useState([])
  
  // Charger les équations au démarrage
  useEffect(() => {
    loadEquations()
  }, [])
  
  const loadEquations = async () => {
    try {
      setIsLoading(true)
      const data = await chemApi.getEquations()
      setEquations(data)
      if (data.length > 0) {
        setCurrentEquation(data[0])
        setCurrentIndex(0)
        setStats({ solved: 0, total: data.length, correct: 0, errors: [] })
        setSessionResults([])
      }
    } catch (error) {
      console.error('Erreur lors du chargement des équations:', error)
      setFeedback({
        type: 'error',
        title: 'Erreur de connexion',
        message: 'Impossible de charger les équations. Vérifiez que le backend est en cours d\'exécution.'
      })
    } finally {
      setIsLoading(false)
    }
  }
  
  // Valider l'équation actuelle
  const handleValidate = useCallback(async (coefficients) => {
    if (!currentEquation) return
    
    setIsLoading(true)
    setFeedback(null)
    
    try {
      // Construire l'objet equation pour l'API
      const equationInput = {
        reactants: currentEquation.reactants.map((formula, idx) => ({
          formula: formula,
          coefficient: coefficients[idx]
        })),
        products: currentEquation.products.map((formula, idx) => ({
          formula: formula,
          coefficient: coefficients[currentEquation.reactants.length + idx]
        }))
      }
      
      const result = await chemApi.validateEquation(equationInput)
      
      if (result.balanced) {
        // Succès !
        setFeedback({
          type: 'success',
          title: '✓ Bravo !',
          message: result.message
        })
        setStats(prev => ({
          ...prev,
          solved: prev.solved + 1,
          correct: prev.correct + 1
        }))
        setSessionResults(prev => [...prev, {
          equationId: currentEquation.id,
          equation: `${currentEquation.reactants.join(' + ')} → ${currentEquation.products.join(' + ')}`,
          userCoefficients: coefficients,
          correctCoefficients: currentEquation.solution,
          isCorrect: true
        }])
        setShowSuccessModal(true)
      } else {
        // Erreur
        const details = result.errors.map(e => 
          `${e.element}: ${e.reactant_count} atome(s) côté réactifs, ${e.product_count} côté produits (différence: ${Math.abs(e.difference)})`
        )
        setFeedback({
          type: 'error',
          title: '✗ Équation non équilibrée',
          message: result.message,
          details,
          showNextButton: true
        })
        
        setSessionResults(prev => [...prev, {
          equationId: currentEquation.id,
          equation: `${currentEquation.reactants.join(' + ')} → ${currentEquation.products.join(' + ')}`,
          userCoefficients: coefficients,
          correctCoefficients: currentEquation.solution,
          isCorrect: false,
          errors: result.errors
        }])
        
        // Incrémenter le niveau d'indice pour les prochains indices
        setHintLevel(prev => Math.min(prev + 1, 3))
      }
    } catch (error) {
      console.error('Erreur lors de la validation:', error)
      setFeedback({
        type: 'error',
        title: 'Erreur',
        message: 'Une erreur est survenue lors de la validation.'
      })
    } finally {
      setIsLoading(false)
    }
  }, [currentEquation, currentIndex])
  
  // Demander un indice avec niveau spécifié
  const handleHint = useCallback(async (level) => {
    if (!currentEquation) return

    setIsLoading(true)
    setFeedback(null)

    try {
      // Construire l'objet equation pour l'API
      const equationInput = {
        reactants: currentEquation.reactants.map((formula) => ({
          formula: formula,
          coefficient: 1
        })),
        products: currentEquation.products.map((formula) => ({
          formula: formula,
          coefficient: 1
        }))
      }

      const result = await chemApi.getHint(
        {
          equation: equationInput,
          equation_id: currentEquation.id,
          user_level: currentEquation.difficulty,
          current_attempt: {},
          error_detail: null
        },
        level
      )

      setFeedback({
        type: 'hint',
        title: `💡 Indice (niveau ${result.hint_level})`,
        message: result.hint
      })

      // Incrémenter le niveau d'indice pour les prochains indices
      setHintLevel(prev => Math.min(prev + 1, 3))
    } catch (error) {
      console.error('Erreur lors de la demande d\'indice:', error)
      setFeedback({
        type: 'error',
        title: 'Erreur',
        message: 'Une erreur est survenue lors de la génération de l\'indice.'
      })
    } finally {
      setIsLoading(false)
    }
  }, [currentEquation])
  
  // Passer à l'équation suivante
  const handleNextEquation = () => {
    setShowSuccessModal(false)
    setHintLevel(1) // Reset du niveau d'indice
    
    if (currentIndex < equations.length - 1) {
      const nextIndex = currentIndex + 1
      setCurrentIndex(nextIndex)
      setCurrentEquation(equations[nextIndex])
      setFeedback(null)
    } else {
      // Fin des équations - afficher les résultats
      setShowResults(true)
    }
  }
  
  // Recommencer la session
  const handleRestart = () => {
    setShowResults(false)
    setCurrentIndex(0)
    setCurrentEquation(equations[0])
    setFeedback(null)
    setHintLevel(1)
    setStats({ solved: 0, total: equations.length, correct: 0, errors: [] })
    setSessionResults([])
  }
  
  // Générer les conseils LLM basés sur les résultats
  const getLLMAdvice = () => {
    const results = sessionResults
    const correctCount = results.filter(r => r.isCorrect).length
    const totalCount = results.length
    const percentage = Math.round((correctCount / totalCount) * 100)
    
    // Analyser les erreurs par type
    const errorElements = {}
    results.forEach(r => {
      if (!r.isCorrect && r.errors) {
        r.errors.forEach(e => {
          if (!errorElements[e.element]) {
            errorElements[e.element] = 0
          }
          errorElements[e.element]++
        })
      }
    })
    
    const weakestElement = Object.keys(errorElements).length > 0 
      ? Object.entries(errorElements).sort((a, b) => b[1] - a[1])[0][0]
      : null
    
    let advice = ""
    
    if (percentage >= 80) {
      advice = `Excellent travail ! Vous avez réussi ${correctCount}/${totalCount} équations (${percentage}%). `
      advice += "Vous maîtrisez bien la stœchiométrie. "
      if (weakestElement) {
        advice += `Un petit rappel sur l'élément ${weakestElement} pourrait être utile pour atteindre la perfection.`
      } else {
        advice += "Essayez des équations plus complexes avec des ions polyatomiques pour vous challenger davantage."
      }
    } else if (percentage >= 50) {
      advice = `Bon début ! Vous avez réussi ${correctCount}/${totalCount} équations (${percentage}%). `
      advice += "Vous comprenez les bases de l'équilibrage. "
      if (weakestElement) {
        advice += `Attention à l'élément ${weakestElement} qui semble poser problème. `
        advice += `Entraînez-vous particulièrement sur les équations impliquant ${weakestElement}.`
      } else {
        advice += "Continuez à pratiquer pour renforcer votre compréhension de la loi de conservation de la masse."
      }
    } else {
      advice = `Vous avez réussi ${correctCount}/${totalCount} équations (${percentage}%). `
      advice += "Ne vous découragez pas ! L'équilibrage des équations chimiques demande de la pratique. "
      advice += "Revoyez la loi de Lavoisier : 'Rien ne se perd, rien ne se crée'. "
      if (weakestElement) {
        advice += `L'élément ${weakestElement} semble poser des difficultés. `
        advice += `Concentrez-vous sur le dénombrement des atomes de ${weakestElement} dans les réactifs et les produits.`
      } else {
        advice += "Commencez par des équations simples comme H₂ + O₂ → H₂O pour construire votre confiance."
      }
    }
    
    return advice
  }
  
  // Afficher les résultats finaux
  if (showResults) {
    const correctCount = sessionResults.filter(r => r.isCorrect).length
    const totalCount = sessionResults.length
    const percentage = Math.round((correctCount / totalCount) * 100)
    
    return (
      <div className="app">
        <Header stats={stats} />
        
        <main className="main-content">
          <div className="exercise-card results-card">
            <h2 style={{ marginBottom: '1.5rem', textAlign: 'center' }}>📊 Résultats de la Session</h2>
            
            <div className="results-summary" style={{
              background: percentage >= 50 ? '#dcfce7' : '#fee2e2',
              padding: '1.5rem',
              borderRadius: '0.75rem',
              marginBottom: '1.5rem',
              textAlign: 'center'
            }}>
              <div style={{ fontSize: '3rem', fontWeight: 'bold' }}>{percentage}%</div>
              <div style={{ color: '#64748b' }}>{correctCount} / {totalCount} équations correctes</div>
            </div>
            
            <div className="results-list" style={{ marginBottom: '1.5rem' }}>
              <h3 style={{ marginBottom: '0.75rem' }}>Détail des réponses :</h3>
              {sessionResults.map((result, idx) => (
                <div key={idx} style={{
                  display: 'flex',
                  alignItems: 'center',
                  gap: '0.5rem',
                  padding: '0.5rem',
                  background: result.isCorrect ? '#dcfce7' : '#fee2e2',
                  borderRadius: '0.5rem',
                  marginBottom: '0.5rem'
                }}>
                  <span>{result.isCorrect ? '✓' : '✗'}</span>
                  <span style={{ flex: 1 }}>Équation #{result.equationId}: {result.equation}</span>
                </div>
              ))}
            </div>
            
            <div className="llm-advice" style={{
              background: '#fef3c7',
              padding: '1rem',
              borderRadius: '0.75rem',
              marginBottom: '1.5rem'
            }}>
              <h3 style={{ marginBottom: '0.5rem' }}>💡 Conseils du Tuteur :</h3>
              <p>{getLLMAdvice()}</p>
            </div>
            
            <div className="button-group" style={{ justifyContent: 'center' }}>
              <button className="btn btn-primary" onClick={handleRestart}>
                🔄 Recommencer
              </button>
            </div>
          </div>
        </main>
      </div>
    )
  }
  
  return (
    <div className="app">
      <Header stats={stats} />
      
      <main className="main-content">
        <ExerciseInterface
          equation={currentEquation}
          onValidate={handleValidate}
          onHint={handleHint}
          isLoading={isLoading}
          feedback={feedback}
        />
        
        {/* Bouton pour passer si l'utilisateur abandonne */}
        {feedback && feedback.showNextButton && (
          <div style={{ marginTop: '1rem', textAlign: 'center' }}>
            <button 
              className="btn btn-secondary" 
              onClick={handleNextEquation}
            >
              Passer à la prochaine question →
            </button>
          </div>
        )}
      </main>
      
      {/* Modal de succès */}
      {showSuccessModal && (
        <div className="modal-overlay" onClick={handleNextEquation}>
          <div className="modal" onClick={e => e.stopPropagation()}>
            <h2>🎉 Équation équilibrée !</h2>
            <p>La loi de conservation de la masse est respectée.</p>
            <button className="btn btn-primary" onClick={handleNextEquation}>
              {currentIndex < equations.length - 1 ? 'Équation suivante →' : 'Voir les résultats'}
            </button>
          </div>
        </div>
      )}
    </div>
  )
}

export default App