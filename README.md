# ML Utilities

A lightweight collection of command-line and Python utilities for common Machine Learning dataset tasks: profiling, cleaning, splitting, and basic encoding. Ready to publish on GitHub (includes LICENSE, examples, and a ZIP release).

## Features
- `ml_utils profiler` — quick dataset profiling (rows, columns, missing values, datatypes, class distribution)
- `ml_utils cleaner` — simple data cleaning (drop duplicates, fill missing with mean/median/mode, remove low-variance cols)
- `ml_utils split` — stratified train/test splitter that supports CSV input
- `ml_utils encode` — label encoding for categorical columns
- Example Jupyter notebook and `sample.csv` included

## Installation (local)
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
pip install -e .
```

## Quick CLI Examples
```bash
# Profile dataset
ml_utils profiler sample.csv

# Clean dataset and save
ml_utils cleaner sample.csv --out cleaned.csv --strategy mean

# Create stratified split
ml_utils split sample.csv --target label --train 0.8 --out-dir splits/

# Encode labels in-place
ml_utils encode sample.csv --cols category_1,category_2 --out encoded.csv
```

## Publishing to GitHub & GitHub Sponsors
1. Create a new repository on GitHub named `ml-utilities`.
2. Upload the files or push via `git`:
```bash
git init
git add .
git commit -m "Initial commit: ML Utilities"
git branch -M main
git remote add origin git@github.com/kanraipermon/ml-utilities.git
git push -u origin main
```
3. Create a Release and attach the ZIP (this file is ready in this package as `ml-utilities.zip`). GitHub Sponsors setup is available in your account settings under "Sponsors". Add a `FUNDING.yml` in `.github/` if you want automated sponsor buttons (example in docs).

## License
MIT — see LICENSE file.

---
For more advanced features (visual reports, integration with pandas-profiling, or a web UI), feel free to ask and I can extend the repo.
