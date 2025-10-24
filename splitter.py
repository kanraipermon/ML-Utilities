import pandas as pd
from sklearn.model_selection import train_test_split
import os

def split(path, target, train_frac, out_dir):
    df = pd.read_csv(path)
    if target not in df.columns:
        raise ValueError(f"Target column '{target}' not found.")
    train, test = train_test_split(df, train_size=train_frac, stratify=df[target], random_state=42)
    os.makedirs(out_dir, exist_ok=True)
    train.to_csv(os.path.join(out_dir, 'train.csv'), index=False)
    test.to_csv(os.path.join(out_dir, 'test.csv'), index=False)
    print('Wrote train.csv and test.csv to', out_dir)
