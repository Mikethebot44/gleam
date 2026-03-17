# GLEAM Source Detection

U-Net baseline for radio source detection on GLEAM / MWA FITS tiles.

## Repo layout

- `data/raw/` FITS tiles and source catalogues
- `data/processed/` derived NumPy patches and masks
- `notebooks/` exploration, baseline, training, evaluation
- `src/` reusable training and postprocessing code
- `models/` checkpoints

## Setup

```bash
conda env create -f environment.yml
conda activate gleam-unet
python -m ipykernel install --user --name gleam-unet --display-name "Python (gleam-unet)"
jupyter lab# gleam
