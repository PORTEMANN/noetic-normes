# Soumission formelle D3 — Deux clauses pour les projets prEN (JTC 21)

**Destinataire** : AFNOR — délégation française au comité technique
CEN-CENELEC JTC 21 (Intelligence artificielle)

**Objet** : Proposition de deux clauses pour les projets prEN en cours
(robustesse ; documentation technique) — chacune accompagnée de sa preuve
d'exécution publique.

**De** : Patrice Portemann, chercheur indépendant, écosystème Noetic
Physics (ORCID 0009-0009-4016-8389, patrice@portemann.eu)

**Le 31 août 2026**

---

Madame, Monsieur,

Je vous soumets deux clauses destinées aux projets prEN en préparation
au CEN-CENELEC JTC 21, relatives à l'article 15 (robustesse) et à
l'annexe IV (documentation technique) du règlement (UE) 2024/1689
modifié par (UE) 2026/1744. Chacune est déjà exécutée sur un corpus
public et rejouable — elles arrivent avec leur preuve, pas avec un texte
seul.

---

## Clause 1 — Stabilité du protocole d'évaluation (robustesse)

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
fixes : elles dépendent du protocole d'évaluation — dépendance jamais
documentée. La perturbation déclarée du protocole est la seule méthode
qui mesure cette dépendance au lieu de la nier.

**Preuve d'exécution publique** (rejouable — scripts et données figées
SHA-256, corpus `github.com/PORTEMANN/noetic-machine-complete`) :

| Chantier | Protocoles testés | Résultat | Artefact |
|---|---|---|---|
| A1 — neurone formel (P34) | 9 | Σ = 1,00 sur tous les verdicts ; prédictions pré-enregistrées confirmées | `a1_batterie_verdict.json` |
| A1 — neurone biologique (P35) | 17 | fragilités publiées avec axes responsables ; 3 accidents historiques réintroduits comme mutations, tous détectés | `a1_batterie_verdict.json` |
| A1b — stabilité nucléaire (P13) | 13 | Σ = 1,00 (4/4) | `a1b_batterie_retroactive_verdict.json` |
| A1b — double bêta (P22) | 16 | Σ_min = 0,94 ; une fragilité publiée (faux positifs sous seuil_q1 = 0,7) | `a1b_batterie_retroactive_verdict.json` |
| P43 — audit d'instrument (ASH) | 11 | Σ = 1,00 sur 6/8 composantes ; fragilités publiées (S1 : nperseg=128 ; S4 : f0, N_oct) | `p43_ash_sous_machine_verdict.json` |

## Clause 2 — Registre des limites mesurées (documentation technique)

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
leur falsifieur — dont une détectée par la machine sur elle-même (F9 :
intégrande défectueuse réparée et re-publiée avec verdict corrigé
3/5 → 5/5). Chaque entrée : énoncé, statut, coût de fermeture exact,
falsifieur exécutable, empreinte SHA-256 par entrée et globale.

---

## Demande

Je sollicite l'examen de ces deux clauses par la délégation française au
JTC 21, en vue de leur insertion dans les projets prEN relatifs à la
robustesse et à la documentation technique. Je me tiens disponible pour
toute itération, démonstration ou audition technique. Tout rejet
documenté sera publié dans le registre public du projet ; deux rejets
consécutifs ferment la direction sans persévérance silencieuse.

Veuillez agréer, Madame, Monsieur, l'expression de ma considération
distinguée.

**Patrice Portemann**

---

*Annexes : (a) dossier de preuve complet
(`docs/clauses-pren-robustesse-limites.md`) ; (b) spécification ASH-MACH
v0.1 ; (c) table de conformité AI Act art. 9–15 ; (d) registres A4
(corpus) et N1 (normalisation). Empreintes : SHASUMS.txt des dépôts
publics.*
