"""Service LLM simulé pour la démonstration - réponses détaillées comme ChatGPT/Gemini."""

from typing import Optional

# Réponses très détaillées pour les indices par équation et niveau
MOCK_HINTS = {
    1: {  # H2 + O2 -> H2O
        1: """Bonjour ! Je suis ton tuteur en chimie. 👋

Tu travailles sur l'équation de formation de l'eau : H₂ + O₂ → H₂O

La première chose à retenir est la **loi de conservation de la masse** formulée par Lavoisier en 1789 : "Rien ne se perd, rien ne se crée, tout se transforme."

Cela signifie que dans une équation chimique, le nombre total d'atomes de chaque élément doit être IDENTIQUE des deux côtés de la flèche (→).

Commençons par compter les atomes dans ta proposition actuelle :
- Côté réactifs (gauche) : tu as tes réactifs
- Côté produits (droite) : tu as ce qui est produit

**Question pour t'aider :** Peux-tu me dire combien d'atomes d'hydrogène (H) et d'oxygène (O) tu vois actuellement de chaque côté ? Ne te préoccupe pas encore des coefficients, compte juste les atomes dans les formules telles qu'elles sont écrites.""",

        2: """Très bien, tu commences à comprendre ! 📊

Laisse-moi t'expliquer plus en détail ce qui se passe.

Dans H₂ (une molécule de dihydrogène), tu as :
- 2 atomes d'hydrogène (H)

Dans O₂ (une molécule de dioxygène), tu as :
- 2 atomes d'oxygène (O)

Dans H₂O (une molécule d'eau), tu as :
- 2 atomes d'hydrogène (H)
- 1 atome d'oxygène (O)

Maintenant, si on compte sans coefficients :
- Côté réactifs : 2 atomes H + 0 atomes O = 2H, 2O
- Côté produits : 2 atomes H + 1 atome O = 2H, 1O

**Tu vois le problème ?** Il y a un déséquilibre en oxygène ! Il y a 2 atomes O à gauche mais seulement 1 à droite.

**Question :** Selon toi, comment pourrait-on corriger ce déséquilibre en oxygène ? Pense à multiplier les molecules par un coefficient...""",

        3: """Excellent ! Tu es sur la bonne voie ! 🌟

Laisse-moi t'expliquer la méthode complète pour équilibrer cette équation.

**Étape 1 : Comprendre la structure**
- H₂O contient 2 atomes H et 1 atome O
- Pour avoir 2 atomes O à droite (comme à gauche), il faut 2 molecules d'eau
- Cela donnerait : H₂ + O₂ → 2H₂O

**Étape 2 : Vérifier l'hydrogène**
- Côté gauche : 2 atomes H (dans H₂)
- Côté droit : 2 × 2 = 4 atomes H (dans 2H₂O)
- OH NON ! Il y a 4 H à droite mais seulement 2 à gauche !

**Étape 3 : Ajuster les coefficients**
- Pour avoir 4 atomes H à gauche, on multiplie H₂ par 2
- Cela donne : 2H₂ + O₂ → 2H₂O

**Étape 4 : Vérification finale**
- Gauche : 2×2 = 4 atomes H, 2×2 = 4 atomes O
- Droite : 2×2 = 4 atomes H, 2×1 = 2 atomes O
- Euh... il y a encore un problème avec l'oxygène !

**Étape 5 : Correction finale**
- Il faut 2 O à droite et on a 2H₂O qui donne 2×1 = 2 O ✓
- Il faut 4 H à gauche et on a 2H₂ qui donne 2×2 = 4 H ✓

**Réponse finale : 2H₂ + O₂ → 2H₂O**

Les coefficients sont : 2, 1, 2"""
    },
    2: {  # Fe + S -> FeS
        1: """Salut ! Bienvenue pour cet exercice sur la formation du sulfure de fer. 🔬

L'équation est : Fe + S → FeS

Cette réaction est une réaction de synthèse (ou combinaison) où le fer (Fe) réagit avec le soufre (S) pour former du sulfure de fer (FeS).

**Rappel important :** La loi de conservation de la masse nous dit que chaque atome présent au début doit se retrouver à la fin, rien ne disparaît et rien n'apparaît magiquement !

**Commençons par analyser :**

Dans cette équation, tu as trois substances :
- Fe (fer) : 1 atome de fer
- S (soufre) : 1 atome de soufre  
- FeS (sulfure de fer) : 1 atome de fer + 1 atome de soufre

**Question pour toi :** En regardant cette équation, peux-tu me dire si le nombre d'atomes de fer et de soufre est le même des deux côtés ? Utilise la loi de conservation pour analyser...""",

        2: """Très bien, tu progresses ! 📈

Laisse-moi t'expliquer ce qui se passe dans cette réaction.

**Analyse atomique :**

**Côté réactifs (gauche de la flèche) :**
- Fe : 1 atome de fer (symbole Fe)
- S : 1 atome de soufre (symbole S)
- Total : 1 atome Fe, 1 atome S

**Côté produits (droite de la flèche) :**
- FeS : 1 atome Fe + 1 atome S = 1 atome Fe, 1 atome S

**Comparaison :**
- Fer (Fe) : 1 atome à gauche, 1 atome à droite ✓
- Soufre (S) : 1 atome à gauche, 1 atome à droite ✓

**Observation :** L'équation semble déjà équilibrée en nombre d'atomes !

Mais attends... il y a une subtilité ici. Quand on écrit Fe + S → FeS, le coefficient 1 est implicite devant chaque substance. En chimie, quand aucun coefficient n'est écrit, cela signifie que le coefficient est 1.

**Question :** Selon toi, quels seraient les coefficients stœchiométriques pour cette équation ? Pense à ce que signifie "équilibrer" une équation...""",

        3: """Parfait ! Tu mérites une explication complète. 🎓

**Explication détaillée de la réaction :**

Le fer (Fe) et le soufre (S) sont deux éléments chimiques qui peuvent réagir ensemble pour former un nouveau composé : le sulfure de fer (FeS). Cette réaction est exothermique et dégage de la chaleur.

**Analyse de l'équation non équilibrée :**
Fe + S → FeS

**Comptage des atomes :**
- Réactifs : 1 atome Fe, 1 atome S
- Produits : 1 atome Fe, 1 atome S

**Constatation :** L'équation est déjà parfaitement équilibrée !

**Pourquoi ?**
Parce que quand un atome de fer (Fe) réagit avec un atome de soufre (S), ils forment exactement une molécule de sulfure de fer (FeS), qui contient elle-même 1 atome Fe et 1 atome S.

**Les coefficients stœchiométriques sont donc :**
- Coefficient devant Fe : 1
- Coefficient devant S : 1
- Coefficient devant FeS : 1

**Équation équilibrée :**
1Fe + 1S → 1FeS

Ou plus simplement : Fe + S → FeS (puisque le coefficient 1 est implicite)

**C'est une équation simple où les coefficients sont tous égaux à 1 !**"""
    },
    3: {  # CH4 + O2 -> CO2 + H2O
        1: """Bienvenue ! Nous allons travailler sur la combustion du méthane. 🔥

L'équation est : CH₄ + O₂ → CO₂ + H₂O

C'est une réaction très importante ! La combustion du méthane est la réaction qui se produit quand on utilise le gaz naturel pour cuisiner ou se chauffer.

**La loi de conservation de la masse** nous dit que les atomes ne peuvent pas disparaître ou apparaître. Donc, le nombre de chaque type d'atome doit être le même des deux côtés.

**Analysons les substances :**

CH₄ (méthane) contient :
- 1 atome de carbone (C)
- 4 atomes d'hydrogène (H)

O₂ (dioxygène) contient :
- 2 atomes d'oxygène (O)

CO₂ (dioxyde de carbone) contient :
- 1 atome de carbone (C)
- 2 atomes d'oxygène (O)

H₂O (eau) contient :
- 2 atomes d'hydrogène (H)
- 1 atome d'oxygène (O)

**Question :** Peux-tu compter combien de C, H et O tu as de chaque côté actuellement (sans coefficients) ??""",

        2: """Tu avances bien ! Laisse-moi t'aider à visualiser le problème. 📊

**Comptage actuel des atomes (sans coefficients) :**

**Côté réactifs (gauche) :**
- Carbone (C) : 1 atome (dans CH₄)
- Hydrogène (H) : 4 atomes (dans CH₄)
- Oxygène (O) : 2 atomes (dans O₂)

**Côté produits (droite) :**
- Carbone (C) : 1 atome (dans CO₂)
- Hydrogène (H) : 2 atomes (dans H₂O)
- Oxygène (O) : 2 + 1 = 3 atomes (dans CO₂ et H₂O)

**Tableau comparatif :**
| Élément | Réactifs | Produits | Équilibré ? |
|---------|----------|----------|-------------|
| C       | 1        | 1        | ✓ Oui       |
| H       | 4        | 2        | ✗ Non (il en manque 2) |
| O       | 2        | 3        | ✗ Non (il y en a 1 de trop) |

**Problèmes identifiés :**
1. Il y a 4 atomes H à gauche mais seulement 2 à droite
2. Il y a 2 atomes O à gauche mais 3 à droite

**Piste de réflexion :**
- Pour l'hydrogène (H) : Si on avait 2×H₂O au lieu de 1×H₂O, on aurait 2×2 = 4 atomes H à droite ✓
- Pour l'oxygène (O) : Il faudrait alors ajuster aussi...

**Question :** Si on met un coefficient 2 devant H₂O, combien d'atomes O cela donnerait-il à droite ? Et que faudrait-il faire pour l'oxygène à gauche ?""",

        3: """Excellent travail ! Tu es prêt pour la solution complète. 🎓

**Méthode d'équilibrage pas à pas :**

**Étape 1 : Identifier le problème**
Tableau actuel (sans coefficients) :
| Élément | Réactifs | Produits | Différence |
|---------|----------|----------|------------|
| C       | 1        | 1        | 0 (OK)     |
| H       | 4        | 2        | -2 (manque 2) |
| O       | 2        | 3        | +1 (excès 1) |

**Étape 2 : Équilibrer le carbone (C)**
- C : 1 à gauche, 1 à droite → Déjà équilibré !
- Coefficient de CO₂ = 1 (pas de changement)

**Étape 3 : Équilibrer l'hydrogène (H)**
- H : 4 à gauche, 2 à droite
- Il faut multiplier H₂O par 2 pour avoir 2×2 = 4 atomes H à droite
- Nouveau coefficient de H₂O = 2

**Étape 4 : Recompter l'oxygène (O)**
Après avoir mis 2 devant H₂O :
- O à droite : CO₂ (2 O) + 2×H₂O (2×1 = 2 O) = 2 + 2 = 4 O
- O à gauche : 2 O (dans O₂)

Maintenant O est déséquilibré : 2 à gauche, 4 à droite

**Étape 5 : Équilibrer l'oxygène (O)**
- Il faut multiplier O₂ par 2 pour avoir 2×2 = 4 O à gauche
- Nouveau coefficient de O₂ = 2

**Étape 6 : Vérification finale**

**Côté réactifs :**
- C : 1 atome (dans CH₄)
- H : 4 atomes (dans CH₄)
- O : 2×2 = 4 atomes (dans 2O₂)

**Côté produits :**
- C : 1 atome (dans CO₂)
- H : 2×2 = 4 atomes (dans 2H₂O)
- O : 1×2 + 2×1 = 2 + 2 = 4 atomes (dans CO₂ et 2H₂O)

**Tableau final :**
| Élément | Réactifs | Produits | Équilibré ? |
|---------|----------|---------|-------------|
| C       | 1        | 1       | ✓ Oui       |
| H       | 4        | 4       | ✓ Oui       |
| O       | 4        | 4       | ✓ Oui       |

**Équation équilibrée finale :**
**CH₄ + 2O₂ → CO₂ + 2H₂O**

**Coefficients : 1, 2, 1, 2**"""
    },
    4: {  # N2 + H2 -> NH3
        1: """Salut ! Nous allons travailler sur la synthèse de l'ammoniac. 🧪

L'équation est : N₂ + H₂ → NH₃

Cette réaction est extrêmement importante dans l'industrie chimique ! C'est le processus Haber-Bosch qui permet de produire des engrais pour l'agriculture mondiale.

**La loi de conservation de la masse** nous rappelle que chaque atome doit se retrouver des deux côtés de l'équation.

**Analysons les substances :**

N₂ (diazote) contient :
- 2 atomes d'azote (N)

H₂ (dihydrogène) contient :
- 2 atomes d'hydrogène (H)

NH₃ (ammoniac) contient :
- 1 atome d'azote (N)
- 3 atomes d'hydrogène (H)

**Question pour toi :** Sans mettre de coefficients, combien d'atomes de chaque type (N et H) vois-tu de chaque côté de l'équation ? Fais un tableau comme on a fait précédemment...""",

        2: """Très bien, tu apprends vite ! 📈

Laisse-moi t'aider à visualiser le déséquilibre.

**Comptage actuel des atomes (sans coefficients) :**

**Côté réactifs (gauche) :**
- Azote (N) : 2 atomes (dans N₂)
- Hydrogène (H) : 2 atomes (dans H₂)

**Côté produits (droite) :**
- Azote (N) : 1 atome (dans NH₃)
- Hydrogène (H) : 3 atomes (dans NH₃)

**Tableau comparatif :**
| Élément | Réactifs | Produits | Différence |
|---------|----------|----------|------------|
| N       | 2        | 1        | -1 (manque 1) |
| H       | 2        | 3        | +1 (excès 1)  |

**Observations importantes :**

1. **Pour l'azote (N)** : Il y a 2 atomes N à gauche mais seulement 1 à droite. Il en manque 1 à droite.

2. **Pour l'hydrogène (H)** : Il y a 2 atomes H à gauche mais 3 à droite. Il y a 1 H de trop à droite.

**Stratégie d'équilibrage :**

Pour l'azote : Si on met un coefficient 2 devant NH₃, on aurait 2 atomes N à droite ✓

Mais attention ! Si on met 2 devant NH₃, alors on aurait aussi 2×3 = 6 atomes H à droite, ce qui aggraverait le déséquilibre de l'hydrogène...

**Question :** Si on met 2 devant NH₃, combien d'atomes H aurait-on à droite ? Et que faudrait-il faire pour l'hydrogène à gauche ? Pense à multiplier H₂ par un certain coefficient...""",

        3: """Parfait ! Tu es sur le point de comprendre ! Voici l'explication complète. 🎓

**Synthèse de l'ammoniac (NH₃) - Réaction de Haber**

**Étape 1 : Analyse initiale**

Tableau sans coefficients :
| Élément | Réactifs | Produits | Différence |
|---------|----------|---------|------------|
| N       | 2        | 1       | -1         |
| H       | 2        | 3       | +1         |

**Étape 2 : Stratégie d'équilibrage**

On commence par l'élément qui apparaît dans le moins de substances, ici l'azote (N).

Pour avoir 2 atomes N à droite (comme à gauche), on met un coefficient 2 devant NH₃ :
- N₂ + H₂ → 2NH₃

Maintenant, vérifions :
- N : 2 à gauche ✓, 2×1 = 2 à droite ✓
- H : 2 à gauche, 2×3 = 6 à droite ✗

Le carbone (H) est maintenant très déséquilibré : 2 à gauche, 6 à droite.

**Étape 3 : Équilibrer l'hydrogène**

Il faut 6 atomes H à gauche. Puisque H₂ contient 2 atomes par molécule, on met un coefficient 3 devant H₂ :
- N₂ + 3H₂ → 2NH₃

**Étape 4 : Vérification complète**

**Côté réactifs (gauche) :**
- N : 2 atomes (dans N₂)
- H : 3×2 = 6 atomes (dans 3H₂)

**Côté produits (droite) :**
- N : 2×1 = 2 atomes (dans 2NH₃)
- H : 2×3 = 6 atomes (dans 2NH₃)

**Tableau final :**
| Élément | Réactifs | Produits | Équilibré ? |
|---------|----------|---------|-------------|
| N       | 2        | 2       | ✓ Oui       |
| H       | 6        | 6       | ✓ Oui       |

**Équation équilibrée finale :**
**N₂ + 3H₂ → 2NH₃**

**Coefficients : 1, 3, 2**

**Interprétation :** 1 molécule de diazote réagit avec 3 molcules de dihydrogène pour produire 2 molicules d'ammoniac."""
    },
    5: {  # Fe2O3 + CO -> Fe + CO2
        1: """Bienvenue ! Nous abordons une réaction plus complexe : la réduction de l'oxyde de fer. ⚙️

L'équation est : Fe₂O₃ + CO → Fe + CO₂

Cette réaction est un exemple de réaction d'oxydoréduction. Le monoxyde de carbone (CO) agit comme agent réducteur et réduit l'oxyde de fer(III) en fer métallique.

**La loi de conservation de la masse** s'applique toujours : chaque atome doit se retrouver des deux côtés.

**Analysons les substances :**

Fe₂O₃ (oxyde de fer III) contient :
- 2 atomes de fer (Fe)
- 3 atomes d'oxygène (O)

CO (monoxyde de carbone) contient :
- 1 atome de carbone (C)
- 1 atome d'oxygène (O)

Fe (fer métallique) contient :
- 0 atomes de O, 1 atome de Fe

CO₂ (dioxyde de carbone) contient :
- 1 atome de carbone (C)
- 2 atomes d'oxygène (O)

**Question :** Peux-tu compter le nombre de Fe, O et C de chaque côté ?""",

        2: """Tu gères bien ! Laisse-moi t'aider à voir les déséquilibres. 📊

**Comptage actuel des atomes (sans coefficients) :**

**Côté réactifs (gauche) :**
- Fer (Fe) : 2 atomes (dans Fe₂O₃)
- Oxygène (O) : 3 (dans Fe₂O₃) + 1 (dans CO) = 4 atomes
- Carbone (C) : 1 atome (dans CO)

**Côté produits (droite) :**
- Fer (Fe) : 1 atome (dans Fe)
- Oxygène (O) : 2 atomes (dans CO₂)
- Carbone (C) : 1 atome (dans CO₂)

**Tableau comparatif :**
| Élément | Réactifs | Produits | Différence |
|---------|----------|----------|------------|
| Fe      | 2        | 1        | -1 (manque 1) |
| O       | 4        | 2        | -2 (manque 2) |
| C       | 1        | 1        | 0 (OK)     |

**Observations :**

1. **Fer (Fe)** : 2 atomes à gauche, seulement 1 à droite. Il en manque 1 à droite.

2. **Oxygène (O)** : 4 atomes à gauche, seulement 2 à droite. Il en manque 2 à droite !

3. **Carbone (C)** : Déjà équilibré (1 des deux côtés).

**Stratégie :**

Pour le fer : Si on met un coefficient 2 devant Fe, on aurait 2 atomes Fe à droite ✓

Pour l'oxygène : Il faut ajouter 2 atomes O à droite. Puisque CO₂ contient 2 O, on pourrait ajuster...

**Question :** Si on met 2 devant Fe et 2 devant CO₂, combien d'atomes de chaque type aurait-on ? Est-ce que ça équilibre ? Pense à ajuster aussi le CO...?""",

        3: """Excellent ! Voici l'explication détaillée de cette réaction d'oxydoréduction. 🎓

**Réduction de l'oxyde de fer(III) par le monoxyde de carbone**

**Étape 1 : Analyse initiale**

Tableau sans coefficients :
| Élément | Réactifs | Produits | Différence |
|---------|----------|---------|------------|
| Fe      | 2        | 1       | -1         |
| O       | 4        | 2       | -2         |
| C       | 1        | 1       | 0          |

**Étape 2 : Commencer par le fer (Fe)**

Pour avoir 2 atomes Fe à droite (comme à gauche), on met un coefficient 2 devant Fe :
- Fe₂O₃ + CO → 2Fe + CO₂

Vérification :
- Fe : 2 à gauche ✓, 2 à droite ✓
- O : 4 à gauche, 2 à droite ✗
- C : 1 à gauche, 1 à droite ✓

**Étape 3 : Équilibrer l'oxygène**

Il faut 4 atomes O à droite. CO₂ contient 2 O par molécule, donc :
- Il faut 2×CO₂ pour avoir 2×2 = 4 atomes O à droite
- Coefficient de CO₂ = 2

Maintenant : Fe₂O₃ + CO → 2Fe + 2CO₂

Vérification :
- Fe : 2 à gauche ✓, 2 à droite ✓
- O : 4 à gauche, 2×2 = 4 à droite ✓
- C : 1 à gauche, 2 à droite ✗

Oh non ! Le carbone est maintenant déséquilibré !

**Étape 4 : Équilibrer le carbone**

Il faut 2 atomes C à gauche. CO contient 1 C, donc :
- Il faut 2×CO pour avoir 2 atomes C à gauche
- Coefficient de CO = 2

Maintenant : Fe₂O₃ + 2CO → 2Fe + 2CO₂

**Étape 5 : Vérification finale**

**Côté réactifs (gauche) :**
- Fe : 2 atomes (dans Fe₂O₃)
- O : 3 (dans Fe₂O₃) + 2×1 (dans 2CO) = 3 + 2 = 5 atomes
- C : 2×1 = 2 atomes (dans 2CO)

**Côté produits (droite) :**
- Fe : 2 atomes (dans 2Fe)
- O : 2×2 = 4 atomes (dans 2CO₂)
- C : 2×1 = 2 atomes (dans 2CO₂)

**Tableau final :**
| Élément | Réactifs | Produits | Équilibré ? |
|---------|----------|---------|-------------|
| Fe      | 2        | 2       | ✓ Oui       |
| O       | 5        | 4       | ✗ Non       |

Attends, il y a une erreur ! Recomptons :
- O dans Fe₂O₃ = 3
- O dans 2CO = 2×1 = 2
- Total O gauche = 3 + 2 = 5

- O dans 2CO₂ = 2×2 = 4
- O total droit = 4

Il y a encore un déséquilibre ! Il faut 5 O à droite mais on n'a que 4...

**Étape 6 : Correction**

En fait, le fer dans Fe₂O₃ est du fer au degré d'oxydation +3, et il se réduit en fer métallique (degré 0). Chaque atome de fer gagne 3 électrons.

La bonne équation équilibrée est :
**Fe₂O₃ + 3CO → 2Fe + 3CO₂**

Vérifions :
- Fe : 2 à gauche ✓, 2 à droite ✓
- O : 3 (dans Fe₂O₃) + 3×1 (dans 3CO) = 3 + 3 = 6 à gauche
- O : 3×2 (dans 3CO₂) = 6 à droite ✓
- C : 3×1 = 3 à gauche ✓, 3×1 = 3 à droite ✓

**Équation équilibrée finale :**
**Fe₂O₃ + 3CO → 2Fe + 3CO₂**

**Coefficients : 1, 3, 2, 3**"""
    }
}

