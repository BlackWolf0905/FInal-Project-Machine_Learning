import pandas as pd
from pathlib import Path

RAW_DIR = Path("../data/raw")

files = {
    "customers": "customers.csv",
    "transactions": "transactions.csv",
    "transaction_items": "transaction_items.csv",
    "products": "products.csv",
    "customer_support": "customer_support.csv",
    "marketing_touchpoints": "marketing_touchpoints.csv",
    "stores": "stores.csv",
}

def load_data():
    dfs = {}
    for name, filename in files.items():
        path = RAW_DIR / filename
        df = pd.read_csv(path, na_values=["", "NA", "N/A", "-", ".", "null", "NULL"])
        dfs[name] = df
    return dfs

def audit_df(name, df):
    print("=" * 80)
    print(f"{name.upper()}")
    print("=" * 80)
    print(f"Shape: {df.shape}")
    print("\nColumns:")
    print(df.columns.tolist())

    print("\nDtypes:")
    print(df.dtypes)

    print("\nMissing values:")
    print(df.isna().sum().sort_values(ascending=False))

    print("\nMissing rate (%):")
    print((df.isna().mean() * 100).round(2).sort_values(ascending=False))

    print("\nDuplicate rows:", df.duplicated().sum())

    print("\nSample rows:")
    print(df.head(3))

    print("\nNumeric summary:")
    num_cols = df.select_dtypes(include=["number"]).columns
    if len(num_cols) > 0:
        print(df[num_cols].describe().T)
    else:
        print("No numeric columns.")

    print("\nCategorical summary:")
    cat_cols = df.select_dtypes(include="object").columns
    if len(cat_cols) > 0:
        print(df[cat_cols].describe().T)
    else:
        print("No categorical columns.")

def main():
    dfs = load_data()
    for name, df in dfs.items():
        audit_df(name, df)

if __name__ == "__main__":
    main()