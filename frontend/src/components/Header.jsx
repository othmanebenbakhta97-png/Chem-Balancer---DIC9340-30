import React from 'react'

/**
 * En-tête de l'application avec statistiques
 */
export function Header({ stats }) {
  return (
    <header className="header">
      <h1>🧪 Chem-Balancer</h1>
      {stats && (
        <div className="header-stats">
          <span>Équations résolues: {stats.solved || 0}</span>
          <span>Précision: {stats.accuracy || 0}%</span>
        </div>
      )}
    </header>
  )
}

export default Header