# Messages de succès détaillés
SUCCESS_MESSAGES = {
    1: """🎉 **Félicitations !** Tu as réussi à équilibrer l'équation de formation de l'eau !

**Équation équilibrée : 2H₂ + O₂ → 2H₂O**

**Explication :**
Tu as appliqué correctement la loi de conservation de la masse de Lavoisier. En mettant le coefficient 2 devant H₂ et H₂O, tu as ensured que le nombre d'atomes d'hydrogène (4) et d'oxygène (2) est identique des deux côtés de l'équation.

**Ce que tu as appris :**
- L'eau (H₂O) est formée par la combinaison de dihydrogène (H₂) et de dioxygène (O₂)
- Cette réaction libère de l'énergie (exothermique)
- La loi de conservation de la masse est fondamentale en chimie

**Application dans la vie réelle :**
Cette réaction est utilisée dans les piles à combustible pour produire de l'électricité propre, avec comme seul sous-produit... de l'eau !""",

    2: """🎉 **Excellent !** Tu as reconnu que l'équation Fe + S → FeS était déjà équilibrée !

**Équation : Fe + S → FeS**

**Explication :**
Dans cette réaction de synthèse, un atome de fer (Fe) se combine directement avec un atome de soufre (S) pour former une molécule de sulfure de fer (FeS). Puisque les coefficients sont tous égaux à 1, l'équation respecte naturellement la loi de conservation de la masse.

**Ce que tu as appris :**
- Les réactions de synthèse combinent deux ou plusieurs substances pour en former une nouvelle
- Le sulfure de fer est un composé ionique
- Parfois, les équations sont déjà équilibrées sans modification !

**Application dans la vie réelle :**
Le sulfure de fer se forme naturellement dans certains contextes géologiques et peut être trouvé dans des minerais.""",

    3: """🎉 **Bravo !** Tu as réussi à équilibrer l'équation de combustion du méthane !

**Équation équilibrée : CH₄ + 2O₂ → CO₂ + 2H₂O**

**Explication :**
La combustion complète du méthane produit du dioxyde de carbone (CO₂) et de l'eau (H₂O), en libérant beaucoup d'énergie. C'est exactement ce qui se passe quand tu utilises ton réchaud à gaz !

**Comptage final :**
- Carbone : 1 atome de chaque côté ✓
- Hydrogène : 4 atomes de chaque côté (1×4 = 2×2) ✓
- Oxygène : 4 atomes de chaque côté (2×2 = 1×2 + 2×1) ✓

**Ce que tu as appris :**
- La combustion complète produit CO₂ et H₂O
- La combustion incomplète produirait du monoxyde de carbone (toxique)
- Le méthane est le principal composant du gaz naturel

**Application dans la vie réelle :**
Cette réaction est la base du fonctionnement des chaudières, des chauffe-eau et des moteurs à gaz naturel.""",

    4: """🎉 **Très bien !** Tu as réussi la synthèse de l'ammoniac !

**Équation équilibrée : N₂ + 3H₂ → 2NH₃**

**Explication :**
C'est le célèbre processus Haber-Bosch, découvert au début du 20e siècle, qui a révolutionné l'agriculture mondiale en permettant la production d'engrais azotés à grande échelle.

**Comptage final :**
- Azote : 2 atomes de chaque côté (1×2 = 2×1) ✓
- Hydrogène : 6 atomes de chaque côté (3×2 = 2×3) ✓

**Ce que tu as appris :**
- Le processus Haber-Bosch nécessite des conditions de haute pression et température
- L'ammoniac est essentiel pour les engrais agricoles
- Cette découverte a permis de nourrir des milliards de personnes

**Application dans la vie réelle :**
Environ 80% de l'azote dans les engrais modernes provient de l'ammoniac synthétisé par ce procédé !""",

    5: """🎉 **Impressionnant !** Tu as réussi cette réaction d'oxydoréduction complexe !

**Équation équilibrée : Fe₂O₃ + 3CO → 2Fe + 3CO₂**

**Explication :**
C'est une réaction d'oxydoréduction où le monoxyde de carbone (CO) réduit l'oxyde de fer(III) en fer métallique. Le CO est oxydé en CO₂.

**Comptage final :**
- Fer : 2 atomes de chaque côté ✓
- Oxygène : 6 atomes de chaque côté (3 + 3×1 = 3×2) ✓
- Carbone : 3 atomes de chaque côté ✓

**Ce que tu as appris :**
- Le fer dans Fe₂O₃ a un degré d'oxydation de +3
- Le fer métallique a un degré d'oxydation de 0
- Le CO est un agent réducteur qui cède des électrons

**Application dans la vie réelle :**
Cette réaction est utilisée dans les hauts-fourneaux pour produire le fer et l'acier à partir des minerais !"""
}


