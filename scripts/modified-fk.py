import pandas as pd
import numpy as np
from pathlib import Path
from statsmodels.stats.inter_rater import fleiss_kappa, aggregate_raters
from itertools import combinations

def normalization(string):
    return string.lower()

# Load CSVs
raters = ["michael", "alexis", "anmol", "david", "jon"]
dfs = []
for r in raters:
    path = Path(__file__).parent.parent / "deliverables" / "data" / "human-determined-sentiment" / f"{r}-sentiment.csv"
    dfs.append(pd.read_csv(path))

# Stack all raters into matrix
sentiments = np.column_stack([df["sentiment"].to_numpy() for df in dfs])
sentimentsClean = np.where(pd.isna(sentiments), "missing", sentiments).astype(str)

# Normalize
for row_idx, row in enumerate(sentimentsClean):
    for col_idx, item in enumerate(row):
        sentimentsClean[row_idx][col_idx] = normalization(item)

def compute_fk_for_subset(indices, sentimentsClean):
    """Compute Fleiss’ kappa for a subset of raters given by indices."""
    sub = sentimentsClean[:, indices]
    counts, cats = aggregate_raters(sub)
    return fleiss_kappa(counts)

results = []

# Try all combinations of 3 and 4 raters
for r in [3, 4]:
    for combo in combinations(range(len(raters)), r):
        fk = compute_fk_for_subset(combo, sentimentsClean)
        results.append({
            "raters": [raters[i] for i in combo],
            "kappa": fk
        })

# Sort by kappa descending
results_sorted = sorted(results, key=lambda x: x["kappa"], reverse=True)

# Pick top k (say top 5)
top_k = 55
count = 0
for res in results_sorted[:top_k]:
    count+=1
    print(f"{count}-Raters: {res['raters']}  |  Fleiss’ kappa: {res['kappa']:.4f}")
    