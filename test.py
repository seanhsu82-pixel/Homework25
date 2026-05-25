import pandas as pd

df = pd.read_csv("Grocery_Inventory_and_Sales_Dataset.csv")

df.columns = df.columns.str.strip()

df["Unit_Price"] = pd.to_numeric(df["Unit_Price"], errors="coerce")
df["Sales_Volume"] = pd.to_numeric(df["Sales_Volume"], errors="coerce")
df["Stock_Quantity"] = pd.to_numeric(df["Stock_Quantity"], errors="coerce")

df["Total_Inventory_Value"] = df["Stock_Quantity"] * df["Unit_Price"]

best = df.loc[df["Sales_Volume"].idxmax()]
print("最暢銷：", best["Product_Name"])

df["Discount_Revenue"] = df["Sales_Volume"] * df["Unit_Price"] * 0.9

print(df[["Product_Name", "Discount_Revenue"]])