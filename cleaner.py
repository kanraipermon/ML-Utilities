import pandas as pd
from sklearn.feature_selection import VarianceThreshold

def clean(path, out, strategy='median'):
    df = pd.read_csv(path)
    # drop duplicates
    df = df.drop_duplicates()
    # fill missing values
    numeric = df.select_dtypes(include=['number']).columns
    for c in numeric:
        if df[c].isna().any():
            if strategy == 'mean':
                df[c] = df[c].fillna(df[c].mean())
            elif strategy == 'median':
                df[c] = df[c].fillna(df[c].median())
            else:
                df[c] = df[c].fillna(df[c].mode().iloc[0])
    # remove low-variance numeric cols
    selector = VarianceThreshold(threshold=0.0)
    numeric_df = df[numeric].fillna(0)
    try:
        selector.fit(numeric_df)
        vars = selector.get_support(indices=True)
        keep = [numeric[i] for i in vars]
        # keep non-numeric columns too
        others = [c for c in df.columns if c not in numeric]
        df = df[keep + others]
    except Exception:
        pass
    df.to_csv(out, index=False)
    print('Cleaned dataset saved to', out)
