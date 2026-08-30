# Fiche d'instrument à verdict algorithmique — gabarit OIML/WELMEC

**Version 0.1 — 31 août 2026 — direction D4 du registre N1 (noetic-normes)**
**Objet : fiche de domaine mesuré obligatoire pour les instruments dont la
fonction principale est un verdict algorithmique (classification,
détection de régime, diagnostic) — complément logiciel à OIML D 31:2023
et WELMEC 7.2.**

---

## 1. Identification de l'instrument

| Champ | Contenu |
|---|---|
| Désignation | Chaîne ASH → M̂ (analyseur spectral à géométrie harmonique + opérateur de verdict) |
| Version logicielle | ASH v1.1.0 (`sha256:2d0b83bb857a…`) ; noyau audité v1.0.0 (`sha256:338dbda7b499fdc8…`) |
| Fonction | Extraction d'invariants topologiques de signaux temporels (Rc, Rtop, Rdyn, E1..E7) et verdict (V, Σ) |
| Intégrité | OIML D 31 §5.1 — empreinte de chaque module, audit trail SHA-256 (`SHASUMS.txt` du dépôt) |

## 2. Domaine de validité mesuré (obligatoire)

L'instrument DOIT déclarer, pour chaque condition, la valeur mesurée et
l'essai qui l'a établie.

| # | Condition | Valeur mesurée | Essai |
|---|---|---|---|
| V1 | Entrée | série temporelle 1D, fréquence d'échantillonnage déclarée | structurel |
| V2 | Bande utile | [f₀, f₀·2^N_oct] = [1 Hz, 30,2 Hz] (N_oct = 5) ; rejet hors grille (interpolation nulle) | P43-C5 (porteuse 48 Hz lue comme enveloppe 2 Hz sur grille 5 octaves) |
| V3 | Résolution effective | δf_eff(f) = max(2^(1/12) − 1 ≈ 5,9 %, (f_s/nperseg)/f) | P43 : tons à 3 % non résolus ; tons à 41 % fusionnés à 2–7 Hz (nperseg = 250), résolus à 20–68 Hz |
| V4 | Récurrence minimale | ≥ ~8 événements par fenêtre ; une paire n'a pas de porteuse lisible | P43-C5 (2 spikes → pic aléatoire ; 11 spikes → ±1 note) |
| V5 | Tâche admise | détection / classification de structure ; **exclue** : métrologie d'amplitude (ReN ∝ 1/amplitude, non portable — pente mesurée −0,996) | P43-C3 / P45-C2 |
| V6 | Stabilité du verdict | Σ = 1,00 sur la batterie de référence (11 protocoles) ; fragilités publiées avec axes (S1 : nperseg ; S4 : f₀, N_oct) | PERT-BATT exécutée |

## 3. Invariants et interprétation

| Invariant | Définition (formule fermée) | Invariance d'échelle |
|---|---|---|
| Rc | énergie spectrale totale sur la grille | **non** — sonde d'énergie relative, pas un étalon |
| Rtop | pics locaux > 10 % du max | oui (≤ 1e-9, P45-C2) |
| Rdyn | écart-type normalisé des rapports log inter-pics (convention : 1,0 si < 2 pics) | oui |
| E1..E7 | énergie par octave, normalisée L2 | oui |
| ReN | ((Rdyn+ε)·(Rtop·D))/(Rc·(H+ε))×100 | **non** — ∝ 1/amplitude ; usage : indicateur à gain fixe déclaré uniquement |

## 4. Coût et temps de traitement (mesuré)

| Propriété | Valeur mesurée | Essai |
|---|---|---|
| Temps par fenêtre | constant (ratio max/min ×1,1 de 8 s à 128 s de signal) | P43-C1 |
| Mémoire par fenêtre | constante (ratio ×1,0) | P43-C1 |
| Dépendances | aucune (FFT maison en C++, cible STM32/ESP32) | inspection |

## 5. Limites publiées (B3-FAIL)

1. ReN non invariant d'échelle — les régimes associés sont retirés de la
   classification officielle (F16, ouverte : fermeture = ReN normalisé).
2. Résolution bornée par l'estimateur de Welch à basse fréquence — une
   série harmonique vraie peut être lue comme sa sous-série d'octaves.
3. Lisibilité nulle sous ~8 événements par fenêtre.
4. Lecture de l'imagerie motrice EEG en essai unique réfutée à zéro
   paramètre (P44 : 0,540/0,520 vs seuil pré-enregistré 0,60).
5. Trace brute dominée par la forme d'onde — l'analyse des trains
   d'événements exige le peigne aux temps d'événements (méthode figée).

## 6. Falsifieurs exécutables déposés

1. Toute exécution de `p43_ash_sous_machine.py` (sha256 a834ff0c…) sur
   les données figées donnant un couple (V, Σ) différent réfute la
   conformité de l'instrument à ASH-MACH-1.0.
2. Toute mesure d'invariance d'échelle des invariants normalisés >
   1e-9 (balayage ×0,01–×100) réfute la colonne 3 du tableau §3.
3. Toute suite d'événements < 8 par fenêtre produisant une porteuse
   lisible à ±1 note réfute V4.

## 7. Traçabilité

| Artefact | Empreinte |
|---|---|
| Noyau audité v1.0.0 | `338dbda7b499fdc8…` (byte-identique au blob git `c9dd73c2…`) |
| Verdict d'audit P43 | `p43_ash_sous_machine_verdict.json` |
| Table de référence v1.1.0 | `table_bench_v110.csv` (sha256 `1c9430c6…`) |
| Errata F16/F18 | `docs/ERRATUM-F16-F18.md` (noetic-ash) |

*Cette fiche est le gabarit proposé à OIML/WELMEC pour la catégorie
« instrument à verdict algorithmique ». Elle s'adosse au cas D1 (DCC
étendu auto-émis, `specs/dcc-etendu-ash-mach-0.1.xml`) avant contact
officiel. Toute objection technique est publiée dans le registre N1.*
