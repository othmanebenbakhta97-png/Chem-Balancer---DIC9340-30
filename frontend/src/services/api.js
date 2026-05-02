import axios from 'axios'

const API_URL = import.meta.env.VITE_API_URL || 'http://localhost:8000'

const api = axios.create({
  baseURL: API_URL,
  headers: {
    'Content-Type': 'application/json'
  }
})

export const chemApi = {
  /**
   * Récupère la liste des équations disponibles
   */
  async getEquations(level = null) {
    const params = level ? { level } : {}
    const response = await api.get('/api/equations', { params })
    return response.data
  },

  /**
   * Récupère une équation spécifique par ID
   */
  async getEquation(id) {
    const response = await api.get(`/api/equation/${id}`)
    return response.data
  },

  /**
   * Valide une équation chimique
   * @param {Object} equation - { reactants: [{formula, coefficient}], products: [{formula, coefficient}] }
   */
  async validateEquation(equation) {
    const response = await api.post('/api/validate', equation)
    return response.data
  },

  /**
   * Demande un indice au tuteur LLM
   * @param {Object} request - { equation, user_level, current_attempt, error_detail }
   * @param {number} hintLevel - Niveau de précision de l'indice (1-3)
   */
  async getHint(request, hintLevel = 1) {
    const response = await api.post('/api/hint', request, {
      params: { hint_level: hintLevel }
    })
    return response.data
  },

  /**
   * Vérification de santé de l'API
   */
  async healthCheck() {
    const response = await api.get('/api/health')
    return response.data
  }
}

export default api