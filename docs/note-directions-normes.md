# Écrire des normes avec la Machine Noétique — directions stratégiques

**Patrice Portemann — 31 août 2026**
*Note de planification fondée sur la recherche multi-agents du 31/08/2026
(12 dimensions, ~300 requêtes — `rarete_rapport`) et sur l'état publié du
corpus (P0–P45, série A, série M, registre de 20 frontières).*

---

## 1. Point de départ mesuré

La recherche a établi trois faits qui fixent la stratégie :

1. **Le contenu épistémique de la machine n'a pas d'équivalent** : verdict
   avec domaine de validité mesuré, marge de stabilité Σ par perturbation
   du protocole, falsifieurs exécutables par artefact, zéro paramètre
   ajusté, échecs publiés, chaîne SHA-256. Le falsifieur exécutable est
   une frontière ouverte même dans la recherche (POPPER, ICML 2025, non
   adopté).
2. **La fenêtre est datée** : le Digital Omnibus (UE) 2026/1744 a reporté
   les obligations haut risque de l'AI Act (art. 9–15) au 2 décembre 2027
   (annexe III) / 2 août 2028 (annexe I) — vérifié sur EUR-Lex. Une seule
   norme harmonisée publiée (EN 18286, système de gestion), zéro citée au
   JOUE, zéro organisme notifié désigné, ~13 projets prEN en rédaction
   (CEN-CENELEC JTC 21).
3. **Le pont le moins cher n'est pas l'AI Act mais la métrologie légale** :
   OIML D 31:2023 couvre déjà le logiciel à ML dans les instruments (hash
   d'intégrité, audit trail) ; le Digital Calibration Certificate (DCC,
   PTB) normalise la traçabilité signée de l'incertitude. Ce canal parle
   déjà le langage de la machine (hash, traçabilité) — il n'y manque que
   le contenu du verdict.

