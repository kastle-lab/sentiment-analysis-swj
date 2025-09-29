import pandas as pd
import numpy as np
from pathlib import Path
from itertools import combinations
from statsmodels.stats.inter_rater import fleiss_kappa, aggregate_raters

def normalization(string):
    return string.lower()

# --- Load CSVs ---
raters = ["michael", "alexis", "anmol", "david", "jon"]
dfs = []
for r in raters:
    path = Path(__file__).parent.parent / "deliverables" / "data" / "human-determined-sentiment" / f"{r}-sentiment.csv"
    dfs.append(pd.read_csv(path))

sentiments = np.column_stack([df["sentiment"].to_numpy() for df in dfs])
sentimentsClean = np.where(pd.isna(sentiments), "missing", sentiments).astype(str)

# Normalize
for row_idx, row in enumerate(sentimentsClean):
    for col_idx, item in enumerate(row):
        sentimentsClean[row_idx][col_idx] = normalization(item)

def compute_fk(indices):
    sub = sentimentsClean[:, indices]
    counts, cats = aggregate_raters(sub)
    return fleiss_kappa(counts)

# --- Compute all 3- and 4-rater combos ---
results = []
for r in [3, 4]:
    for combo in combinations(range(len(raters)), r):
        fk = compute_fk(combo)
        results.append({
            "raters": [raters[i] for i in combo],
            "kappa": fk
        })

# --- Sort descending, filter positives ---
results_sorted = sorted([res for res in results if res["kappa"] > 0],
                        key=lambda x: x["kappa"], reverse=True)

# Show top N results
top_k = 5
print(f"\nTop {top_k} highest κ subsets:")
for res in results_sorted[:top_k]:
    print(f"  Raters: {res['raters']} | Fleiss’ κ = {res['kappa']:.4f}")

# --- Analyze which raters drag agreement down ---
avg_with = {r: np.mean([res["kappa"] for res in results if r in res["raters"]])
            for r in raters}
avg_without = {r: np.mean([res["kappa"] for res in results if r not in res["raters"]])
               for r in raters}

print("\nAverage κ with vs without each rater:")
for r in raters:
    print(f"  {r:<8} | with: {avg_with[r]:.3f} | without: {avg_without[r]:.3f} | diff: {avg_without[r]-avg_with[r]:.3f}")
