import streamlit as st 
from ptmn3 import dataMhs
# Membuat Judul Web Apps
st.title ("👨🏻‍🎓Manajemen Data Mahasiswa 👩🏻‍🎓")
# Menambah Data Mahasiswa dengan Append
st.subheader("➕ Tambah data dengan Append")
new_name = st.text_input("Masukan Nama Mhs")
new_nim = st.text_input("Masukan NIM")
new_prodi = st.text_input("Masukan Prodi")
if st.button("Tambah Append"):
    new_Mhs = {"nama":new_name, "NIM":new_nim, "Prodi":new_prodi}
    dataMhs.append(new_Mhs)
    st.success("✅ Data Mahasiswa berhasil ditambah")
# Menampilkan data Mahasiswa
st.subheader("📅Data Mahasiswa")
no=0
for i in dataMhs:
    no+=1
    st.write(f"{no}.Nama = {i['nama']};  NIM = {i['NIM']}; Prodi = {i['Prodi']}")