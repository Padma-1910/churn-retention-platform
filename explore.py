from src.data import load_raw

df = load_raw()

print("Shape:", df.shape)
print("\nColumns:\n", list(df.columns))
print("\nFirst 5 rows:\n", df.head())
print("\nInfo:")
df.info()
print("\nMissing values:\n", df.isna().sum())

# Find the churn column (name may differ in the cleaned file)
churn_cols = [c for c in df.columns if "churn" in c.lower()]
print("\nChurn column(s):", churn_cols)
for c in churn_cols:
    print(df[c].value_counts(normalize=True))
