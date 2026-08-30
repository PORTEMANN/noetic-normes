# ASH-MACH — Spécification ouverte d'un opérateur de verdict à preuve exécutable

**Version 0.1 — 31 août 2026 — statut : proposition ouverte (pré-norme)**
**Auteur : Patrice Portemann — écosystème Noetic Physics**
**Dépôt de référence : `noetic-machine-complete` (corpus figé, 371 artefacts + release)**
**Falsifieur de la spécification : si elle n'est rejouée par aucun tiers en six mois, la voie D5 est réfutée et publiée telle quelle.**

---

## 1. Objet et domaine d'application

La présente spécification définit les exigences applicables à un
**opérateur de verdict** — une machine qui prend en entrée des données
mesurées et une structure candidate et produit un verdict assorti d'une
preuve exécutable — ainsi que les méthodes d'essai permettant de vérifier
la conformité à ces exigences.

Elle s'applique aux instruments et chaînes de traitement qui émettent des
affirmations mesurées (classification, détection de régime, diagnostic)
dans un contexte où la preuve doit être rejouable par un tiers
(métrologie, sûreté de fonctionnement, conformité réglementaire).

Elle ne s'applique pas à la métrologie d'amplitude absolue, ni aux
systèmes dont la tâche est l'optimisation continue (contrôle en boucle
fermée temps réel).

## 2. Références normatives (internes au corpus de référence)

| Référence | Objet |
|---|---|
| `noetic-machine-complete` | Corpus de référence (P0–P45, série A, série M) |
| registre A4 (REG-FR-1.0) | Format du registre des frontières (20 entrées) |
| PERT-BATT-1.0 (A1/A1b) | Batterie de perturbation de protocole |
| ASH-MACH-1.0 (P43) | Audit d'un instrument par l'opérateur (7/7) |
| série M2 (MÉT-LIB-1.x) | Métrologie de la liberté (coûts mesurés, minimalité certifiée) |

## 3. Termes et définitions

| Terme | Définition |
|---|---|
| **opérateur de verdict** M̂ | fonction (D, S, L, π) → (V, Σ) |
| **D** | données figées, d'origine déclarée, jamais ré-ajustées |
| **S** | structure candidate éprouvée (modèle, classifieur, instrument) |
| **L** | levier discriminant : suppression contrôlée du mécanisme |
| **π** | protocole, objet perturbable déclaré |
| **V** | verdict (booléen par composante + verdict global) |
| **Σ** | stabilité : fraction des protocoles perturbés préservant V |
| **falsifieur exécutable** | test rejouable dont le succès tue l'affirmation |
| **coût de fermeture** | mesure (en ddll) des degrés de liberté à ajouter pour clore une frontière |
| **B3-FAIL** | publication d'un échec avec le même soin qu'un succès |

## 4. Exigences

Les exigences sont formulées avec **DOIT** (shall). Chaque exigence porte
un identifiant et une méthode d'essai associée (§6).

**N1 — Zéro paramètre ajusté.** Tout nombre hors de D DOIT être dérivé
par une règle déclarée avant exécution. Aucun ajustement sur les données
de test n'est permis, y compris les seuils, coefficients de normalisation
et hyperparamètres.

**N2 — Protocole gelé et pré-enregistrement.** Le protocole (π) DOIT être
écrit avant la première exécution : paramètres, attentes chiffrées,
critères de verdict et falsifieurs. Toute modification ultérieure DOIT
prendre la forme d'un addendum daté qui conserve la version antérieure.

**N3 — Verdict conjoint (V, Σ).** L'opérateur DOIT produire, pour chaque
affirmation, le couple (verdict, stabilité). Un verdict livré sans sa
stabilité est non conforme.

**N4 — Stabilité par perturbation axiale.** Σ DOIT être mesurée par un
plan factoriel axial déclaré (une coordonnée de π perturbée à la fois,
nominal inclus), avec publication des axes responsables de toute
fragilité (Σ < 1).

**N5 — Intégrité chaînée.** Chaque artefact (données, script, verdict,
figure, note) DOIT être figé par empreinte SHA-256, et le fichier
d'empreintes DOIT être régénéré sur l'ensemble de l'arbre publié.

**N6 — Publication des échecs (B3-FAIL).** Toute attente pré-enregistrée
non tenue, toute fragilité mesurée, toute rupture de chaîne d'intégrité
et tout défaut découvert DOIT être publié comme artefact de première
classe, au même niveau que les succès.

**N7 — Addenda seulement.** Aucun artefact publié ne DOIT être réécrit ;
les corrections prennent la forme d'addenda chaînés datés.

**N8 — Registre des frontières.** L'opérateur DOIT tenir un registre où
chaque limite connue est une entrée : énoncé, statut, coût de fermeture
exact, falsifieur exécutable, empreinte par entrée et globale.

