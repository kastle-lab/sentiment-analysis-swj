import pandas as pd
import numpy as np
from pathlib import Path
from statsmodels.stats.inter_rater import fleiss_kappa, aggregate_raters


ir1 = Path(__file__).parent.parent / 'deliverables' / 'data' / 'human-determined-sentiment'/ 'michael-sentiment.csv'
ir2 = Path(__file__).parent.parent / 'deliverables' / 'data' / 'human-determined-sentiment'/ 'alexis-sentiment.csv'
ir3 = Path(__file__).parent.parent / 'deliverables' / 'data' / 'human-determined-sentiment'/ 'anmol-sentiment.csv'
ir4 = Path(__file__).parent.parent / 'deliverables' / 'data' / 'human-determined-sentiment'/ 'david-sentiment.csv'
ir5 = Path(__file__).parent.parent / 'deliverables' / 'data' / 'human-determined-sentiment'/ 'jon-sentiment.csv'

df1 = pd.read_csv(ir1)
df2 = pd.read_csv(ir2)
df3 = pd.read_csv(ir3)
df4 = pd.read_csv(ir4)
df5 = pd.read_csv(ir5)

sentiments = np.column_stack([df1['sentiment'].to_numpy(), df2['sentiment'].to_numpy(), df3['sentiment'].to_numpy(), df4['sentiment'].to_numpy(), df5['sentiment'].to_numpy()])
sentimentsClean =  np.where(pd.isna(sentiments), "missing", sentiments).astype(str)

# print(sentimentsClean)
counts, cats = aggregate_raters(sentimentsClean) 
fkScore = fleiss_kappa(counts)                    
# print(counts)

print(fkScore)