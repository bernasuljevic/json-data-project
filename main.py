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

import matplotlib.pyplot as plt

# İsim ve maaşları al
names = df["name"]
salaries = df["salary"]

# Grafik oluştur
plt.figure()
plt.bar(names, salaries)

# Başlık ve etiketler
plt.title("Çalışan Maaş Grafiği")
plt.xlabel("İsim")
plt.ylabel("Maaş")

# Göster
plt.show()