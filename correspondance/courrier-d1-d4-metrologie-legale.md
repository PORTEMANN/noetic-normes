# Courrier D1/D4 — Métrologie légale

**Destinataire** : Physikalisch-Technische Bundesanstalt (PTB) —
groupe Digital Calibration Certificate · DAkkS · délégation française de
métrologie légale (LNE — Direction de la métrologie légale)

**Objet** : Proposition d'extension du Digital Calibration Certificate
(DCC) par un champ « verdict algorithmique » et présentation d'une fiche
d'instrument à verdict algorithmique — cas complet exécuté, rejouable,
publié sous licence ouverte.

Patrice Portemann
Chercheur indépendant — Écosystème Noetic Physics
ORCID : 0009-0009-4016-8389 · patrice@portemann.eu
Corpus : github.com/PORTEMANN/noetic-machine-complete

Le 31 août 2026

---

Madame, Monsieur,

Je vous adresse une proposition concrète et exécutée d'extension du
Digital Calibration Certificate à destination des instruments dont la
fonction principale est un **verdict algorithmique** (classification,
détection de régime, diagnostic automatisé).

## 1. Motivation

Le DCC porte aujourd'hui la traçabilité et l'incertitude des mesures.
Lorsque l'instrument ne mesure plus une grandeur mais émet un verdict —
une affirmation sur la structure d'un signal —, le contenu à certifier
change de nature : ce n'est plus une valeur avec une incertitude, mais
une affirmation avec un **protocole**, un **domaine de validité mesuré**,
une **stabilité** et un **falsifieur exécutable**. Aucun de ces quatre
contenus n'a de champ dans le schéma actuel.

Cette extension est proposée alors que les normes harmonisées de
l'AI Act (règlement (UE) 2024/1689, modifié par (UE) 2026/1744) sont en
rédaction au CEN-CENELEC JTC 21 — la définition du format de preuve pour
l'art. 15 (robustesse) se joue maintenant, et la métrologie légale est le
canal où la chaîne d'intégrité (SHA-256) est déjà la norme (OIML D 31).

## 2. La proposition, exécutée

Le cas joint — `dcc-etendu-ash-mach-0.1.xml` — est un DCC auto-émis
complet pour une chaîne réelle (analyseur spectral ASH + opérateur de
verdict), auditée par le protocole gelé ASH-MACH-1.0 (7/7 critères).
L'extension est portée dans `<dcc:statements>` — la zone extensible
prévue par le schéma v3.3.0 — et contient :

1. **le protocole gelé** (π) — tous les paramètres, aucun ajusté ;
2. **le domaine de validité mesuré** (V1–V6) — chaque condition avec sa
   valeur mesurée et l'essai qui l'a établie ;
3. **le falsifieur exécutable déposé** — le test dont le succès réfute
   le certificat ;
4. **la stabilité Σ** — mesurée par perturbation déclarée du protocole
   (plan factoriel axial), fragilités publiées avec l'axe responsable ;
5. **l'empreinte SHA-256** de chaque artefact, chaînée sur l'ensemble.

La fiche d'instrument jointe (`fiche-instrument-verdict-0.1.md`) propose
le gabarit de domaine mesuré pour la catégorie OIML/WELMEC
correspondante.

## 3. Ce qui distingue cette proposition

Elle n'est pas un texte à discuter mais un **système qui tourne** :
l'instrument audité est public (github.com/PORTEMANN/noetic-ash), le
corpus de référence est public (371 artefacts figés SHA-256), les
verdicts sont rejouables, les échecs sont publiés au même titre que les
succès (B3-FAIL) — y compris une réparation forensique où la machine a
détecté et corrigé un défaut de son propre corpus (F9).

## 4. Demande

Je sollicite votre évaluation technique du format proposé — en
particulier : la portabilité du champ dans le schéma DCC, la forme des
mesures à déclarer pour un verdict, et l'articulation avec OIML D 31 /
WELMEC 7.2 pour les instruments à verdict. Je suis à votre disposition
pour toute itération, et je publierai toute objection technique dans le
registre public du projet.

Veuillez agréer, Madame, Monsieur, l'expression de ma considération
distinguée.

**Patrice Portemann**

---

*Annexes : (a) cas DCC étendu auto-émis `dcc-etendu-ash-mach-0.1.xml` ;
(b) fiche d'instrument `fiche-instrument-verdict-0.1.md` ; (c)
spécification ASH-MACH v0.1 ; (d) table de conformité AI Act art. 9–15.
Tous publiés : github.com/PORTEMANN/noetic-normes — empreintes dans
SHASUMS.txt.*
