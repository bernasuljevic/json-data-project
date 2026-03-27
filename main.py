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

plt.figure()

bars = plt.bar(names, salaries)

# Ortalama çizgisi
avg_salary = df["salary"].mean()
plt.axhline(avg_salary, linestyle='--')
plt.text(0, avg_salary, f"Avg: {int(avg_salary)}")

# Değerleri yaz
for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, yval, int(yval), ha='center', va='bottom')

plt.title("Employee Salary Analysis")
plt.xlabel("Employees")
plt.ylabel("Salary")

plt.grid()

plt.savefig("salary_chart.png")

plt.show()