## 5. Domaine de validité de la chaîne ASH (conditions V1–V6)

Pour la couche d'acquisition spectrale (ASH), l'éligibilité d'un signal
est la conjonction de :

- **V1** série temporelle 1D ;
- **V2** contenu utile dans la grille [f₀, f₀·2^N_oct] et sous Nyquist ;
- **V3** écarts à résoudre > résolution effective
  δf_eff(f) = max(2^(1/12) − 1, (f_s/nperseg)/f) ;
- **V4** récurrence : ≥ ~8 événements par fenêtre (une paire n'a pas de
  porteuse — mesuré P43-C5) ;
- **V5** tâche structurelle (détection/classification), pas métrologie
  d'amplitude (ReN non invariant d'échelle — F16) ;
- **V6** verdict stable sous batterie de perturbation (Σ publiée).

## 6. Méthodes d'essai (rejouables)

**E1 (N1)** — inspection de D : aucune donnée nouvelle n'entre dans S
après gel ; la comparaison d'empreintes avant/après exécution DOIT être
identique.

**E2 (N3, N4)** — exécution de la batterie PERT-BATT sur le chantier
encapsulé en fonction pure f(π) : la stabilité Σ est calculée sur
1 nominal + k perturbés ; les fragilités sont publiées avec l'axe
responsable.

**E3 (N4)** — certification par mutation : les accidents historiques
sont réintroduits comme protocoles mutés ; la batterie DOIT les détecter,
sinon elle est elle-même non conforme.

**E4 (N5)** — vérification de la chaîne : `sha256sum` sur chaque
artefact, comparaison au fichier d'empreintes ; toute divergence est un
événement à publier.

**E5 (N8)** — lecture du registre : chaque entrée DOIT comporter un
falsifieur exécutable ; une entrée sans falsifieur est non conforme.

**E6 (global)** — rejeu complet : un tiers exécutant les scripts avec
les données figées DOIT obtenir des verdicts identiques aux empreintes.

## 7. Format du registre des frontières (REG-FR-1.0)

Chaque entrée : `id`, `type` (physique | méthode | hygiène), `énoncé`,
`chantier_source`, `protocole`, `statut` (ouverte | partielle | fermée |
réfutée), `coût_de_fermeture_exact`, `comptage_ddll` (verdict +
justification), `artefacts`, `falsifieur`, `sha256_entrée`. Le registre
porte un `sha256_registre` global recalculé à chaque modification.

## 8. Conformité

Une affirmation est conforme à la présente spécification si et seulement
si elle est livrée avec : (a) le couple (V, Σ) mesuré par E2 ; (b) le
falsifieur exécutable associé (E5) ; (c) l'empreinte SHA-256 de
l'artefact (E4) ; (d) l'inscription de ses limites au registre (N8) ;
(e) la publication B3-FAIL de ses échecs (N6).

---

## Annexe A — Safety case pilote (exécuté)

**Tâche** : lecture exacte d'un état à n composantes par un bloc linéaire
(attention à scores bilinéaires, readout par agrégation de valeurs).

**Certificat de minimalité (calculé, rejouable)** : la tâche exige
**n canaux indépendants** (n dimensions de représentation positionnelle).
Chaîne de preuve : (i) la validité du readout exige la dominance
diagonale stricte de la matrice de scores (nécessité mesurée par
exécution, exhaustive sur petites tailles) ; (ii) une matrice
strictement diagonalement dominante est non singulière (théorème de
Lévy–Desplanques, cité) ; (iii) des scores bilinéaires de rang ≤ r
imposent r ≥ n ; (iv) la construction one-hot atteint r = n. Le chemin
candidat à rang 3 (scores quadratiques) est réfuté par exécution sur les
séquences à doublons et publié comme B3-FAIL interne.

**Artefact** : verdict `m2e_copie_tri_verdict.json` du corpus
(sha `aa518fbf…`), échantillon figé de 200 matrices de rang < n par
taille, toutes échouées — mesuré, pas simulé.

**Portée** : la forme d'argument — *coût minimal calculé + preuve
rejouable + falsifieur* — est celle que la présente spécification propose
pour les safety cases en général (absente des normes IEC 61508 /
ISO 26262, où les arguments de complétude restent des assertions
d'expert).

## Annexe B — Falsifieurs de la spécification elle-même

1. Tout tiers ne parvenant pas à rejouer un artefact conforme avec les
   mêmes empreintes tue E6 pour cet artefact.
2. Toute exigence de la norme harmonisée entrante (AI Act, art. 9–15)
   non couverte par la table de conformité jointe (D6) est publiée en
   addendum, jamais corrigée en silence.
3. La non-rejouabilité de la présente spécification par tout tiers sous
   six mois réfute la voie D5 — publiée telle quelle dans le registre N1.
