import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load dataset
beijing_airquality_df = pd.read_csv("dashboard/airquality.csv")



# Judul Dashboard
st.title("📊 Dashboard Analisis Kualitas Udara Kota Beijing")

# Sidebar untuk memilih analisis
menu = st.sidebar.radio("Pilih Analisis:", [
    "Distribusi Polutan",
    "Korelasi Polutan & Suhu",
    "Tren Polusi Tahunan & Musiman"
])

if menu == "Distribusi Polutan":
    st.subheader("Distribusi Polutan (PM2.5, PM10, SO2, NO2, CO)")
    polutan = ["PM2.5", "PM10", "SO2", "NO2", "CO"]
    
    selected_pollutant = st.selectbox("Pilih Polutan:", polutan)
    
    fig, ax = plt.subplots(figsize=(12, 5))
    

    if selected_pollutant == "PM2.5":
        sns.histplot(beijing_airquality_df["PM2.5"], bins=30, kde=True, color="red", ax=ax)
        ax.set_title("Distribusi PM2.5")
        ax.set_xlabel("PM2.5")
        ax.set_ylabel("Frekuensi")

    elif selected_pollutant == "PM10":
        sns.histplot(beijing_airquality_df["PM10"], bins=30, kde=True, color="blue", ax=ax)
        ax.set_title("Distribusi PM10")
        ax.set_xlabel("PM10")
        ax.set_ylabel("Frekuensi")

    elif selected_pollutant == "SO2":
        sns.histplot(beijing_airquality_df["SO2"], bins=30, kde=True, color="green", ax=ax)
        ax.set_title("Distribusi SO2")
        ax.set_xlabel("SO2")
        ax.set_ylabel("Frekuensi")

    elif selected_pollutant == "NO2":
        sns.histplot(beijing_airquality_df["NO2"], bins=30, kde=True, color="purple", ax=ax)
        ax.set_title("Distribusi NO2")
        ax.set_xlabel("NO2")
        ax.set_ylabel("Frekuensi")

    elif selected_pollutant == "CO":
        sns.histplot(beijing_airquality_df["CO"], bins=30, kde=True, color="orange", ax=ax)
        ax.set_title("Distribusi CO")
        ax.set_xlabel("CO")
        ax.set_ylabel("Frekuensi")

    plt.tight_layout()
    st.pyplot(fig)

elif menu == "Korelasi Polutan & Suhu":
    st.subheader("Korelasi antara Polutan dan Temperatur Suhu")
    
    numeric_cols = ["PM2.5", "PM10", "SO2", "NO2", "CO", "TEMP"]
    corr_matrix = beijing_airquality_df[numeric_cols].corr()
    
    fig, ax = plt.subplots(figsize=(8, 6))
    sns.heatmap(corr_matrix, annot=True, cmap="coolwarm", fmt=".2f", ax=ax)
    ax.set_title("Korelasi antara Polutan dan Suhu")
    st.pyplot(fig)

