import pandas as pd

# JSON oku
df = pd.read_json("data.json")

print("İlk veri:")
print(df)

# Eksik veriler
print("\nEksik veriler:")
print(df.isnull().sum())

# Temizleme
df["age"] = df["age"].fillna(df["age"].mean())
df["salary"] = df["salary"].fillna(df["salary"].mean())
df["city"] = df["city"].replace("", "Unknown")

print("\nTemizlenmiş veri:")
print(df)

# Analiz
print("\nOrtalama maaş:", df["salary"].mean())
