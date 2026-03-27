import pandas as pd
import matplotlib.pyplot as plt  

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

# Maaşa göre sırala
df_sorted = df.sort_values(by="salary", ascending=False)

names = df_sorted["name"]
salaries = df_sorted["salary"]

plt.style.use("ggplot")

plt.figure()

# Renk paleti (gradient gibi)
colors = ["#FF6B6B", "#4ECDC4", "#522079", "#57D757"]

bars = plt.bar(names, salaries, color=colors)

# Ortalama çizgi
avg_salary = df["salary"].mean()
plt.axhline(avg_salary, linestyle='--')
plt.text(0, avg_salary, f"Avg: {int(avg_salary)}")

# Değerleri barların üstüne yaz
for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, yval, int(yval),
             ha='center', va='bottom', fontsize=10)

# Başlık ve stil
plt.title("💰 Employee Salary Analysis", fontsize=14)
plt.xlabel("Employees")
plt.ylabel("Salary")

plt.grid(axis='y', linestyle='--', alpha=0.7)

plt.tight_layout()

plt.savefig("salary_chart.png")

plt.show()