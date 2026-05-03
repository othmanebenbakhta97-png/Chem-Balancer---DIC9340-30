# MEMOIRE TECHNIQUE - Chem-Balancer STI

## Système Tutoriel Intelligent pour l'Équilibrage d'Équations Chimiques

---

## 1. PRÉSENTATION DU PROJET

### 1.1 Objectif du Projet

**Chem-Balancer** est un prototype de Système Tutoriel Intelligent (STI) conçu pour aider les étudiants à apprendre l'équilibrage des équations chimiques. Le système combine :

- Un **moteur de validation stœchiométrique** qui vérifie automatiquement si les coefficients proposés par l'étudiant respectent la loi de conservation de la masse (Lavoisier)
- Un **tuteur LLM** qui génère des indices pédagogiques personnalisés selon le niveau de l'étudiant
- Une **interface web moderne** avec rendu professionnel des formules chimiques via LaTeX (KaTeX)

### 1.2 Public Cible

- Étudiants en chimie (niveau secondaire, pré-universitaire ou universitaire)
- Professeurs souhaitant démontrer les capacités d'un STI

### 1.3 Fonctionnalités Principales

| Fonctionnalité | Description |
|----------------|-------------|
| Validation automatique | Vérifie si l'équation est correctement équilibrée |
| Indices pédagogiques | 3 niveaux de détail (vague, moyen, précis) |
| Tuteur LLM simulé | Réponses détaillées style ChatGPT/Gemini |
| 5 équations de test | Difficulté progressive (débutant → avancé) |
| Écran de résultats | Analyse finale avec conseils personnalisés |

---

## 2. ARCHITECTURE TECHNIQUE

### 2.1 Vue d'Ensemble

```
┌─────────────────────────────────────────────────────────────────┐
│                        FRONTEND (React)                         │
│  ┌─────────────┐  ┌──────────────────┐  ┌────────────────────┐  │
│  │   Header    │  │ ExerciseInterface│  │   FeedbackPanel    │  │
│  │             │  │                  │  │                    │  │
│  │  - Logo     │  │  - Coefficients │  │  - Success msg    │  │
│  │  - Progress │  │  - HintSelector  │  │  - Error details  │  │
│  │  - Stats    │  │  - EquationDisp  │  │  - LLM hints      │  │
│  └─────────────┘  └──────────────────┘  └────────────────────┘  │
│                              │                                   │
│                     ┌────────▼────────┐                          │
│                     │  MoleculeDisplay│                          │
│                     │  (KaTeX render) │                          │
│                     └─────────────────┘                          │
└─────────────────────────────────────────────────────────────────┘
                               │ HTTP/Axios
                               ▼
┌─────────────────────────────────────────────────────────────────┐
│                        BACKEND (FastAPI)                        │
│  ┌─────────────────────────────────────────────────────────┐    │
│  │                    API Endpoints                        │    │
│  │  GET  /api/equations    - Liste des équations          │    │
│  │  GET  /api/equation/{id} - Équation par ID              │    │
│  │  POST /api/validate     - Valider coefficients          │    │
│  │  POST /api/hint          - Générer indice LLM           │    │
│  │  GET  /api/health       - Health check                  │    │
│  └─────────────────────────────────────────────────────────┘    │
│                              │                                   │
│  ┌────────────────┐  ┌─────────────────┐  ┌─────────────────┐  │
│  │ ChemistryService│  │ MockLLMService  │  │  Supabase (DB)  │  │
│  │                 │  │                 │  │                 │  │
│  │ - Validation    │  │ - Hints (15)    │  │  - Équations    │  │
│  │ - Atom parsing  │  │ - Success msgs  │  │  - Résultats    │  │
│  │ - Molecule parse│  │ - Advice        │  │  - Sessions     │  │
│  └────────────────┘  └─────────────────┘  └─────────────────┘  │
└─────────────────────────────────────────────────────────────────┘
```

