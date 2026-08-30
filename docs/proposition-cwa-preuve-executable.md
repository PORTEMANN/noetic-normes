# Proposition d'atelier CEN-CENELEC (CWA)

**« Exécutable evidence for high-risk AI performance claims »**
*(Preuve exécutable pour les affirmations de performance des systèmes d'IA à haut risque)*

**Version 0.1 — 31 août 2026 — direction D2 du registre N1 (noetic-normes)**
**Proposant : Patrice Portemann, écosystème Noetic Physics**

---

## 1. Contexte et justification

L'article 15 du règlement (UE) 2024/1689 (AI Act) exige des systèmes d'IA
à haut risque « un niveau approprié d'exactitude, de robustesse et de
cybersécurité » — mesuré et déclaré. Les projets prEN en rédaction
(CEN-CENELEC JTC 21) définissent actuellement les formats de preuve.

Fait mesuré (recherche multi-agents, 31/08/2026, 12 dimensions) : la
preuve de performance algorithmique est aujourd'hui **documentaire**
(registres, logs, cartographies), jamais **exécutable** — aucun artefact
de performance publié au niveau industriel ou normatif n'est livré avec
un test rejouable qui le falsifie. La seule occurrence identifiée de
falsification exécutable (POPPER, ICML 2025) est un prototype non adopté.

Fenêtre : obligations reportées au 2 décembre 2027 / 2 août 2028
(règlement (UE) 2026/1744) ; normes harmonisées en rédaction ; aucune
citée au JOUE. La définition du format de preuve se joue maintenant.

## 2. Objet (scope)

L'atelier produira un **format de preuve exécutable pour les affirmations
de performance des systèmes d'IA à haut risque**, défini comme le
quintuplet :

1. **protocole gelé** (π) — paramètres, attentes chiffrées, critères,
   écrits avant exécution ;
2. **verdict conjoint (V, Σ)** — l'affirmation et sa stabilité mesurée
   par perturbation déclarée du protocole (plan factoriel axial, une
   coordonnée à la fois) ;
3. **falsifieur exécutable** — le test déposé dont le succès réfute
   l'affirmation ;
4. **empreinte** (SHA-256) de chaque artefact, chaînée sur l'ensemble
   publié ;
5. **registre des limites mesurées** — chaque limite connue : énoncé,
   statut, coût de fermeture exact, falsifieur.

Domaine : tâches de classification, détection, diagnostic à haut risque.
Hors domaine : génération de contenu, systèmes à optimisation continue.

## 3. Livrables

| # | Livrable | Échéance |
|---|---|---|
| L1 | Spécification du format (définitions, exigences SHALL, méthodes d'essai rejouables) — base : ASH-MACH v0.1 (`specs/ash-mach-0.1.md`) | M+3 |
| L2 | Deux cas d'application exécutés : (a) instrument spectral à verdict (ASH, O(1) par fenêtre mesuré) ; (b) safety case avec certificat de minimalité calculé (forme Lévy–Desplanques) | M+5 |
| L3 | Guide d'alignement avec l'art. 15 et les prEN JTC 21 en cours (robustesse, journalisation, documentation) | M+6 |

## 4. Calendrier prévisionnel

| Jalon | Contenu | Cible |
|---|---|---|
| J0 | Constitution du groupe (ouvert à tout acteur, y compris petits) | 2027-T1 |
| J1 | Revue du format v0.1 + adoption du périmètre | 2027-T1 |
| J2 | Exécution des deux cas + publication intermédiaire | 2027-T2 |
| J3 | Vote du CWA et dépôt | 2027-T3 |

## 5. Cas de référence vivant (preuve d'exécution publique)

Le corpus `noetic-machine-complete` (public) applique déjà le format :
20 frontières au registre avec falsifieurs exécutables, stabilité Σ
mesurée par perturbation (batteries A1/A1b exécutées), chaîne SHA-256
sur 371 artefacts + release, échecs publiés (B3-FAIL) : F9 (intégrande
défectueuse réparée), M1 (postulat central réfuté avec inversion), P44
(réfutation de la lecture EEG en essai unique). L'atelier ne part pas
d'un texte : il part d'un système qui tourne.

## 6. Parties intéressées sollicitées

Laboratoires nationaux de métrologie (PTB/DAkkS ou délégation française),
intégrateurs d'instruments à verdict (monitoring embarqué), organismes
d'audit IA (conformité art. 9–15), utilisateurs industriels (ferroviaire,
énergie, médical), AFNOR (délégation nationale).

## 7. Propriété intellectuelle

Les spécifications produites seront publiées sous licence ouverte (MIT ou
équivalent). Les cas de référence sont déjà publics sous MIT.

## 8. Falsifieur de la proposition (discipline B3-FAIL)

Si l'atelier n'aboutit pas ou si la proposition est refusée, le refus est
publié tel quel dans le registre N1. Deux refus consécutifs ferment la
voie D2 — documentée, pas persévérée en silence.