elif menu == "Tren Polusi Tahunan & Musiman":
    st.subheader("Tren Polusi per Tahun dan Bulan")

    beijing_airquality_df["datetime"] = pd.to_datetime(beijing_airquality_df["datetime"])
    beijing_airquality_df["year"] = beijing_airquality_df["datetime"].dt.year
    beijing_airquality_df["month"] = beijing_airquality_df["datetime"].dt.month
    analysis_type = st.selectbox("Pilih Analisis:", ["Tahunan", "Bulanan"])

    fig, ax = plt.subplots(figsize=(10, 5))

    if analysis_type == "Tahunan":
        polutan = ["PM2.5", "PM10", "SO2", "NO2", "CO"]
        selected_pollutant = st.selectbox("Pilih Polutan:", polutan)

        if selected_pollutant == "PM2.5":
            pm25_yearly = beijing_airquality_df.groupby("year")["PM2.5"].mean()

            sns.lineplot(x=pm25_yearly.index, y=pm25_yearly.values, marker="o", label="PM2.5", color="red", ax=ax)

            ax.set_title("Tren PM2.5 per Tahun")
            ax.set_xlabel("Tahun")
            ax.set_ylabel("Jumlah")
            ax.legend()
            ax.grid(True)
        elif selected_pollutant == "PM10":
            pm10_yearly = beijing_airquality_df.groupby("year")["PM10"].mean()

            sns.lineplot(x=pm10_yearly.index, y=pm10_yearly.values, marker="s", label="PM10", color="blue", ax=ax)

            ax.set_title("Tren PM10 per Tahun")
            ax.set_xlabel("Tahun")
            ax.set_ylabel("Jumlah")
            ax.legend()
            ax.grid(True)
        elif selected_pollutant == "SO2":
            so2_yearly = beijing_airquality_df.groupby("year")["SO2"].mean()

            sns.lineplot(x=so2_yearly.index, y=so2_yearly.values, marker="s", label="SO2", color="green", ax=ax)

            ax.set_title("Tren SO2 per Tahun")
            ax.set_xlabel("Tahun")
            ax.set_ylabel("Jumlah")
            ax.legend()
            ax.grid(True)
        elif selected_pollutant == "NO2":
            no2_yearly = beijing_airquality_df.groupby("year")["NO2"].mean()

            sns.lineplot(x=no2_yearly.index, y=no2_yearly.values, marker="s", label="NO2", color="purple", ax=ax)

            ax.set_title("Tren NO2 per Tahun")
            ax.set_xlabel("Tahun")
            ax.set_ylabel("Jumlah")
            ax.legend()
            ax.grid(True)
        elif selected_pollutant == "CO":
            co_yearly = beijing_airquality_df.groupby("year")["CO"].mean()

            sns.lineplot(x=co_yearly.index, y=co_yearly.values, marker="s", label="CO", color="orange", ax=ax)

            ax.set_title("Tren CO per Tahun")
            ax.set_xlabel("Tahun")
            ax.set_ylabel("Jumlah")
            ax.legend()
            ax.grid(True)
        st.pyplot(fig)
    
    elif analysis_type == "Bulanan":
        polutan = ["PM2.5", "PM10", "SO2", "NO2", "CO"]
        selected_pollutant = st.selectbox("Pilih Polutan:", polutan)

        if selected_pollutant == "PM2.5":
            pm25_monthly = beijing_airquality_df.groupby("month")["PM2.5"].mean()

            sns.lineplot(x=pm25_monthly.index, y=pm25_monthly.values, marker="o", label="PM2.5", color="red", ax=ax)

            ax.set_title("Tren PM2.5 per Bulan")
            ax.set_xlabel("Bulan")
            ax.set_ylabel("Jumlah")
            ax.set_xticklabels(["Jan", "Feb", "Mar", "Apr", "Mei", "Jun", 
            "Jul", "Agu", "Sep", "Okt", "Nov", "Des"])
            ax.legend()
            ax.grid(True)
        elif selected_pollutant == "PM10":
            pm10_monthly = beijing_airquality_df.groupby("month")["PM10"].mean()

            sns.lineplot(x=pm10_monthly.index, y=pm10_monthly.values, marker="s", label="PM10", color="blue", ax=ax)

            ax.set_title("Tren PM10 per Bulan")
            ax.set_xlabel("Bulan")
            ax.set_ylabel("Jumlah")
            ax.set_xticklabels(["Jan", "Feb", "Mar", "Apr", "Mei", "Jun", 
            "Jul", "Agu", "Sep", "Okt", "Nov", "Des"])
            ax.legend()
            ax.grid(True)
        elif selected_pollutant == "SO2":
            so2_monthly = beijing_airquality_df.groupby("month")["SO2"].mean()

            sns.lineplot(x=so2_monthly.index, y=so2_monthly.values, marker="s", label="SO2", color="green", ax=ax)

            ax.set_title("Tren SO2 per Bulan")
            ax.set_xlabel("Bulan")
            ax.set_ylabel("Jumlah")
            ax.set_xticklabels(["Jan", "Feb", "Mar", "Apr", "Mei", "Jun", 
            "Jul", "Agu", "Sep", "Okt", "Nov", "Des"])
            ax.legend()
            ax.grid(True)
        elif selected_pollutant == "NO2":
            no2_monthly = beijing_airquality_df.groupby("month")["NO2"].mean()

            sns.lineplot(x=no2_monthly.index, y=no2_monthly.values, marker="s", label="NO2", color="purple", ax=ax)

            ax.set_title("Tren NO2 per Bulan")
            ax.set_xlabel("Bulan")
            ax.set_ylabel("Jumlah")
            ax.set_xticklabels(["Jan", "Feb", "Mar", "Apr", "Mei", "Jun", 
            "Jul", "Agu", "Sep", "Okt", "Nov", "Des"])
            ax.legend()
            ax.grid(True)
        elif selected_pollutant == "CO":
            co_monthly = beijing_airquality_df.groupby("month")["CO"].mean()

            sns.lineplot(x=co_monthly.index, y=co_monthly.values, marker="s", label="CO", color="orange", ax=ax)

            ax.set_title("Tren CO per Bulan")
            ax.set_xlabel("Bulan")
            ax.set_ylabel("Jumlah")
            ax.legend()
            ax.grid(True)
        st.pyplot(fig)

st.write("© 2025")
