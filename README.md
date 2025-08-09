[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.16785841.svg)](https://doi.org/10.5281/zenodo.16785841)

# Multidimensional Wave Structure — Code & Data

This repository provides **data and code** to reproduce the figures and core results in:

> Nachev, K. (2025). *Multidimensional Wave Structure: Dimensional Scaling from Quantum to Cosmological Phenomena*.

## What’s inside
- `src/` — core equations and plotting utilities
- `notebooks/` — one notebook per figure
- `figures/` — publication-ready PDFs
- `data/` — inputs or pointers to public sources
- `paper/` — LaTeX sources (optional)

## Quick start
```bash
# Option A: conda
conda env create -f environment.yml
conda activate mws

# Option B: pip
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
```

## Reproduce all figures
```bash
python -m src.reproduce_all
```

## Outputs
- `figures/fig_projection_schematic_unified.pdf`
- `figures/fig_energy_scaling_unified.pdf`
- `figures/fig_curvature_scaling_unified.pdf`
- `figures/combined_dimensional_dependencies_unified.pdf`

## License and citation
- Code and materials: Licensed under **Creative Commons Attribution-NonCommercial 4.0 International (CC BY-NC 4.0)**.
- This means you are free to share and adapt the material for **non-commercial** purposes, with proper attribution.
- Commercial use is **not permitted** without explicit written permission from the author.
- Cite via DOI: [10.5281/zenodo.16785841](https://doi.org/10.5281/zenodo.16785841)

## Contact
Kaloyan Nachev — National Academy of Arts, Sofia
