# Chem-Balancer - Prototype STI

Système Tutoriel Intelligent pour l'aide à l'équilibrage d'équations chimiques, combinant un moteur de calcul stœchiométrique et un tuteur LLM simulé.

## ✨ Prototype de Démonstration

Ce prototype est conçu pour démontrer le concept d'un STI (Système Tutoriel Intelligent) pour l'équilibrage d'équations chimiques. Il utilise un **service LLM simulé** qui ne nécessite PAS de clé API OpenAI.

**Le professeur peut tester directement le prototype sans configuration supplémentaire !**

## 🏗️ Architecture

```
┌─────────────────┐     ┌─────────────────┐
│   Frontend      │     │    Backend      │
│   (React +      │────▶│   (FastAPI)     │
│   react-katex)  │     │                 │
└─────────────────┘     └─────────────────┘
                               │
                               ▼
                        ┌─────────────────┐
                        │  LLM Simulé     │
                        │  (Réponses      │
                        │   pré-définies)  │
                        └─────────────────┘
```

## 🚀 Démarrage Rapide (Sans Installation)

### Option 1 : Avec Python + Node.js

```bash
# Terminal 1 - Backend
cd backend
python -m venv venv
venv\Scripts\activate  # Windows
# ou: source venv/bin/activate  # Linux/Mac
pip install -r requirements.txt
python -c "import uvicorn; uvicorn.run('app.main:app', host='0.0.0.0', port=8000, reload=True)"

# Terminal 2 - Frontend
cd frontend
npm install
npm run dev
```

### Option 2 : Avec Docker

```bash
docker-compose up --build
```

## 📋 Prérequis

- Python 3.11+ (ou Docker)
- Node.js 18+ (sauf si utilisation Docker)

## 🎯 Fonctionnalités

- ✅ 5 équations chimiques de difficulté croissante
- ✅ Validation stœchiométrique automatique
- ✅ Indices pédagogiques en 3 niveaux de détail
- ✅ Tuteur LLM simulé (pas de clé API requise)
- ✅ Écran de résultats avec conseils personnalisés
- ✅ Interface professionnelle avec rendu LaTeX (KaTeX)
```

### 3. Configurer le frontend

```bash
cd ../frontend

# Installer les dépendances
npm install

# Configurer l'URL de l'API
cp .env.example .env
```

### 4. Lancer les services

**Backend (terminal 1):**
```bash
cd backend
source venv/bin/activate
uvicorn app.main:app --reload --port 8000
```

**Frontend (terminal 2):**
```bash
cd frontend
npm run dev
```

### 5. Accéder à l'application

- Frontend: http://localhost:5173
- API Docs: http://localhost:8000/docs

## 🐳 Déploiement avec Docker

```bash
# Variables d'environnement
export OPENAI_API_KEY="votre-clé-api"

# Lancer avec Docker Compose
docker-compose up --build
```

## 📁 Structure du Projet

```
chem-balancer/
├── backend/
│   ├── app/
│   │   ├── main.py              # Point d'entrée FastAPI
│   │   ├── config.py            # Configuration
│   │   ├── models/
│   │   │   └── chemistry.py     # Parsing et modèles chimiques
│   │   ├── schemas/
│   │   │   └── schemas.py       # Schémas Pydantic
│   │   ├── api/
│   │   │   └── endpoints.py     # Routes API
│   │   └── services/
│   │       ├── chemistry_service.py  # Logique chimique
│   │       └── llm_service.py   # Intégration OpenAI
│   ├── requirements.txt
│   └── Dockerfile
│
├── frontend/
│   ├── src/
│   │   ├── components/
│   │   │   ├── chemistry/
│   │   │   │   └── MoleculeDisplay.jsx  # Rendu Katex
│   │   │   ├── ExerciseInterface.jsx
│   │   │   ├── FeedbackPanel.jsx
│   │   │   └── Header.jsx
│   │   ├── services/
│   │   │   └── api.js           # Client Axios
│   │   ├── App.jsx
│   │   └── main.jsx
│   ├── package.json
│   └── vite.config.js
│
├── docker-compose.yml
└── README.md
```

## 🔌 API Endpoints

| Méthode | Endpoint | Description |
|---------|----------|-------------|
| GET | `/api/equations` | Liste des équations |
| GET | `/api/equation/{id}` | Équation par ID |
| POST | `/api/validate` | Valider une équation |
| POST | `/api/hint` | Générer un indice LLM |
| GET | `/api/health` | Vérification santé |

### Exemple de validation

```bash
curl -X POST http://localhost:8000/api/validate \
  -H "Content-Type: application/json" \
  -d '{
    "reactants": [{"formula": "H2", "coefficient": 2}, {"formula": "O2", "coefficient": 1}],
    "products": [{"formula": "H2O", "coefficient": 2}]
  }'
```

## 🧪 Équations de Test

| ID | Équation | Difficulté | Solution |
|----|----------|------------|----------|
| 1 | H₂ + O₂ → H₂O | Débutant | 2, 1 → 2 |
| 2 | Fe + S → FeS | Débutant | 1, 1 → 1 |
| 3 | CH₄ + O₂ → CO₂ + H₂O | Intermédiaire | 1, 2 → 1, 2 |
| 4 | N₂ + H₂ → NH₃ | Intermédiaire | 1, 3 → 2 |
| 5 | Fe₂O₃ + CO → Fe + CO₂ | Avancé | 1, 3 → 2, 3 |

## 🎓 Fonctionnalités

- ✅ Parsing de formules chimiques (indices, parenthèses)
- ✅ Validation stœchiométrique en temps réel
- ✅ Indices pédagogiques générés par LLM
- ✅ Rendu professionnel des formules (react-katex)
- ✅ Feedback adapté au niveau de l'apprenant
- ✅ Progression graduée de la difficulté

## 🔒 Sécurité

- La clé API OpenAI est stockée **uniquement** côté backend
- Le frontend communique avec l'API via des appels HTTP sécurisés
- Aucune clé敏感信息 n'est exposée dans le code frontend

## 📝 Licence

MIT License