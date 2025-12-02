# Drug Response Analysis (in-progress)

Status: in progress

## Tech stack
Python, TensorFlow, scikit-learn, Pandas, NumPy, SciPy, Matplotlib

## Project summary
A machine learning pipeline to predict drug efficacy (continuous response) from synthetic biological datasets.
This repo demonstrates data generation, preprocessing, feature extraction, a scikit-learn baseline, and a TensorFlow model.
It is intended as a clear, reproducible scaffold that you can adapt to real drug-response datasets later.

## Run the demo (local)
1. Create and activate a virtual environment
```
python -m venv venv
source venv/bin/activate  # macOS / Linux
venv\Scripts\activate   # Windows
pip install -r requirements.txt
```
2. Run the pipeline on the included synthetic dataset
```
python src/pipeline.py --data data/synthetic_drug_response.csv --out_dir results/demo --target response
```
3. Open `notebooks/drug_response_demo.ipynb` for an interactive walkthrough.

## Repo structure
```
drug-response-analysis/
├─ data/                   # raw and processed datasets (do not commit large files)
├─ notebooks/              # exploratory analysis and figures
├─ src/
│  ├─ pipeline.py          # main pipeline and CLI
│  ├─ data_utils.py        # loading and preprocessing helpers
│  ├─ features.py          # feature extraction functions
│  ├─ models.py            # sklearn and TF model definitions
│  └─ eval.py              # metrics and plotting
├─ requirements.txt
├─ README.md
└─ .gitignore
```

## Notes
- The dataset here is synthetic. Replace `data/synthetic_drug_response.csv` with real data for practical use.
- Keep experiments reproducible by fixing random seeds.
- Add domain-specific feature engineering for real datasets (e.g., normalization by housekeeping genes, encoding cell lines, etc.).