class MockLLMService:
    """Service LLM simulé pour la démonstration - réponses détaillées."""
    
    @staticmethod
    def get_hint(equation_id: int, hint_level: int, user_level: str = "débutant") -> str:
        """
        Retourne un indice simulé très détaillé.
        
        Args:
            equation_id: ID de l'équation
            hint_level: Niveau de l'indice (1-3)
            user_level: Niveau de l'utilisateur (non utilisé en mode simulé)
            
        Returns:
            Texte de l'indice très détaillé
        """
        if equation_id in MOCK_HINTS:
            hints = MOCK_HINTS[equation_id]
            level = min(max(hint_level, 1), 3)
            return hints[level]
        
        # Fallback si l'équation n'est pas trouvée
        return f"""Indice niveau {hint_level} :

Selon la loi de conservation de la masse formulée par Lavoisier : "Rien ne se perd, rien ne se crée, tout se transforme."

Cela signifie que dans toute équation chimique équilibrée, le nombre total d'atomes de chaque élément doit être identique des deux côtés de la flèche (→).

Pour équilibrer une équation chimique, suis ces étapes :

1. **Identifie tous les éléments** présents dans l'équation
2. **Compte les atomes** de chaque élément des deux côtés (réactifs et produits)
3. **Trouve le déséquilibre** - quel élément a plus/moins d'atomes d'un côté
4. **Ajoute des coefficients** devant les formules pour équilibrer
5. **Vérifie** que tous les éléments sont équilibrés

Commence par l'élément qui apparaît dans le moins de substances, et termine par celui qui apparaît dans le plus de substances.

Si tu as besoin d'aide, n'hésite pas à demander un indice de niveau supérieur !"""
    
    @staticmethod
    def get_success_message(equation_id: int) -> str:
        """
        Retourne un message de succès très détaillé.
        
        Args:
            equation_id: ID de l'équation
            
        Returns:
            Message de succès détaillé
        """
        return SUCCESS_MESSAGES.get(equation_id, 
            "🎉 Bravo ! L'équation est correctement équilibrée ! Tu appliques parfaitement la loi de conservation de la masse.")
    
    @staticmethod
    def get_error_explanation(equation_id: int, errors: list) -> str:
        """
        Retourne une explication d'erreur détaillée.
        
        Args:
            equation_id: ID de l'équation
            errors: Liste des erreurs de déséquilibre
            
        Returns:
            Explication détaillée de l'erreur
        """
        if not errors:
            return """L'équation semble ne pas être équilibrée, mais analysons ensemble...

Peux-tu me montrer combien d'atomes de chaque élément tu as des deux côtés ? Je t'aide à faire le comptage correctement.

N'oublie pas :
- Les coefficients multiplient TOUS les atomes dans une formule
- Exemple : 2H₂O signifie 2 × (2 atomes H + 1 atome O) = 4 atomes H + 2 atomes O"""
        
        error_msgs = []
        for e in errors:
            elem = e.get("element", "inconnu")
            diff = e.get("difference", 0)
            reactant_count = e.get("reactant_count", 0)
            product_count = e.get("product_count", 0)
            
            if diff > 0:
                msg = f"""**{elem} ({diff} atome(s) en trop du côté des réactifs)**

Tu as {reactant_count} atome(s) de {elem} du côté des réactifs, mais seulement {product_count} du côté des produits.

Pour corriger, tu pourrais :
- Augmenter le coefficient des produits contenant {elem}, OU
- Diminuer le coefficient des réactifs contenant {elem} (si c'est possible)"""
            else:
                msg = f"""**{elem} ({abs(diff)} atome(s) en trop du côté des produits)**

Tu as {product_count} atome(s) de {elem} du côté des produits, mais seulement {reactant_count} du côté des réactifs.

Pour corriger, tu pourrais :
- Augmenter le coefficient des réactifs contenant {elem}, OU
- Diminuer le coefficient des produits contenant {elem}"""
            
            error_msgs.append(msg)
        
        return """**Analysons ton erreur ensemble :**\n\n""" + "\n\n".join(error_msgs) + """

N'hésite pas à demander un indice de niveau supérieur si tu as besoin de plus d'aide !"""
    
    @staticmethod
    def is_available() -> bool:
        """Le service simulé est toujours disponible."""
        return True


# Instance singleton
_mock_llm_service: Optional[MockLLMService] = None


def get_mock_llm_service() -> MockLLMService:
    """Retourne l'instance du service LLM simulé (singleton)."""
    global _mock_llm_service
    if _mock_llm_service is None:
        _mock_llm_service = MockLLMService()
    return _mock_llm_service