import streamlit as st 
from ptmn3 import dataMhs
# Membuat Judul Web Appps
st.title ("👨‍🎓Manajemen Data Mahasiswa👩‍🎓")
# Menambah Data Mahasiswa dengan Append
st.title("➕ Tambah data denagan Append")
new_name = st.text_input("Masukan Nama Mhs")
new_nim = st.text_input("Masukan NIM")
new_prodi = st.text_input("Masukan Prodi")
if st.button("Tambah Append"):
             new_Mhs = {"nama":new_name, "NIM":new_nim, "Prodi":new_prodi}
             dataMhs.append(dataMhs)
             st.success("✅ Data Mahasiswa Berhasil Ditambah")


# Menampilkan data Mahasiswa
st.subheader("📅 Data Mahasiswa")
no=0
for i in dataMhs:
    no=no+1
    st.write(f"{no}. Nama = {i['nama']} NIM = {i['NIM']} Prodi = {i['Prodi']}")