#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 23 14:37:21 2025

@author: niharpattanayak
"""
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

df=pd.read_csv('/Users/niharpattanayak/Documents/e_commerce.csv')

df.shape # find no. of rows[50000 rows 13 cols]
print(df.dtypes)
df.info()
df.isnull().sum()
print(df.mean(numeric_only=True))
print(df.median(numeric_only=True))
print(df.std(numeric_only=True))
df.describe()
df['total_revenue'].sum()
prd=df.groupby('product_category')['total_revenue'].sum()
prd.head()
reg=df.groupby('customer_region')['total_revenue'].sum()
max_revenue = df['total_revenue'].max()
print(max_revenue)
min_reveneu=df['total_revenue'].min()
sold_per_product=df.groupby("product_category")["quantity_sold"].sum()#.sort_values(ascending=False)
discount_per_product=df.groupby('product_category')['discounted_price'].sum()
top_ratings=df.groupby('product_category')['rating'].sum()
top_pay=df['payment_method'].value_counts().head(3)
upi_reg=df.groupby('customer_region')['payment_method'].apply(lambda x: x.value_counts().head(3))


df.groupby("product_category")["total_revenue"].sum().plot(kind="bar")
plt.title("Revenue by Product Category")
plt.show()

df.groupby('customer_region')['total_revenue'].sum().plot(kind='bar')
plt.title('revenue by region')
plt.show()

df.groupby('product_category')['quantity_sold'].sum().plot(kind='bar')
plt.title('quantitysold per product')
plt.show()

df.groupby('product_category')['discounted_price'].sum().plot(kind='bar')
plt.title('discount per product')
plt.show()

df.groupby('product_category')['rating'].sum().plot(kind='bar')
plt.title('rating per product')
plt.show()

