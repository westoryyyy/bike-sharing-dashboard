import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Membaca dataset
data = pd.read_csv('day.csv')  # Pastikan file day.csv ada di folder yang sama
data['dteday'] = pd.to_datetime(data['dteday'])

# Halaman utama
st.title("Dashboard Bike Sharing")
st.write("Analisis data penyewaan sepeda berdasarkan suhu, musim, dan cuaca.")

# Pilihan Analisis
menu = st.sidebar.selectbox("Pilih Analisis:", ["Tren Musiman", "Pengaruh Suhu", "RFM Analysis"])

if menu == "Tren Musiman":
    st.subheader("Tren Musiman dalam Penyewaan Sepeda")
    fig, ax = plt.subplots()
    sns.lineplot(data=data, x='dteday', y='cnt', hue='season', palette='viridis', ax=ax)
    ax.set_title('Tren Musiman dalam Penyewaan Sepeda')
    ax.set_xlabel('Tanggal')
    ax.set_ylabel('Jumlah Penyewaan Sepeda')
    st.pyplot(fig)

elif menu == "Pengaruh Suhu":
    st.subheader("Pengaruh Suhu Terhadap Penyewaan Sepeda")
    fig, ax = plt.subplots()
    sns.scatterplot(data=data, x='temp', y='cnt', hue='season', palette='coolwarm', ax=ax)
    ax.set_title('Pengaruh Suhu Terhadap Penyewaan Sepeda')
    ax.set_xlabel('Normalized Temperature')
    ax.set_ylabel('Jumlah Penyewaan Sepeda')
    st.pyplot(fig)

elif menu == "RFM Analysis":
    st.subheader("RFM Analysis")
    data['recency'] = (data['dteday'].max() - data['dteday']).dt.days
    rfm = data.groupby('weekday').agg({
        'recency': 'mean',
        'cnt': ['count', 'sum']
    }).reset_index()
    rfm.columns = ['weekday', 'recency', 'frequency', 'monetary']
    st.write(rfm)
