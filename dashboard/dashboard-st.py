# Import Library
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

st.set_option('client.showErrorDetails', False)

#Import data
df_all = pd.read_csv("df_all.csv")
q1_top = pd.read_csv("q1_top.csv")
q1_down = pd.read_csv("q1_down.csv")
q2_a = pd.read_csv("q2_a.csv")
q2_b = pd.read_csv("q2_b.csv")
q3_sorted = pd.read_csv("q3_sorted.csv")
q4_sorted = pd.read_csv("q4_sorted.csv")

st.write("""
# E-Commerce Dashboard Analysis
Aplikasi ini untuk **Proyek Akhir Analisis Data dengan Python Dicoding**!""")
st.write('---')

#Question 1
st.header('Top Order Count by Product Category')
# Membuat barplot horizontal
plt.figure(figsize=(10, 6))
plt.barh(q1_top['product_category_name_english'], q1_top['order_id'], color='skyblue')

# Memberikan label sumbu
plt.xlabel('Order Count')
plt.ylabel('Product Category')

# Menampilkan plot
plt.gca().invert_yaxis()
st.pyplot(plt)
st.write('---')

# Membuat barplot horizontal
st.header('Lowest Order Count by Product Category')
plt.figure(figsize=(10, 6))
plt.barh(q1_down['product_category_name_english'], q1_down['order_id'], color='skyblue')

# Memberikan label sumbu
plt.xlabel('Order Count')
plt.ylabel('Product Category')

# Menampilkan plot
plt.gca().invert_yaxis()
st.pyplot(plt)
st.write('---')

# Question 2
st.header('Number of Customer for each city')

# Membuat barplot horizontal
plt.figure(figsize=(10, 6))

q2_a_max = q2_a['customer_id'].max()
colors = ['skyblue' if value == q2_a_max else 'gray' for value in q2_a['customer_id']]

plt.bar(q2_a['customer_city'], q2_a['customer_id'], color=colors)

# Memberikan label sumbu
plt.xlabel('Customer City')
plt.xticks(rotation=45)
plt.ylabel('Number of Customer')

# Menampilkan plot
st.pyplot(plt)
st.write('---')

# Membuat barplot horizontal
st.header('Number of seller for Each City')
plt.figure(figsize=(10, 6))

q2_b_max = q2_b['seller_id'].max()
colors = ['skyblue' if value == q2_b_max else 'gray' for value in q2_b['seller_id']]

plt.bar(q2_b['seller_city'], q2_b['seller_id'], color=colors)

# Memberikan label sumbu
plt.xlabel('Seller City')
plt.xticks(rotation=45)
plt.ylabel('Number of Seller')

# Menampilkan plot
st.pyplot(plt)
st.write('---')

# Question 3
# Membuat barplot horizontal
st.header('Number of Order for Each Months in 2017')
plt.figure(figsize=(10, 6))
plt.plot(q3_sorted['Months'], q3_sorted['Count'], color='skyblue', marker='o')

# Memberikan label sumbu
plt.xlabel('Months')
plt.xticks(rotation=45)
plt.ylabel('Number of Order')

# Menampilkan plot
st.pyplot(plt)
st.write('---')

# Question 4
# Membuat barplot horizontal
st.header('Total Customer Expense for Each Months in 2017')
plt.figure(figsize=(10, 6))
plt.plot(q4_sorted['Months'], q4_sorted['Sum'], color='skyblue', marker='o')

# Memberikan label sumbu
plt.xlabel('Months')
plt.xticks(rotation=45)
plt.ylabel('Total Customer Expense')

# Menampilkan plot
st.pyplot(plt)
st.write('---')

st.caption('Copyright (C) Musthafa Zaki Bahar 2024')