### 2.2 Stack Technologique

#### Frontend
| Technologie | Version | Usage |
|-------------|---------|-------|
| **React** | 18.x | Framework UI principal |
| **Vite** | 5.x | Build tool et dev server |
| **react-katex** | 3.x | Rendu LaTeX des formules chimiques |
| **axios** | 1.x | Client HTTP pour API |
| **CSS** | - | Styling (custom CSS) |

#### Backend
| Technologie | Version | Usage |
|-------------|---------|-------|
| **Python** | 3.11+ | Langage principal |
| **FastAPI** | 0.115+ | Framework API REST |
| **Pydantic** | 2.10+ | Validation des données |
| **Uvicorn** | 0.34+ | ASGI server |
| **Supabase** | - | Base de données (préparé pour production) |

#### Infrastructure
| Technologie | Usage |
|-------------|-------|
| **Docker** | Conteneurisation |
| **Docker Compose** | Orchestration multi-conteneurs |

---

## 3. STRUCTURE DU PROJET

```
chem-balancer/
├── backend/
│   ├── app/
│   │   ├── __init__.py
│   │   ├── main.py              # Point d'entrée FastAPI
│   │   ├── config.py            # Configuration
│   │   ├── api/
│   │   │   ├── __init__.py
│   │   │   └── endpoints.py     # Routes API (5 endpoints)
│   │   ├── models/
│   │   │   ├── __init__.py
│   │   │   └── chemistry.py     # Classes Atom, Molecule, ChemicalEquation
│   │   ├── schemas/
│   │   │   ├── __init__.py
│   │   │   └── schemas.py       # Pydantic models (EquationInput, etc.)
│   │   └── services/
│   │       ├── __init__.py
│   │       ├── chemistry_service.py  # Logique de validation
│   │       ├── llm_service.py        # Interface OpenAI
│   │       └── mock_llm_service.py   # LLM simulé (744 lignes)
│   ├── requirements.txt
│   ├── Dockerfile
│   └── .env.example
│
├── frontend/
│   ├── src/
│   │   ├── main.jsx             # Entry point React
│   │   ├── App.jsx              # Composant principal (368 lignes)
│   │   ├── index.css            # Styles globaux
│   │   ├── components/
│   │   │   ├── Header.jsx               # En-tête avec progression
│   │   │   ├── ExerciseInterface.jsx    # Interface d'exercice
│   │   │   ├── FeedbackPanel.jsx       # Panneau de feedback
│   │   │   ├── HintSelector.jsx        # Sélecteur niveau d'indice
│   │   │   └── chemistry/
│   │   │       └── MoleculeDisplay.jsx # Rendu KaTeX
│   │   └── services/
│   │       └── api.js           # Client Axios
│   ├── package.json
│   ├── vite.config.js
│   └── index.html
│
├── docker-compose.yml
├── README.md
├── .gitignore
└── plans/
    └── plan.md
```

---

## 4. DESCRIPTION DÉTAILLÉE DES COMPOSANTS

### 4.1 BACKEND

#### 4.1.1 `backend/app/models/chemistry.py` (172 lignes)

**Classes définies :**

| Classe | Attributs | Méthodes | Rôle |
|--------|-----------|----------|------|
| `Atom` | `symbol` (str), `count` (int) | `__repr__()` | Représente un atome individuel |
| `Molecule` | `formula` (str), `atoms` (dict), `coefficient` (int) | `parse_formula()`, `get_total_atoms()` | Représente une molécule avec ses atomes |
| `ChemicalEquation` | `reactants` (list), `products` (list) | `is_balanced()`, `validate()` | Représente une équation complète |

**Fonction `parse_formula()` :**
- Parse les formules chimiques simples : `H2O` → `{H: 2, O: 1}`
- Gère les parenthèses imbriquées : `Fe2(SO4)3` → `{Fe: 2, S: 3, O: 12}`
- Utilise une fonction récursive interne `parse_group()`

