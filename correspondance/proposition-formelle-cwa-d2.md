# Proposition formelle d'atelier CEN-CENELEC — D2

**Formulaire de proposition de CEN Workshop Agreement (CWA)**

| Champ | Contenu |
|---|---|
| **Titre de l'atelier** | Exécutable evidence for high-risk AI performance claims — Format de preuve exécutable pour les affirmations de performance des systèmes d'IA à haut risque |
| **Type de livrable** | CWA (CEN Workshop Agreement) |
| **Proposant** | Patrice Portemann — Écosystème Noetic Physics (chercheur indépendant) |
| **Contact** | patrice@portemann.eu · ORCID 0009-0009-4016-8389 |
| **Date de proposition** | 31 août 2026 |
| **Version** | 1.0 (formelle) |

---

## A. Titre et champ de l'atelier

**Titre** : Exécutable evidence for high-risk AI performance claims.

**Champ** : définition d'un format de preuve exécutable pour les
affirmations de performance (exactitude, robustesse, cybersécurité) des
systèmes d'IA à haut risque au sens de l'art. 15 du règlement (UE)
2024/1689, modifié par (UE) 2026/1744.

L'atelier couvre les tâches de classification, détection et diagnostic.
Il ne couvre ni la génération de contenu, ni les systèmes à optimisation
continue (contrôle en boucle fermée temps réel).

## B. Objectif et justification

**Problème mesuré.** La preuve de performance algorithmique est
documentaire (registres, logs, cartographies de risques), jamais
exécutable : aucun artefact publié — au niveau industriel ou normatif —
n'est livré avec un test rejouable qui le falsifie. La recherche
multi-agents du 31/08/2026 (12 dimensions, ~300 requêtes) n'a trouvé
aucune pratique de falsification exécutable déposée avec une affirmation
de performance ; la seule occurrence identifiée (POPPER, ICML 2025) est
un prototype non adopté.

**Fenêtre normative.** Les obligations haut risque entrent en vigueur le
2 décembre 2027 (annexe III) / 2 août 2028 (annexe I). Une norme
harmonisée est publiée (EN 18286, système de gestion), aucune n'est
citée au JOUE, aucun organisme notifié n'est désigné, ~13 projets prEN
sont en rédaction. Le format de preuve se définit maintenant.

**Valeur ajoutée.** Un format exécutable — où chaque affirmation porte
son protocole gelé, sa stabilité mesurée par perturbation, son falsifieur
déposé et son empreinte chaînée — rend la conformité art. 15 vérifiable
par un tiers sans accès au système, et publie les limites au lieu de les
dissimuler.

## C. Livrables

| # | Livrable | Contenu | Échéance (mois après constitution) |
|---|---|---|---|
| L1 | Spécification du format | Définitions ; exigences normatives (shall) ; méthodes d'essai rejouables ; format du registre des limites | M+3 |
| L2 | Cas d'application exécutés | (a) instrument spectral à verdict (chaîne ASH → opérateur) ; (b) safety case avec certificat de minimalité calculé | M+5 |
| L3 | Guide d'alignement | Cartographie format ↔ art. 15 AI Act ↔ projets prEN JTC 21 (robustesse, journalisation, documentation technique) | M+6 |

**Base de départ** : la spécification ouverte ASH-MACH v0.1 (publiée,
rejouable) — l'atelier ne part pas d'une page blanche mais d'un format
exécuté sur un corpus public de 371 artefacts figés.

## D. Plan de travail et calendrier

| Jalon | Contenu | Cible |
|---|---|---|
| J0 | Constitution du groupe d'atelier | 2027-T1 |
| J1 | Revue du format v0.1, adoption du périmètre | 2027-T1 |
| J2 | Exécution des deux cas, publication intermédiaire | 2027-T2 |
| J3 | Revue finale, vote et dépôt du CWA | 2027-T3 |

Durée totale : 6–9 mois après constitution.

## E. Parties intéressées sollicitées

L'atelier est ouvert à tout acteur, y compris les petits. Sont
sollicitées :

- laboratoires nationaux de métrologie (PTB/DAkkS ; délégation française) ;
- organismes d'audit et de conformité IA (art. 9–15) ;
- intégrateurs d'instruments à verdict (monitoring embarqué) ;
- utilisateurs industriels (ferroviaire, énergie, médical) ;
- délégation nationale de normalisation (AFNOR) ;
- recherche (métrologie du logiciel, vérification formelle).

## F. Ressources

Le proposant apporte : le corpus de référence complet (public, MIT), la
spécification de base (ASH-MACH v0.1), les deux cas exécutés (DCC étendu
et fiche d'instrument), la table de conformité art. 9–15 publiée, et
l'infrastructure de figeage SHA-256. Aucun financement n'est demandé.

## G. Propriété intellectuelle

Les livrables de l'atelier seront publiés sous licence ouverte (MIT ou
équivalent). Le corpus de référence est déjà public sous MIT.

## H. Mesure de succès et falsifiabilité

Conformément à la discipline du corpus, la proposition porte son
falsifieur : si l'atelier n'aboutit pas ou si la proposition est refusée,
le refus est publié tel quel dans le registre public du projet
(`noetic-normes`, entrée D2). Deux refus consécutifs ferment la voie —
documentée, pas persévérée en silence. Le succès se mesure à
l'adoption du format par au moins un organisme tiers d'ici décembre 2027.

---

*Références : corpus `github.com/PORTEMANN/noetic-machine-complete` ;
dépôt normatif `github.com/PORTEMANN/noetic-normes` ; instrument audité
`github.com/PORTEMANN/noetic-ash` v1.1.0. Empreintes : SHASUMS.txt de
chaque dépôt.*
