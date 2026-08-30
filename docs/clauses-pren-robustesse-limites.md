# Clauses normatives proposées — robustesse et documentation des limites

**Pour insertion dans les projets prEN CEN-CENELEC JTC 21 (délégation AFNOR)**
**Version 0.1 — 31 août 2026 — direction D3 du registre N1 (noetic-normes)**
**Preuve d'exécution publique : batteries A1/A1b du corpus, verdicts figés.**

---

## Clause 1 — Stabilité par perturbation du protocole d'évaluation (robustesse)

> **15.x — Stabilité du protocole d'évaluation.**
> *Toute affirmation de performance d'un système d'IA à haut risque DOIT
> être accompagnée d'une mesure de stabilité obtenue par perturbation
> déclarée du protocole d'évaluation. Le protocole (paramètres d'entrée,
> seuils, grilles, fenêtres, conventions) DOIT être documenté avant
> exécution. La stabilité DOIT être mesurée par un plan factoriel axial
> (une coordonnée perturbée à la fois, protocole nominal inclus), en
> publiant, pour chaque fragilité identifiée, la coordonnée responsable.
> Une affirmation livrée sans stabilité mesurée est réputée non
> démontrée.*

**Justification.** L'art. 15 exige une robustesse « mesurée et déclarée ».
Les robustesses publiées actuelles sont des moyennes sur jeux de test
fixes : elles dépendent du protocole d'évaluation, dépendance jamais
documentée. La perturbation déclarée du protocole est la seule méthode
qui mesure cette dépendance au lieu de la nier.

**Preuve d'exécution publique.** Exécutée sur le corpus de référence :

| Chantier | Protocoles testés | Résultat | Artefact |
|---|---|---|---|
| A1 — neurone formel (P34) | 9 | Σ = 1,00 sur tous les verdicts ; prédictions pré-enregistrées confirmées | `a1_batterie_verdict.json` |
| A1 — neurone biologique (P35) | 17 | fragilités publiées avec axes responsables ; 3 accidents historiques réintroduits comme mutations, tous détectés | `a1_batterie_verdict.json` |
| A1b — stabilité nucléaire (P13) | 13 | Σ = 1,00 (4/4) | `a1b_batterie_retroactive_verdict.json` |
| A1b — double bêta (P22) | 16 | Σ_min = 0,94 ; une fragilité publiée (faux positifs sous seuil_q1 = 0,7) | `a1b_batterie_retroactive_verdict.json` |
| P43 — audit d'instrument (ASH) | 11 | Σ = 1,00 sur 6/8 composantes ; fragilités publiées (S1 : nperseg=128 ; S4 : f0, N_oct) | `p43_ash_sous_machine_verdict.json` |

Chaque exécution est rejouable : scripts publics, données figées SHA-256.

## Clause 2 — Registre des limites mesurées (documentation, annexe IV)

> **11.y — Registre des limites.**
> *La documentation technique d'un système d'IA à haut risque DOIT
> comprendre un registre des limites mesurées dans lequel chaque limite
> connue est une entrée comportant : l'énoncé de la limite, son statut
> (ouverte, partielle, fermée, réfutée), le coût exact de sa fermeture
> lorsqu'il est déterminé, et le test rejouable dont le succès la lève
> (falsifieur). Le registre DOIT être mis à jour par addenda datés, sans
> suppression d'entrée. Les limites découvertes après mise sur le marché
> DOIVENT y être inscrites au même titre que celles identifiées en
> développement.*

**Justification.** L'annexe IV demande une description des « limites
connues et prévisibles ». Sans format, cette exigence se satisfait d'un
paragraphe vague. Le registre impose la granularité qui rend la limite
vérifiable : chaque limite porte son test de sortie.

**Preuve d'exécution publique.** Le registre A4 du corpus (format
REG-FR-1.0) porte 20 entrées mesurées, dont 9 fermées par exécution de
leur falsifieur — dont une détectée par la machine sur elle-même (F9,
intégrande défectueuse réparée et re-publiée avec verdict corrigé 3/5 →
5/5). Chaque entrée : énoncé, statut, coût de fermeture exact, falsifieur
exécutable, empreinte SHA-256 par entrée et globale. Le registre N1
(normalisation) applique le même format à la stratégie normative elle-
même.

---

## Dossier de preuve récapitulatif

| Clause | Objet | Statut d'exécution |
|---|---|---|
| 1 — Stabilité par perturbation | batterie PERT-BATT (plan factoriel axial, certification par mutation) | **Exécutée** — 5 chantiers, 66 protocoles cumulés, fragilités publiées avec axes |
| 2 — Registre des limites | format REG-FR-1.0 / NORM-REG-1.0 | **Exécutée** — 20 entrées (A4) + 6 directions (N1), SHA-256 par entrée et global |

*Ces clauses arrivent avec une preuve d'exécution publique, pas avec un
texte seul. Tout rejet documenté sera publié dans le registre N1 ; deux
rejets consécutifs ferment la direction D3 — sans persévérance silencieuse.*