**Fonction `is_balanced()` :**
- Applique la loi de conservation de Lavoisier
- Retourne `True` si tous les atomes sont équilibrés

#### 4.1.2 `backend/app/schemas/schemas.py`

**Schémas Pydantic :**

| Schéma | Champs | Usage |
|--------|--------|-------|
| `MoleculeInput` | `formula`, `coefficient` | Entrée d'une molécule |
| `EquationInput` | `reactants`, `products` | Équation à valider |
| `ValidationResponse` | `balanced`, `message`, `errors` | Résultat validation |
| `HintRequest` | `equation`, `user_level`, `current_attempt`, `error_detail` | Demande d'indice |
| `HintResponse` | `hint`, `hint_level` | Réponse avec indice |
| `EquationResponse` | `id`, `formula`, `reactants`, `products`, `solution`, `difficulty` | Équation complète |

#### 4.1.3 `backend/app/services/chemistry_service.py`

**Classe `ChemistryService` :**

| Méthode | Paramètres | Retour | Description |
|---------|-------------|--------|-------------|
| `validate_equation()` | `reactants`, `products` | `ValidationResponse` | Valide l'équation complète |
| `count_atoms()` | `molecules` | `dict` | Compte les atomes |
| `check_balance()` | `reactant_counts`, `product_counts` | `list[dict]` | Trouve les déséquilibres |

**Logique de validation :**
1. Parse chaque molécule pour extraire les atomes
2. Multiplie par le coefficient
3. Compare les totaux réactifs vs produits
4. Retourne les erreurs spécifiques par élément

#### 4.1.4 `backend/app/services/mock_llm_service.py` (744 lignes)

**Contenu :**

| Section | Lignes | Description |
|---------|--------|-------------|
| `MOCK_HINTS` | 6-600 | 15 indices détaillés (5 équations × 3 niveaux) |
| `MOCK_SUCCESS` | 600-650 | 5 messages de succès détaillés |
| `MockLLMService` | 650-744 | Classe avec méthodes `get_hint()`, `get_success_message()`, `get_llm_advice()` |

**Structure des indices :**

```python
MOCK_HINTS = {
    equation_id: {
        1: "Indice vague - orientation générale...",
        2: "Indice moyen - pointer vers l'élément...",
        3: "Indice précis - explication complète..."
    }
}
```

**Exemple d'indice niveau 3 (H2 + O2 → H2O) :**
- Explication de la loi de Lavoisier
- Comptage détaillé des atomes
- Étapes pas à pas de la méthode
- Réponse finale avec coefficients

#### 4.1.5 `backend/app/api/endpoints.py` (149 lignes)

**Endpoints définis :**

| Méthode | Endpoint | Description |
|---------|----------|-------------|
| `GET` | `/api/equations` | Liste toutes les équations (filtre optionnel par difficulty) |
| `GET` | `/api/equation/{id}` | Récupère une équation par ID |
| `POST` | `/api/validate` | Valide les coefficients d'une équation |
| `POST` | `/api/hint` | Génère un indice LLM (avec hint_level en query param) |
| `GET` | `/api/health` | Vérifie que l'API est opérationnelle |

**Banque d'équations (5 équations) :**

| ID | Équation | Solution | Difficulté |
|----|----------|----------|-------------|
| 1 | H₂ + O₂ → H₂O | [2, 1, 2] | débutant |
| 2 | Fe + S → FeS | [1, 1, 1] | débutant |
| 3 | CH₄ + O₂ → CO₂ + H₂O | [1, 2, 1, 2] | intermédiaire |
| 4 | N₂ + H₂ → NH₃ | [1, 3, 2] | intermédiaire |
| 5 | Fe₂O₃ + CO → Fe + CO₂ | [1, 3, 2, 3] | avancé |

#### 4.1.6 `backend/app/main.py`

