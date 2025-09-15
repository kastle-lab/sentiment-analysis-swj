import pandas as pd
import random
from pathlib import Path

# Input and output file paths
names = ["michael", "alexis", "david", "anmol", "jon"]
input_file = Path(__file__).parent.parent / 'deliverables' / 'data' / 'non-reviewed-assessments-base.csv'


# Read CSV file 
df = pd.read_csv(input_file)

# Random Start Systematic Sampling
P = len(df)         # population size
n = 20              # sample size
k = P // n          # sampling interval

# Random start between index 0 and 4
start = random.randint(0, k-1)

# Select every k-th item starting from start
sampled_indices = list(range(1, start + n * k, k))
sampled_df = df.iloc[sampled_indices]
sampled_df['pos-tally'] = ''
sampled_df['neutral-tally'] = ''
sampled_df['neg-tally'] = ''

# Step 3: Save results as a markdown file
for name in names:
    output_file = Path(__file__).parent.parent / 'deliverables' / 'data' / 'human-determined-sentiment' /  f'{name}-sentiment.csv' 
    sampled_df.to_csv(output_file, index=False)

