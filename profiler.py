import pandas as pd

def profile(path):
    df = pd.read_csv(path)
    print('Rows:', len(df))
    print('Columns:', len(df.columns))
    print('\nColumn types:')
    print(df.dtypes)
    print('\nMissing values per column:')
    print(df.isna().sum())
    # If there is a 'label' column, show distribution
    if 'label' in df.columns:
        print('\nLabel distribution:')
        print(df['label'].value_counts())