**Point d'entrée FastAPI :**

```python
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.endpoints import router

app = FastAPI(title="Chem-Balancer API")

# CORS pour permettre le frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router)
```

---

### 4.2 FRONTEND

#### 4.2.1 `frontend/src/App.jsx` (368 lignes)

**État de l'application :**

| État | Type | Usage |
|------|------|-------|
| `currentEquation` | object | Équation affichée actuellement |
| `equations` | array | Liste de toutes les équations |
| `currentIndex` | number | Index de l'équation actuelle |
| `feedback` | object | Message de feedback (success/error/hint) |
| `stats` | object | `{solved, total, correct, errors}` |
| `hintLevel` | number | Niveau d'indice actuel (1-3) |
| `showSuccessModal` | boolean | Affiche modal de succès |
| `showResults` | boolean | Affiche écran de résultats |
| `sessionResults` | array | Historique des tentatives |

**Fonctions principales :**

| Fonction | Description |
|----------|-------------|
| `loadEquations()` | Charge les équations depuis l'API |
| `handleValidate()` | Valide les coefficients saisis |
| `handleHintRequest()` | Demande un indice au backend |
| `handleNextEquation()` | Passe à l'équation suivante |
| `handleRestart()` | Redémarre la session |
| `getLLMAdvice()` | Génère les conseils finaux |

**Flux utilisateur :**
1. L'étudiant voit une équation à équilibrer
2. Il saisit les coefficients dans les champs
3. Il peut demander un indice (niveau 1, 2 ou 3)
4. L'indice s'affiche avec explication du LLM
5. L'étudiant soumet sa réponse
6. Si correct → message de succès → next
7. Si incorrect → erreur détaillée → bouton "Passer à la suivante"
8. Après 5 équations → écran de résultats avec conseils

#### 4.2.2 `frontend/src/components/ExerciseInterface.jsx` (138 lignes)

**Rôle :** Interface principale d'exercice

**Sous-composants utilisés :**
- `EquationDisplay` - Affiche l'équation avec coefficients
- `HintSelector` - Sélecteur de niveau d'indice
- `FeedbackPanel` - Affiche les messages

**État local :**

| État | Type | Description |
|------|------|-------------|
| `coefficients` | array | Coefficients saisis par l'étudiant |
| `selectedHintLevel` | number | Niveau d'indice sélectionné |
| `hasRequestedHint` | boolean | Si un indice a été demandé |

**Nouveau flux (après modification) :**
1. L'étudiant voit le HintSelector en premier
2. Il choisit le niveau d'indice (1, 2 ou 3)
3. L'indice s'affiche automatiquement
4. L'équation est automatiquement validée
5. Feedback affiché

#### 4.2.3 `frontend/src/components/HintSelector.jsx` (34 lignes)

**Options d'indices :**

| Niveau | Titre | Description |
|--------|-------|-------------|
| 1 | Indice vague | "Orientation générale" |
| 2 | Indice moyen | "Pointer vers l'élément" |
| 3 | Indice précis | "Explication de la méthode" |

**Rendu :** 3 boutons horizontaux avec style visuel différent

#### 4.2.4 `frontend/src/components/FeedbackPanel.jsx` (29 lignes)

**Types de feedback :**

| Type | Couleur | Usage |
|------|---------|-------|
| `success` | Vert | Équation correctement équilibrée |
| `error` | Rouge | Équation mal équilibrée |
| `hint` | Jaune | Indice du tuteur LLM |
| `info` | Bleu | Information générale |

**Structure :**
```jsx
<div className="feedback-panel {type}">
  <div className="feedback-header">
    <span>{icon}</span>
    <span>{title}</span>
  </div>
  <div className="feedback-content">
    {children}
  </div>
</div>
```

#### 4.2.5 `frontend/src/components/chemistry/MoleculeDisplay.jsx` (85 lignes)

