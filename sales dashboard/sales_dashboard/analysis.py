
import pandas as pd

df = pd.read_csv('sales_data.csv')

print("Total Sales:", df['sales'].sum())
print("\nSales by Region:")
print(df.groupby('region')['sales'].sum())

print("\nTop Products:")
print(df.groupby('product')['sales'].sum().sort_values(ascending=False))
