import streamlit as st
import pandas  as pd 
import numpy as np
import requests



#1 ELEMEN TEXT
st.title("Aplikasi Streamlit app")
st.header("Aplikasi Streamlit App - ini header")
st.write("Selamat datang di aplikasi Streamlit kamu!")
st.subheader("Ini subheader")
st.markdown("**Markdown** juga bisa digunakan di Streamlit.")
st.caption("Ini adalah caption kecil di bawah elemen lain.")
st.code("print('Hello, Streamlit!')", language="python") 
st.text("Aplikasi Streamlit App - ini text")
st.dialog("Konfirmasi Hapus Data")
st.latex(r'5^2 + 22^2 = 20^2')
st.divider()
st.markdown("Aplikasi Streamlit App - ini markdown")

#2 DATAFRAME INPUT  
# 2.1 API
st.subheader("Lembar kerja Belajar API")
url = 'https://jsonplaceholder.typicode.com/posts'
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    df = pd.DataFrame(data)
    st.dataframe(df)
else:
    print(f"Error: {response.status_code}")
    st.error("datanya gagal di fetch dari API")

st.subheader("Lembar kerja Belajar Upload CSV")

# 2.2 CSV UPLOAD FILE
uploaded_file = st.file_uploader("upload a CSV file", type=("csv"))
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.dataframe(df)
else:
    st.write("No file uploaded yet")

# 2.3 Simple Data
st.subheader("Lembar kerja Belajar Simpel Data")
data = {
    'Name': ['tasya', 'cinta', 'fajar'],
    'Age' : [18, 25, 19],
    'City' : ['Indonesia', 'Singapur', 'Amerika']
}

df = pd.DataFrame(data)
st.dataframe(df)

st.subheader("Lembar kerja Belajar Simple Data 2")

#3 Metrix Streamlit
col1, col2, col3 = st.columns(3)

with col1:
    st.metric(label="Omset", value="Rp 500 Juta", delta="+15%")
with col2:
    st.metric(label="User Aktif", value="1.250", delta="+2%")
with col3:
    st.metric(label="Refund", value="25", delta=" 5%",)

# 4 Charts
## 4.1 LINE CHART

st.subheader("Lembar kerja CHARTS")
chart_data = pd.DataFrame(
    np.random.randn(50, 3),
    columns=['a', 'b', 'c']
)

st.line_chart(chart_data)
st.bar_chart(chart_data, color=['#ffc0cb', '#808080', '#0000ff'])

## 4.2 Map Chart
df = pd.DataFrame(
    np.random.randn(1000, 2) / [60, 60] + [37.76, -122.4],
    columns=['lat', 'lon']
)

st.map(df)

# 5 INPUT FORM

st.subheader("Lembar kerja Belajar Form input")
with st.form("ay_form"):
    name = st.text_input("Name", placeholder="Enter your name")
    usia = st.text_area("Alamat", placeholder="Enter your address")
    usia = st.slider("Usia", 4, 120, 35)
    tanggal_lahir = st.date_input("Tanggal Lahir")
    warna_favorit = st.color_picker("warna favorit")
    foto_kamera = st.camera_input("Foto kamera")
    ratting = st.slider("Rating", 2, 6, 1)
    jenis_kelamin = st.radio("Jenis kelamin", ["Laki-laki", "Perempuan"])
    hobi = st.multiselect("Hobi", ["Membaca", "Menulis", "Menggambar", "Mengaji"])
    submitted = st.form_submit_button("submit")
    if submitted:
        st.write(f"Name: {name}")
        st.write(f"Alamat: {alamat}")
        st.write(f"Usia: {usia}")
        st.writer(f"Tanggal lahir: {tanggal_lahir}")

if submitted:
    st.success("Fora sub,itted!")

# 6. Upload Media Di Streamlit
st.subheader("Lembar Kerja Belajar Upload Media YT")
st.video("https://youtu.be/H73Q1W_NSho?si=D9SEr3TEv7GzxnC5")
# st.vidio('.vidio.mp4')

st.subheader("Lembar Kerja Belajar Upload Media mp3")
# st.audio('.audio.mp3')

#7. Membuat dua kolom
col1, col2 = st.columns(2)

# Menampilkan konten di kolom pertama
with col1:
    st.header("Kolom 1")
    st.write("Ini adalah konten di kolom pertama.")
    st.button("Tombol Kolom 1")

# Menampilkan konten di kolom kedua
with col2:
    st.header("Kolom 2")
    st.write("Ini adalah konten di kolom kedua.")
    st.button("Tombol Kolom 2")

st.sidebar.header("Lembar Kerja Belajar Sidebar")
st.sidebar.subheader("Lembar Kerja Belajar Sidebar Subheader")
st.sidebar.write("Lembar Kerja Belajar Sidebar Write")


import streamlit as st

# Menambahkan elemen navigasi di Sidebar
st.sidebar.header("Navigasi")
selection = st.sidebar.radio("Pilih Halaman", ["Beranda", "Tentang", "Kontak"])

# Konten berdasarkan pilihan
if selection == "Beranda":
    st.title("Beranda")
    st.write("Ini adalah halaman beranda.")
elif selection == "Tentang":
    st.title("Tentang")
    st.write("Ini adalah halaman tentang.")
else:
    st.title("Kontak")
    st.write("Ini adalah halaman kontak.")

# Menambahkan elemen navigasi dengan dropdown di Sidebar
st.sidebar.header("Navigasi")
selection = st.sidebar.selectbox("Pilih Halaman", ["Beranda", "Tentang", "Galeri", "Kontak"])

# Konten berdasarkan pilihan
if selection == "Beranda":
    st.title("Beranda")
    st.write("Ini adalah halaman beranda.")
elif selection == "Tentang":
    st.title("Tentang")
    st.write("Ini adalah halaman tentang.")
elif selection == "Galeri":
    st.title("Galeri")
    st.write("Ini adalah halaman galeri.")
else:
    st.title("Kontak")
    st.write("Ini adalah halaman kontak.")

# Menambahkan tombol untuk navigasi di Sidebar
st.sidebar.header("Navigasi")
if st.sidebar.button("Beranda"):
    st.title("Beranda")
    st.write("Ini adalah halaman beranda.")
elif st.sidebar.button("Tentang"):
    st.title("Tentang")
    st.write("Ini adalah halaman tentang.")
elif st.sidebar.button("Kontak"):
    st.title("Kontak")
    st.write("Ini adalah halaman kontak.")

# Menambahkan tautan navigasi di Sidebar
st.sidebar.header("Navigasi")
st.sidebar.markdown("[Beranda](#beranda)")
st.sidebar.markdown("[Tentang](#tentang)")
st.sidebar.markdown("[Kontak](#kontak)")

# Konten halaman berdasarkan tautan
st.title("Beranda")
st.write("Ini adalah halaman beranda.")

st.title("Tentang")
st.write("Ini adalah halaman tentang.")

st.title("Kontak")
st.write("Ini adalah halaman kontak.") 