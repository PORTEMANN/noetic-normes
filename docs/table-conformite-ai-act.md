# Table de conformité — Machine Noétique vs AI Act (art. 9–15)

**31 août 2026 — v1.0**
**Cadre : règlement (UE) 2024/1689 modifié par (UE) 2026/1744 (obligations
haut risque reportées au 2 déc. 2027 / 2 août 2028).**
**Objet : cartographie publique des artefacts du corpus sur les exigences.
Tout écart découvert ultérieurement sera publié en addendum — jamais
corrigé en silence (falsifieur de l'entrée D6 du registre N1).**

| Article AI Act | Exigence | Artefact du corpus qui la couvre | État |
|---|---|---|---|
| **9 — Système de gestion des risques** | processus continu d'identification, évaluation, mitigation | **Registre A4** (20 frontières : énoncé, statut, coût de fermeture exact, ddll, falsifieur) + registre N1 (6 directions de normalisation) ; chaque risque connu est une entrée mesurée avec son falsifieur exécutable | **Couvert (substance)** — pas de processus QMS documenté (forme, à produire) |
| **10 — Gouvernance des données** | qualité, provenance, pertinence des données | **D figées** : tables d'origine déclarée dans chaque script (AME2020, JEFF-3.1.1, Allen Cell Types release `artefacts-donnees-v1.0` avec empreintes) ; aucune donnée ré-ajustée (N1 de la spécification ASH-MACH) | **Couvert** |
| **11 — Documentation technique** | description du système, développement, fonctionnement | Notes de chantiers (md/docx) par artefact, protocoles gelés en en-tête de chaque script, doc technique chaîne ASH → M̂ (LaTeX, domaine V1–V6) | **Couvert (substance)** — pas de format annexe IV structuré (forme, à produire) |
| **12 — Journalisation** | enregistrement automatique des événements | Chaîne git (chaque version conservée), registres A4/N1 avec SHA par entrée et global, verdicts JSON datés | **Couvert** |
| **13 — Transparence** | informations permettant d'interpréter la sortie | Chaque verdict est un couple (V, Σ) décomposable en composantes ; falsifieurs lisibles dans chaque artefact ; spécification ASH-MACH §3 (définitions) | **Couvert (substance)** |
| **14 — Supervision humaine** | capacité d'intervention effective | Le verdict **refuse de commander quand Σ chute** (fragilité publiée avec l'axe responsable — comportement structurel, pas statistique) ; le registre des frontières dit où la machine s'arrête | **Couvert (substance)** — pas de procédure humaine documentée (forme, à produire) |
| **15 — Précision, robustesse, cybersécurité** | niveau approprié mesuré et déclaré | **Batterie PERT-BATT** (stabilité Σ mesurée par perturbation déclarée du protocole, plan factoriel axial, axes responsables publiés) ; intégrité chaînée SHA-256 sur 371 artefacts + release ; audit d'intégrité exécutable (F9 détectée par la machine elle-même) | **Couvert (substance)** |

## Écarts publiés (honnêteté de la table)

1. **Forme QMS absente** : la machine produit la substance (mesures,
   registres, preuves) mais pas le système de gestion de qualité
   documenté exigé par EN 18286 — coût de fermeture déclaré : un fichier
   QMS minimal, à produire.
2. **Pas de plan de surveillance post-commercialisation** : le registre
   des frontières surveille les limites connues, pas un plan formel de
   suivi en exploitation — à produire.
3. **Pas de procédure de supervision humaine documentée** : le
   comportement structurel existe (refus quand Σ chute), la procédure
   opérationnelle associée n'est pas écrite — à produire.

*Cette table est un artefact du registre N1 (entrée D6). Toute divergence
découverte entre cette lecture et les normes harmonisées finales sera
publiée ici en addendum chaîné.*