Distinction stratégique à tenir : **substance** (inimitable aujourd'hui)
vs **forme** (QMS, documentation, fichiers de risque — copiable par tous,
à produire à bas coût). La stratégie consiste à écrire la substance dans
les normes pendant que la forme est encore liquide.

---

## 2. Ce que la machine offre à une norme (actifs réutilisables)

| Actif publié | Forme normative qu'il peut devenir |
|---|---|
| Couple verdict–stabilité (V, Σ), batterie PERT-BATT (A1/A1b) | Clause d'essai : « toute affirmation de robustesse est livrée avec sa stabilité mesurée par perturbation déclarée du protocole » |
| Falsifieur exécutable par artefact (registre A4, 20 entrées) | Exigence : « chaque exigence de performance porte un test rejouable déposé » |
| Registre des frontières (statut, coût de fermeture exact, ddll) | Structure de fichier de risque : chaque limite connue est une entrée avec coût de fermeture et falsifieur |
| Chaîne SHA-256 complète (SHASUMS, 371 fichiers + release) | Intégrité — déjà alignée OIML D 31 / DCC |
| Métrologie de la liberté (série M2 : coûts mesurés, minimalité certifiée) | Arguments de complétude *calculés* pour safety cases (la forme d'argument absente des normes IEC 61508 / ISO 26262) |
| B3-FAIL (échecs publiés : F9, M1, P44, F16, F18) | Exigence de publication des limites mesurées (personne ne la pratique — dim03, dim12) |
| Doc technique chaîne ASH → M̂ (domaine de validité V1–V6) | Modèle de « domaine de validité mesuré » pour instruments à verdict |

---

## 3. Les six directions

### D1 — Étendre le Digital Calibration Certificate (canal prioritaire)

Le DCC (PTB, DAkkS) est un document XML signé qui porte la traçabilité et
l'incertitude d'un instrument. Direction : proposer un champ
**« verdict algorithmique »** — protocole gelé, domaine mesuré, falsifieur
exécutable, stabilité Σ, empreinte. C'est le seul canal où la chaîne
SHA-256 de la machine est déjà la norme, et où le contenu manquant est
exactement ce que la machine produit. Première action : un cas complet —
la chaîne ASH → M̂ publiée *comme* un DCC étendu auto-émis, rejouable,
servant de proposition concrète (on ne discute pas d'un format, on en
montre un).

### D2 — CEN Workshop Agreement (voie rapide, ouverte aux petits acteurs)

Le CWA est l'instrument de pré-normalisation rapide de CEN-CENELEC :
ouvert, léger, quelques mois. Objet proposé : **« Exécutable evidence for
high-risk AI performance claims »** — le format de preuve art. 15
(robustesse) *avant* que les prEN se figent. Le corpus est le cas de
référence vivant : 20 frontières, falsifieurs exécutables, réparations
publiées. Risque déclaré : si l'atelier n'aboutit pas, le refus est
publié (discipline B3-FAIL appliquée au plan lui-même).

### D3 — Entrer dans les projets prEN par la délégation nationale

Les projets CEN-CENELEC JTC 21 en rédaction (gestion des risques,
journalisation, biais, robustesse, conformité) se travaillent en
délégation nationale — en France via AFNOR. Direction : proposer deux
clauses précises, déjà exécutées dans le corpus : (i) la stabilité par
perturbation du protocole d'évaluation comme exigence de robustesse ;
(ii) le registre de limites mesurées comme structure de la documentation
annexe IV. Leur force : elles arrivent avec une preuve d'exécution
publique, pas avec un texte seul.

### D4 — OIML / WELMEC : la catégorie « instrument à verdict algorithmique »

OIML D 31 (logiciel des instruments légaux, ML inclus) et WELMEC 7.2
encadrent le logiciel de mesure. Direction : proposer que les instruments
à verdict (classifieurs embarqués, monitoring) portent, comme les
instruments physiques, une **fiche de domaine mesuré** — résolution
effective, train minimal d'événements, stabilité — le modèle V1–V6 du
document technique ASH → M̂ est prêt à servir de gabarit.

### D5 — La norme miniature auto-appliquée (preuve par l'exemple)

Publier la spécification ouverte **ASH-MACH** (protocoles gelés du corpus
présentés comme une mini-norme : définitions, conditions de validité,
essais, falsifieurs, format de registre) et l'appliquer à un safety case
pilote complet — une tâche de détection avec certificat de minimalité
calculé (forme M2e : « la tâche exige n voies indépendantes, voici la
preuve rejouable »). Une norme qu'on peut lire *et exécuter*.

### D6 — Table de conformité AI Act publiée

Cartographier publiquement les artefacts du corpus sur les articles 9–15
(gestion des risques = registre des frontières ; données = D figées ;
documentation = notes SHA-chaînées ; robustesse = PERT-BATT ; supervision
= le verdict qui refuse quand Σ chute). Effet : quand les obligations
entreront en vigueur (déc. 2027), la machine aura déjà publié *sa* lecture
conforme — et tout écart découvert sera publié en addendum.

---

## 4. Séquence

| Horizon | Actions |
|---|---|
| T4 2026 | D5 (spécification ASH-MACH + safety case pilote) ; D6 (table de conformité publiée) — les deux sont entièrement internes, zéro dépendance externe |
| T1 2027 | D1 (cas DCC étendu, contact communauté métrologie légale) ; D3 (contact AFNOR / JTC 21 avec les deux clauses exécutées) |
| T1–T2 2027 | D2 (dépôt du CWA) ; D4 (proposition OIML/WELMEC adossée au cas D1) |
| T3 2027 → déc. 2027 | Itérations normatives ; publication de chaque refus ou échec (B3-FAIL du plan) |

## 5. Falsifieurs du plan lui-même

Conformément à la discipline du corpus, ce plan porte ses propres tests
tuables : (i) si la spécification ASH-MACH publiée n'est rejouée par
personne en six mois → la voie D5 est réfutée telle quelle ; (ii) si un
concurrent publie un falsifieur exécutable par artefact → la rareté
mesurée le 31/08/2026 tombe, et cette note reçoit un addendum ;
(iii) si les clauses proposées aux prEN sont rejetées deux fois → la
direction D3 est documentée comme fermée, pas persévérée en silence.

*Rien dans ce plan n'est une promesse : chaque direction a sa mesure, son
échéance et son falsifieur.*
