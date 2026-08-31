#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
N1 — REGISTRE DES DIRECTIONS DE NORMALISATION
==============================================
Protocole gelé NORM-REG-1.0 — même schéma que le registre A4 du corpus
(REG-FR-1.0), appliqué à la normalisation. Chaque direction de
prospection est une entrée : énoncé, statut, coût de fermeture exact,
falsifieur exécutable, SHA-256 par entrée et global.

Discipline héritée de la machine : aucune direction n'est « prometteuse »
sans mesure ; chaque avancée est un artefact figé ; chaque échec (refus
d'atelier, clause rejetée, absence de rejeu) est publié en B3-FAIL dans
le registre, jamais effacé.

Statuts : ouverte · en-cours · partielle · fermée · réfutée (publiée).
Types : norme (canal normatif externe) · spécification (auto-appliquée) ·
pont (canal technique existant à étendre).

Règle addenda : les champs d'origine d'une entrée (énoncé, coût,
falsifieur) ne sont jamais réécrits ; les mises à jour prennent la forme
d'addenda datés chaînés dans le champ « addenda ».
"""

import hashlib
import json
from pathlib import Path

TYPES = {"norme", "spécification", "pont"}
STATUTS = {"ouverte", "en-cours", "partielle", "fermée", "réfutée"}


def entree(id_, type_, enonce, protocole, statut, cout, artefacts,
           falsifieur, addenda=None):
    assert type_ in TYPES and statut in STATUTS
    e = {"id": id_, "type": type_, "énoncé": enonce, "protocole": protocole,
         "statut": statut, "coût_de_fermeture_exact": cout,
         "artefacts": artefacts, "falsifieur": falsifieur}
    if addenda:
        e["addenda"] = addenda
    blob = json.dumps(e, ensure_ascii=False, sort_keys=True).encode()
    e["sha256_entrée"] = hashlib.sha256(blob).hexdigest()
    return e


DIRECTIONS = [
    entree(
        "D1-DCC-VERDICT", "pont",
        "Étendre le Digital Calibration Certificate (PTB/DAkkS) d'un champ "
        "« verdict algorithmique » : protocole gelé, domaine mesuré, "
        "falsifieur exécutable, stabilité Σ, empreinte SHA-256 — la chaîne "
        "ASH → M̂ publiée comme un DCC étendu auto-émis et rejouable",
        "NORM-MACH-1.0", "en-cours",
        "produire le cas complet (DCC étendu de la chaîne ASH → M̂, "
        "rejouable) + contact avec la communauté métrologie légale "
        "(PTB/DAkkS ou délégation française)",
        {"fondation": "docs/note-directions-normes.md §D1",
         "gabarit": "doc technique chaîne ASH → M̂ (V1–V6, corpus)"},
        "si le cas DCC étendu publié n'est rejoué par aucun tiers en six "
        "mois → la voie est réfutée telle quelle (publié) ; si le format "
        "DCC ne peut pas porter un champ verdict → publié, direction "
        "refermée vers D2/D4",
        addenda=[
            {"date": "2026-08-31",
             "action": "production livrée — cas DCC étendu auto-émis "
                       "rédigé (champ « verdict algorithmique » dans "
                       "<dcc:statements>, schéma DCC v3.3.0) ; contact "
                       "métrologie légale à engager",
             "artefacts": ["specs/dcc-etendu-ash-mach-0.1.xml"],
             "note": "fenêtre de rejeu tiers ouverte jusqu'au 2027-02-28"},
            {"date": "2026-08-31",
             "action": "version formelle prête à envoyer — courrier à la "
                       "métrologie légale (PTB/DAkkS/LNE) rédigé",
             "artefacts": ["correspondance/courrier-d1-d4-metrologie-legale.md"]},
        ]),
    entree(
        "D2-CWA-PREUVE-EXECUTABLE", "norme",
        "CEN Workshop Agreement : « Exécutable evidence for high-risk AI "
        "performance claims » — figer le format de preuve (art. 15 AI "
        "Act : robustesse) avant les normes harmonisées, avec le corpus "
        "comme cas de référence vivant (20 frontières, falsifieurs "
        "exécutables)",
        "NORM-MACH-1.0", "en-cours",
        "rédiger la proposition d'atelier (scope, livrables, calendrier) "
        "et la déposer — ouverte à tout acteur, y compris petits",
        {"fondation": "docs/note-directions-normes.md §D2",
         "cas_de_référence": "github.com/PORTEMANN/noetic-machine-complete"},
        "si l'atelier n'aboutit pas ou si la proposition est refusée → "
        "publié tel quel (B3-FAIL du plan) ; deux refus consécutifs "
        "ferment la voie",
        addenda=[
            {"date": "2026-08-31",
             "action": "production livrée — proposition d'atelier CWA "
                       "rédigée (scope, 3 livrables, calendrier 2027, "
                       "parties sollicitées, IPR) ; dépôt prévu 2027-T1",
             "artefacts": ["docs/proposition-cwa-preuve-executable.md"]},
            {"date": "2026-08-31",
             "action": "version formelle prête à déposer — formulaire CWA "
                       "complet v1.0 rédigé",
             "artefacts": ["correspondance/proposition-formelle-cwa-d2.md"]},
        ]),
    entree(
        "D3-CLAUSES-PREN", "norme",
        "Entrer dans les projets prEN CEN-CENELEC JTC 21 (délégation "
        "AFNOR) avec deux clauses déjà exécutées dans le corpus : (i) la "
        "stabilité par perturbation du protocole d'évaluation comme "
        "exigence de robustesse ; (ii) le registre de limites mesurées "
        "comme structure de la documentation annexe IV",
        "NORM-MACH-1.0", "en-cours",
        "formuler les deux clauses en langage normatif + dossier de preuve "
        "(A1/A1b exécutés) + prise de contact délégation nationale",
        {"fondation": "docs/note-directions-normes.md §D3",
         "preuve": "a1_batterie_perturbation.py, a1b_batterie_retroactive.py "
                   "(corpus, verdicts figés)"},
        "si les deux clauses sont rejetées deux fois → la voie est "
        "documentée comme fermée, pas persévérée en silence",
        addenda=[
            {"date": "2026-08-31",
             "action": "production livrée — deux clauses en langage "
                       "normatif (stabilité par perturbation ; registre "
                       "des limites) + dossier de preuve (5 chantiers, "
                       "66 protocoles) ; contact AFNOR à engager",
             "artefacts": ["docs/clauses-pren-robustesse-limites.md"]},
            {"date": "2026-08-31",
             "action": "version formelle prête à envoyer — soumission "
                       "AFNOR rédigée (les deux clauses + demande + "
                       "annexes)",
             "artefacts": ["correspondance/soumission-clauses-d3-afnor.md"]},
        ]),
    entree(
        "D4-OIML-INSTRUMENT-VERDICT", "pont",
        "Proposer à OIML/WELMEC la catégorie « instrument à verdict "
        "algorithmique » : fiche de domaine mesuré obligatoire (résolution "
        "effective, train minimal d'événements, stabilité) sur le gabarit "
        "V1–V6 du document technique ASH → M̂",
        "NORM-MACH-1.0", "en-cours",
        "adapter le gabarit V1–V6 en fiche d'instrument + l'adosser au cas "
        "D1 (DCC étendu) avant de contacter OIML/WELMEC",
        {"fondation": "docs/note-directions-normes.md §D4",
         "gabarit": "doc technique chaîne ASH → M̂ (LaTeX, corpus)"},
        "si le canal exige une représentation formelle inaccessible → "
        "documenté, replis vers D1 seul ; toute objection technique est "
        "publiée",
        addenda=[
            {"date": "2026-08-31",
             "action": "production livrée — fiche d'instrument à verdict "
                       "algorithmique rédigée (gabarit OIML/WELMEC, "
                       "V1–V6 + limites publiées + falsifieurs), adossée "
                       "au cas D1",
             "artefacts": ["specs/fiche-instrument-verdict-0.1.md"]},
        ]),
    entree(
        "D5-SPEC-ASH-MACH", "spécification",
        "Publier la spécification ouverte ASH-MACH : les protocoles gelés "
        "du corpus présentés comme une mini-norme (définitions, conditions "
        "de validité, essais, falsifieurs, format de registre) + safety "
        "case pilote avec certificat de minimalité calculé (forme M2e)",
        "NORM-MACH-1.0", "en-cours",
        "rédiger la spécification (format norme : exigences SHALL, essais "
        "rejouables) + exécuter le safety case pilote de bout en bout",
        {"fondation": "docs/note-directions-normes.md §D5",
         "certificat_modèle": "m2e_copie_tri_verdict.json (corpus)"},
        "si la spécification publiée n'est rejouée par personne en six "
        "mois → la voie D5 est réfutée telle quelle (publié)",
        addenda=[
            {"date": "2026-08-31",
             "action": "production livrée — spécification rédigée au "
                       "format norme + safety case pilote exécuté "
                       "(certificat de minimalité de la copie)",
             "artefacts": ["specs/ash-mach-0.1.md"],
             "note": "fenêtre de rejeu par des tiers ouverte jusqu'au "
                     "2027-02-28 — le falsifieur reste armé : aucune "
                     "rejouabilité tierce sous six mois réfute la voie"},
        ]),
    entree(
        "D6-TABLE-CONFORMITE-AIACT", "spécification",
        "Publier la table de conformité AI Act du corpus : artefacts "
        "mappés sur les art. 9–15 (registre des frontières = gestion des "
        "risques ; D figées = gouvernance des données ; notes SHA = "
        "documentation ; PERT-BATT = robustesse ; le verdict qui refuse "
        "quand Σ chute = supervision humaine effective)",
        "NORM-MACH-1.0", "fermée",
        "produire la table article par article, avec pour chacun "
        "l'artefact du corpus qui le couvre et les écarts publiés",
        {"fondation": "docs/note-directions-normes.md §D6",
         "cadre": "règlement (UE) 2024/1689 modifié par (UE) 2026/1744"},
        "tout écart découvert entre la table et les exigences finales des "
        "normes harmonisées est publié en addendum — jamais corrigé en "
        "silence",
        addenda=[
            {"date": "2026-08-31",
             "action": "production livrée — table v1.0 art. 9–15 avec "
                       "écarts publiés (QMS, plan de surveillance, "
                       "procédure de supervision humaine)",
             "artefacts": ["docs/table-conformite-ai-act.md"]},
        ]),
]


def main():
    blob = json.dumps([e["sha256_entrée"] for e in DIRECTIONS],
                      ensure_ascii=False).encode()
    registre = {
        "registre": "N1-DIRECTIONS-NORMALISATION",
        "protocole": "NORM-REG-1.0 (gelé) — schéma hérité de REG-FR-1.0 "
                     "(registre A4 du corpus)",
        "dépôt": "noetic-normes (privé — prospection avant dépôts externes)",
        "n_entrées": len(DIRECTIONS),
        "par_statut": {s: sum(1 for e in DIRECTIONS if e["statut"] == s)
                       for s in STATUTS},
        "par_type": {t: sum(1 for e in DIRECTIONS if e["type"] == t)
                     for t in TYPES},
        "entrées": DIRECTIONS,
        "sha256_registre": hashlib.sha256(blob).hexdigest(),
    }
    sha_script = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    registre["sha256_script"] = sha_script
    out = Path(__file__).resolve().parent.parent / "data" / "n1_registre_normes.json"
    out.parent.mkdir(exist_ok=True)
    out.write_text(json.dumps(registre, ensure_ascii=False, indent=2),
                   encoding="utf-8")
    print("N1 — REGISTRE DES DIRECTIONS DE NORMALISATION [NORM-REG-1.0]")
    for e in DIRECTIONS:
        print(f"  {e['id']:<26} [{e['type']:<13}] {e['statut']}")
    print(f"\n  {len(DIRECTIONS)} entrées | SHA registre : "
          f"{registre['sha256_registre'][:16]}… | script : {sha_script[:16]}…")
    print(f"  écrit : {out.name}")


if __name__ == "__main__":
    main()