**Fonction `formulaToLatex()` :**
- Convertit `H2O` → `H_2O`
- Convertit `Fe2(SO4)3` → `Fe_2(SO_4)_3`
- Utilise des regex pour le parsing

**Composants exportés :**

| Composant | Props | Description |
|-----------|-------|-------------|
| `MoleculeDisplay` | `formula`, `coefficient`, `showCoefficient` | Affiche une molécule |
| `EquationDisplay` | `reactants`, `products`, `coefficients` | Affiche l'équation complète |

**Rendu KaTeX :**
- Utilise `InlineMath` de react-katex
- Affiche les coefficients en exposant
- Format professionnel style article scientifique

#### 4.2.6 `frontend/src/services/api.js` (60 lignes)

**Configuration Axios :**
```javascript
const API_URL = import.meta.env.VITE_API_URL || 'http://localhost:8000'
```

**Méthodes de l'API :**

| Méthode | Endpoint | Description |
|---------|----------|-------------|
| `getEquations(level)` | `GET /api/equations` | Liste des équations |
| `getEquation(id)` | `GET /api/equation/{id}` | Une équation |
| `validateEquation(eq)` | `POST /api/validate` | Validation |
| `getHint(request, level)` | `POST /api/hint` | Indice LLM |
| `healthCheck()` | `GET /api/health` | Health check |

#### 4.2.7 `frontend/src/index.css`

**Sections CSS :**

| Section | Lignes | Description |
|---------|--------|-------------|
| Variables CSS | 1-50 | Couleurs, espacements |
| Reset | 50-100 | Styles de base |
| Layout | 100-200 | Container, cards |
| Header | 200-220 | En-tête |
| Exercise | 220-250 | Interface d'exercice |
| Feedback Panel | 250-280 | Messages de feedback |
| Hint Selector | 280-320 | Sélecteur d'indice |
| Results | 320-380 | Écran de résultats |
| Animations | 380-410 | Spinner, transitions |

**Couleurs utilisées :**

| Couleur | Hex | Usage |
|---------|-----|-------|
| Primary | #3b82f6 | Boutons, liens |
| Success | #22c55e | Feedback positif |
| Error | #ef4444 | Feedback négatif |
| Warning | #f59e0b | Indices |
| Background | #f8fafc | Fond |
| Text | #1e293b | Texte principal |

---

## 5. FONCTIONNALITÉS DÉTAILLÉES

### 5.1 Équilibrage d'Équations

**Processus :**

1. L'étudiant voit l'équation non équilibrée
2. Il entre les coefficients pour chaque molécule
3. Le système parse les formules chimiques
4. Le moteur vérifie la conservation des atomes
5. Retourne succès ou erreur détaillée

**Exemple :**

```
Équation: H₂ + O₂ → H₂O
Entrée:   1   1    1

Vérification:
- Réactifs: H=2, O=2
- Produits: H=2, O=1
- ERREUR: Oxygène déséquilibré (2 vs 1)

Suggestion: 2H₂ + O₂ → 2H₂O
```

### 5.2 Système d'Indices

**3 niveaux de détail :**

| Niveau | Contenu |
|--------|---------|
| 1 (Vague) | Rappel de la loi de Lavoisier, question ouverte |
| 2 (Moyen) | Comptage des atomes, identification du problème |
| 3 (Précis) | Méthode complète, étapes détaillées, réponse |

**Flux :**
1. Étudiant clique sur un niveau
2. Backend récupère l'indice pré-défini
3. Affichage dans le FeedbackPanel
4. Auto-validation après l'indice

### 5.3 Tuteur LLM Simulé

**Réponses pré-définies pour chaque combinaison :**
- 5 équations × 3 niveaux = 15 indices
- 5 messages de succès détaillés
- Conseils personnalisés selon les résultats

**Style des réponses :**
- Ton pédagogique et encourageant
- Questions pour guider la réflexion
- Explications step-by-step
- Réponses de 500-1000+ mots

