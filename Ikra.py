import pandas as pd
import matplotlib.pyplot as plt

# 1. Cədvəli oxuyuruq
df = pd.read_csv("orders.csv")

print("--- ÜMUMI MƏLUMAT ---")
print(df.info())

# 2. Gəlir və Mənfəət Hesablaması
price_usd_cem = df["price_usd"].sum()
cogs_usd_cem = df["cogs_usd"].sum()
qazanc = price_usd_cem - cogs_usd_cem

print(f"\nÜmumi Xalis Qazanc (Mənfəət): ${qazanc:,.2f}")

# 3. Səbətdəki orta məhsul sayı
orta_mehsul = df["items_purchased"].mean()
print(f"Bir sifarişə düşən orta məhsul sayı: {orta_mehsul:.2f}")

# 4. Hər məhsul üzrə sifariş sayı
result = df.groupby("primary_product_id")["order_id"].count()
print("\nMəhsullar üzrə sifariş sayı:")
print(result)

# ==========================================
# 5. VİZUALLAŞDIRMA (Qrafik Hissəsi)
# ==========================================
product_counts = df["primary_product_id"].value_counts().sort_index()

# Qrafiki parametrləri ilə birlikdə qururuq
plt.figure(figsize=(8, 5))
product_counts.plot(kind="bar", color="skyblue", edgecolor="black")

plt.title("Maven Fuzzy Factory - Əsas Məhsullar Üzrə Sifariş Sayı", fontsize=12, fontweight='bold')
plt.xlabel("Məhsul ID-si", fontsize=10)
plt.ylabel("Sifariş Sayı", fontsize=10)
plt.xticks(rotation=0)
plt.grid(axis="y", linestyle="--", alpha=0.7)

# Qrafiki ekranda göstər
plt.tight_layout()
plt.show()