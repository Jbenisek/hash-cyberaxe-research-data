# HASH$CyberAxe research data

> **By Jeremy Benisek ([CyberAxe](https://cyberaxe.dev/))** · part of **[HASH$CyberAxe](https://hashcyberaxe.com/)** open research
>
> Research library: [hashcyberaxe.com](https://hashcyberaxe.com/) · Tools & data: [hashcyberaxe.com/tools.html](https://hashcyberaxe.com/tools.html) · Play the game: [hashcyberaxe.com/game](https://hashcyberaxe.com/game/)

**What this is for.** The research data behind the HASH$CyberAxe library: 1,227,001 typed scientific cell records, the historical experiment tables, the exact-source bundles, the library's machine indexes and the readable field guides. This repository holds the schemas, manifests, a verifier and a cell reader; the large archives are attached to its Release. Use it to analyse the data yourself, check a result against its saved records, or build on the cell format.

**Credits.** Author: **Jeremy Benisek (CyberAxe)**: research direction, questions and project lead. Made with AI research and coding agents working under CyberAxe's direction; the agents are tools, not authors. Third-party code keeps its original authors and notices ([AUTHORS.md](AUTHORS.md)).

**License.** See [LICENSING.md](LICENSING.md). Credit: "Jeremy Benisek (CyberAxe), HASH$CyberAxe, https://hashcyberaxe.com/".

Versioned scientific tables, cell records, schemas, source identities and readable guide exports from the public research library. The small repository contains manifests and inspection tools; large ZIPs belong in GitHub Releases, not in Git history.

## What is available

- **cellbook**: Typed scientific records, source appearances, schemas and joined indexes. 4,418 files; 230,726,712 archive bytes.
- **bulk-tables**: Published game, lattice and experiment tables with historical source paths. 12 files; 51,483,614 archive bytes (public edition: other teams' material, AI agent session notes and audits, and slur-list scripts left out).
- **exact-source-bundles**: Exact-source ZIP bundles, extraction indexes and retained unpacked browser sources. 221 files; 449,308,661 archive bytes (public edition: other teams' material, AI agent session notes and audits, and slur-list scripts left out).
- **library-indexes**: Catalogue, toolkit, guides, trajectories and other published machine indexes. 684 files; 26,653,636 archive bytes.
- **supporting-downloads**: Published non-ZIP source instructions, numerical tables and example checkers. 129 files; 6,963,114 archive bytes.
- **field-guide-exports**: Readable HTML, JSON and Markdown guide exports. 21,625 files; 36,640,180 archive bytes.

The cellbook edition contains 1,227,001 typed records in 373 groups and 1,265,678 source appearances. The intake tracks 5,898 imported sources and 100 pending adapters. Source appearances and typed records are different units; saved statuses retain their historical meaning. See CELLBOOK_SUMMARY.json and cell-record.schema.json.

## Download and verify

Requires Python 3.11 or newer, standard library only. Put release downloads together in a folder, then from this repository run:

```sh
python -B verify_release.py --self-test
python -B verify_release.py RELEASE_DIRECTORY
python -B verify_release.py RELEASE_DIRECTORY --dataset cellbook
```

The verifier checks asset hashes, exact archive membership, every file size and SHA-256. It never executes archived code. Each archive preserves its published paths. Extract multiple assets into the same empty folder if you need their indexes and data together.

## Inspect cells without extracting

```sh
python -B list_cells.py RELEASE_DIRECTORY/HASH-CyberAxe-cellbook-2026-11-05.zip
python -B list_cells.py RELEASE_DIRECTORY/HASH-CyberAxe-cellbook-2026-11-05.zip --group g0 --limit 3
```

The first command lists groups. The second prints three JSON records after checking their chunk hash. Fields, provenance IDs, recorded status and publication holds remain visible; do not discard those when comparing experiments.

## Source

Prepared from the HASH$CyberAxe research library (https://hashcyberaxe.com/) by its publication process; `PROJECT.json` and `ORIGINAL_FILES.json` record the original archive and file identities.

## Website integration

Download links can be connected once release URLs exist. Interactive browser use additionally requires tested cross-origin and byte-range behavior; a working download is not proof of those capabilities. The current library remains unchanged until that integration passes.

## Guide-export editorial edition

The optional guide export uses the current research-first presentation. Source identities, target/model fields and execution metadata are retained. JSON and Markdown match the current guide shards by id; original code/source blocks and stylesheets remain unchanged. EDITORIAL_EDITION.json records the member counts, shard identities and the original asset SHA-256 d144e9ef8bf2466abb2d22154b5943ebab30d2ed6204eec06f5dde636e0d9666. Other raw-data release assets retain their original bytes.

## Guide-export editorial edition

The optional guide export uses the current research-first presentation. Source identities, target/model fields and execution metadata are retained. JSON and Markdown match the current guide shards by id; original code/source blocks and stylesheets remain unchanged. EDITORIAL_EDITION.json records the member counts, shard identities and the original asset SHA-256 d144e9ef8bf2466abb2d22154b5943ebab30d2ed6204eec06f5dde636e0d9666. Other raw-data release assets retain their original bytes.

**Public edition.** 4 files were edited for this edition: the exact-source release zip rebuilt without other teams' boards, AI agent session notes and slur-list scripts. [PUBLIC_EDITION_EDITS.json](PUBLIC_EDITION_EDITS.json) lists each file, why, and its original SHA-256.