### 5.4 Écran de Résultats

**Affiché après les 5 équations :**

| Métrique | Description |
|----------|-------------|
| Score | X/5 équations correctes |
| Pourcentage | X% de réussite |
| Temps | Durée de la session |

**Analyse des erreurs :**
- Identification de l'élément le plus problématique
- Conseils personnalisés selon le niveau

**Conseils LLM :**

| Score | Conseil |
|-------|---------|
| ≥80% | "Excellent ! Vous maîtrisez bien..." |
| 50-79% | "Bon début ! Attention à..." |
| <50% | "Ne vous découragez pas ! Revoyez..." |

### 5.5 Navigation

**Bouton "Passer à la prochaine" :**
- Affiché uniquement après une erreur
- Permet de continuer sans bloquer
- Les résultats sont quand même enregistrés

---

## 6. BASE DE DONNÉES (Supabase)

### 6.1 Structure préparée

Pour la version production, les tables suivantes seraient utilisées :

| Table | Description |
|-------|-------------|
| `equations` | Banque d'équations (id, formula, solution, difficulty) |
| `sessions` | Sessions d'étudiants (id, started_at, completed_at) |
| `attempts` | Tentatives (session_id, equation_id, coefficients, correct) |
| `hints_used` | Indices utilisés (attempt_id, hint_level) |

### 6.2 Prototype actuel

Le prototype utilise une banque d'équations en mémoire (`EQUATIONS_DB` dans `endpoints.py`) pour simplifier le déploiement.

---

## 7. API REST

### 7.1 Endpoints

| Méthode | URL | Corps | Réponse |
|---------|-----|-------|---------|
| `GET` | `/api/equations` | - | `EquationResponse[]` |
| `GET` | `/api/equation/1` | - | `EquationResponse` |
| `POST` | `/api/validate` | `EquationInput` | `ValidationResponse` |
| `POST` | `/api/hint?hint_level=2` | `HintRequest` | `HintResponse` |
| `GET` | `/api/health` | - | `{status: "ok"}` |

### 7.2 Exemple de validation

**Request :**
```json
{
  "reactants": [
    {"formula": "H_2", "coefficient": 2},
    {"formula": "O_2", "coefficient": 1}
  ],
  "products": [
    {"formula": "H_2O", "coefficient": 2}
  ]
}
```

**Response :**
```json
{
  "balanced": true,
  "message": "L'équation est correctement équilibrée !",
  "errors": []
}
```

---

## 8. DOCKER

### 8.1 Services

| Service | Image | Ports |
|---------|-------|-------|
| `backend` | Dockerfile local | 8000 |
| `frontend` | node:20-alpine | 5173 |

### 8.2 Lancement

```bash
docker-compose up --build
```

---

## 9. INSTALLATION ET DÉMARRAGE

### 9.1 Méthode Python (sans Docker)

```bash
# Backend
cd backend
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python -c "import uvicorn; uvicorn.run('app.main:app', host='0.0.0.0', port=8000)"

# Frontend (autre terminal)
cd frontend
npm install
npm run dev
```

### 9.2 Méthode Docker

```bash
docker-compose up --build
```

---

## 10. LIENS UTILES

- **Repo GitHub :** https://github.com/othmanebenbakhta97-png/Chem-Balancer---DIC9340-30
- **Frontend :** http://localhost:5173
- **API Docs :** http://localhost:8000/docs

---

## 11. AMÉLIORATIONS POSSIBLES

| Amélioration | Description |
|--------------|-------------|
| Authentification | Connexion étudiants/professeurs |
| Base de données | Migration vers Supabase |
| Plus d'équations | Banque plus complète |
| Mode compétition | Classement des étudiants |
| Analytics | Suivi des progrès |
| Intégration OpenAI | Vrai LLM au lieu du simulé |

---

*Document généré pour le projet DIC9340 - Hiver 2026*