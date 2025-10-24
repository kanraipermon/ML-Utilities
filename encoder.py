import pandas as pd
from sklearn.preprocessing import LabelEncoder

def encode(path, cols, out):
    df = pd.read_csv(path)
    for c in cols:
        if c not in df.columns:
            raise ValueError(f'Column {c} not in CSV')
        le = LabelEncoder()
        df[c] = le.fit_transform(df[c].astype(str))
    df.to_csv(out, index=False)
    print('Encoded columns saved to', out)
