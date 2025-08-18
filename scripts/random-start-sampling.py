import pandas as pd
import random
from pathlib import Path

# Input and output file paths
input_file = Path(__file__).parent.parent / 'deliverables' / 'data' /  'non-reviewed-assessments-base.csv'
output_file = Path(__file__).parent.parent / 'deliverables' / 'data' /  'initial-sample-human-reviewed-assessments.md' 

# Read CSV file 
df = pd.read_csv(input_file)

# Random Start Systematic Sampling
P = len(df)         # population size
n = 20              # sample size
k = P // n          # sampling interval

# Random start between index 0 and 4
start = random.randint(0, k-1)

# Select every k-th item starting from start
sampled_indices = list(range(start, start + n * k, k))
sampled_df = df.iloc[sampled_indices]

# Step 3: Save results as a markdown file
sampled_df_md = sampled_df.to_markdown(index=False)
with open(output_file, "w") as f:
    f.write(sampled_df_md)