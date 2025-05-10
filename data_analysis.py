import pandas as pd
import matplotlib.pyplot as plt

file_path = r"C:\Users\marka\Downloads\Attachment-Statistical_Tables_for_April_2025_Wholesale Prices_Cereals.xlsx"
df = pd.read_excel(file_path, sheet_name="Table 1_RiceSpecial", skiprows=4)

df = df.iloc[3:].copy()

df = df.rename(columns={
    "Unnamed: 9": "April_2025_Price",
    "Region/Province": "Region"
})

df["April_2025_Price"] = pd.to_numeric(df["April_2025_Price"], errors='coerce')
df = df.dropna(subset=["April_2025_Price"])

plt.figure(figsize=(10, 6))
plt.hist(df["April_2025_Price"], bins=10, color="skyblue", edgecolor="black")
plt.title("Histogram of April 2025 Wholesale Prices (Rice Special)")
plt.xlabel("Price (PhP/kg)")
plt.ylabel("Number of Regions/Provinces")
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()
