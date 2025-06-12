import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# ---------------- Sidebar: Dokumentasi / Instruksi ----------------
st.sidebar.title("📘 Instruksi Penggunaan")
st.sidebar.markdown("""
Aplikasi ini menggunakan **model antrian M/M/1**.

**Definisi model M/M/1:**
- Laju kedatangan pelanggan mengikuti distribusi eksponensial (λ).
- Laju pelayanan juga mengikuti distribusi eksponensial (μ).
- Hanya ada **1 server** (pelayan).

**Petunjuk:**
- Masukkan nilai **λ** (laju kedatangan pelanggan per satuan waktu).
- Masukkan nilai **μ** (laju pelayanan pelanggan per satuan waktu).
- Pastikan **λ < μ** agar sistem stabil.
- Aplikasi akan menampilkan hasil perhitungan dan grafik.

**Output yang ditampilkan:**
- Utilisasi sistem (ρ)
- Jumlah rata-rata pelanggan dalam sistem (L)
- Jumlah rata-rata dalam antrean (Lq)
- Waktu rata-rata pelanggan di sistem (W)
- Waktu rata-rata dalam antrean (Wq)
""")

# ---------------- Judul Aplikasi ----------------
st.title("📊 Simulasi Model Antrian M/M/1")

# ---------------- Input Pengguna ----------------
st.subheader("Masukkan Parameter Antrian:")
lambda_val = st.number_input("λ (Laju Kedatangan)", min_value=0.01, value=2.0, step=0.1, format="%.2f")
mu_val = st.number_input("μ (Laju Pelayanan)", min_value=0.01, value=4.0, step=0.1, format="%.2f")

# ---------------- Validasi dan Hitung ----------------
if lambda_val >= mu_val:
    st.error("❌ Sistem tidak stabil: λ harus lebih kecil dari μ.")
else:
    rho = lambda_val / mu_val
    L = rho / (1 - rho)
    Lq = rho**2 / (1 - rho)
    W = 1 / (mu_val - lambda_val)
    Wq = rho / (mu_val - lambda_val)

    # ---------------- Output ----------------
    st.subheader("📈 Hasil Perhitungan:")
    st.metric("Utilisasi (ρ)", f"{rho:.2f}")
    st.metric("L (Jumlah rata-rata dalam sistem)", f"{L:.2f}")
    st.metric("Lq (Jumlah rata-rata dalam antrean)", f"{Lq:.2f}")
    st.metric("W (Waktu rata-rata dalam sistem)", f"{W:.2f} satuan waktu")
    st.metric("Wq (Waktu rata-rata dalam antrean)", f"{Wq:.2f} satuan waktu")

    # ---------------- Visualisasi Grafik ----------------
    st.subheader("📉 Grafik: Jumlah Pelanggan (L) terhadap Laju Kedatangan (λ)")

    lambda_vals = np.linspace(0.01, mu_val * 0.99, 100)
    L_vals = lambda_vals / (mu_val - lambda_vals)

    fig, ax = plt.subplots()
    ax.plot(lambda_vals, L_vals, label='L vs λ', color='blue')
    ax.axvline(lambda_val, color='red', linestyle='--', label='λ saat ini')
    ax.set_xlabel("λ (Laju Kedatangan)")
    ax.set_ylabel("L (Jumlah Pelanggan Rata-rata)")
    ax.set_title("Hubungan antara λ dan L (μ tetap)")
    ax.legend()
    ax.grid(True)

    st.pyplot(fig)
