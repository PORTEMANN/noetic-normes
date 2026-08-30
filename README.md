# noetic-normes — Normalisation pilotée par la Machine Noétique

Prospection des directions de normalisation de
l'écosystème Noetic Physics, régie par le protocole de la machine :
zéro paramètre ajusté, protocoles gelés, falsifieurs exécutables,
échecs publiés (B3-FAIL), artefacts figés SHA-256.

## Protocole NORM-MACH-1.0 (gelé)

1. **Toute direction est une entrée de registre** — énoncé, statut, coût
   de fermeture exact, falsifieur exécutable. Pas de direction «
   prometteuse » sans mesure.
2. **Toute avancée est un artefact figé** — document, table, cas,
   chacun avec son SHA-256 dans `SHASUMS.txt`.
3. **Tout échec est publié dans le registre** (refus d'atelier, clause
   rejetée, absence de rejeu par des tiers) — statut `réfutée`, jamais
   effacé.
4. **Addenda seulement** — aucune entrée n'est réécrite ; les mises à
   jour sont des addenda chaînés.
5. **Privé jusqu'au dépôt externe** — chaque direction bascule en public
   au moment de son dépôt officiel (DCC, CWA, AFNOR, OIML), pas avant.

## Registre N1 (protocole NORM-REG-1.0)

| Entrée | Direction | Type | Statut |
|---|---|---|---|
| D1-DCC-VERDICT | DCC étendu d'un champ « verdict algorithmique » (PTB/DAkkS) | pont | **en-cours** — cas auto-émis produit (`specs/dcc-etendu-ash-mach-0.1.xml`), contact métrologie légale à engager |
| D2-CWA-PREUVE-EXECUTABLE | CEN Workshop Agreement : preuve exécutable art. 15 | norme | **en-cours** — proposition rédigée (`docs/proposition-cwa-preuve-executable.md`), dépôt 2027-T1 |
| D3-CLAUSES-PREN | Deux clauses exécutées pour les prEN JTC 21 (via AFNOR) | norme | **en-cours** — clauses + dossier de preuve (`docs/clauses-pren-robustesse-limites.md`), contact AFNOR à engager |
| D4-OIML-INSTRUMENT-VERDICT | Catégorie « instrument à verdict algorithmique » (OIML/WELMEC) | pont | **en-cours** — fiche produite (`specs/fiche-instrument-verdict-0.1.md`), adossée à D1 |
| D5-SPEC-ASH-MACH | Spécification ouverte ASH-MACH auto-appliquée + safety case pilote | spécification | **en-cours** — produite (`specs/ash-mach-0.1.md`), fenêtre de rejeu tiers ouverte jusqu'au 2027-02-28 |
| D6-TABLE-CONFORMITE-AIACT | Table de conformité AI Act (art. 9–15) du corpus | spécification | **fermée** — produite (`docs/table-conformite-ai-act.md`), écarts suivis en addenda |

Registre machine-lisible : `data/n1_registre_normes.json` (régénéré par
`src/n1_registre_normes.py` — empreintes par entrée + globale).

## Fondation

- `docs/note-directions-normes.md` — la note stratégique (six directions,
  séquence, falsifieurs du plan) issue de la recherche multi-agents du
  31/08/2026 (12 dimensions, ~300 requêtes).
- `specs/ash-mach-0.1.md` — la spécification ouverte : exigences SHALL,
  essais rejouables, falsifieurs, safety case pilote exécuté.
- `specs/dcc-etendu-ash-mach-0.1.xml` — cas DCC étendu auto-émis (champ
  « verdict algorithmique », schéma DCC v3.3.0).
- `specs/fiche-instrument-verdict-0.1.md` — fiche d'instrument à verdict
  (gabarit OIML/WELMEC, domaine V1–V6).
- `docs/table-conformite-ai-act.md` — la table de conformité AI Act
  (art. 9–15) avec écarts publiés.
- `docs/proposition-cwa-preuve-executable.md` — proposition d'atelier CWA.
- `docs/clauses-pren-robustesse-limites.md` — deux clauses normatives +
  dossier de preuve.
- Corpus de référence : `noetic-machine-complete` (P0–P45, série A,
  série M, registre A4 de 20 frontières).
- Instrument audité : `noetic-ash` v1.1.0.

## Fenêtre mesurée

Obligations AI Act haut risque reportées au 2 décembre 2027 (annexe III)
/ 2 août 2028 (annexe I) par le règlement (UE) 2026/1744. Une norme
harmonisée publiée (EN 18286), zéro citée au JOUE, zéro organisme
notifié désigné. La fenêtre est celle de la *définition* des normes.

## Licence

MIT — © 2026 Patrice Portemann.
