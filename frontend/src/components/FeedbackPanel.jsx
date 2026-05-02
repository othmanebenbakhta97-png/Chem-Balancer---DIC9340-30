import React from 'react'

/**
 * Panneau de feedback pour afficher les messages du tuteur
 */
export function FeedbackPanel({ type = 'info', title, children }) {
  const panelClass = `feedback-panel ${type}`
  
  const icons = {
    success: '✓',
    error: '✗',
    hint: '💡',
    info: 'ℹ'
  }
  
  return (
    <div className={panelClass}>
      <div className="feedback-header">
        <span>{icons[type] || icons.info}</span>
        <span>{title || (type === 'success' ? 'Succès' : type === 'error' ? 'Erreur' : 'Indice')}</span>
      </div>
      <div className="feedback-content">
        {children}
      </div>
    </div>
  )
}

export default FeedbackPanel