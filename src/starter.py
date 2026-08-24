import pandas as pd

def inspect_dataset(file_path):
    df = pd.read_csv(file_path)

    print("Shape:", df.shape)

    print("\nColumns:")
    print(df.columns.tolist())

    print("\nMissing values:")
    print(df.isna().sum().sort_values(ascending=False))

    print("\nDuplicate rows:", df.duplicated().sum())

    return df

if __name__ == "__main__":
    print("AgriGuard AI starter script")
    print("Add the documented dataset to data/ before running inspection.")
