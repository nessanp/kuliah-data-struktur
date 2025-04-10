import streamlit as st
from data import dataMhs

st.title("👨‍🎓 Manajemen Data Mahasiswa 👩‍🎓")

# Menambah data mahasiswa
with st.expander("Tambah Data Mahasiswa"):
    with st.form("form_mahasiswa"):
        nama = st.text_input("Nama")
        nim = st.text_input("NIM")
        prodi = st.text_input("Prodi")
        submit = st.form_submit_button("Tambah Data")
        if submit:
            dataMhs.append({"nama": nama, "nim": nim, "prodi": prodi})
            st.success("Data berhasil ditambahkan")

# Menghapus data mahasiswa dengan Remove
with st.expander("Hapus Data Mahasiswa"):
    with st.form("form_mahasiswa_pop"):
        nim = st.text_input("NIM")
        submit = st.form_submit_button("Hapus Data")
        if submit:
            for i in range(len(dataMhs)):
                if dataMhs[i]["nim"] == nim:
                    dataMhs.pop(i)
                    st.success("Data berhasil dihapus")
                    break

# menampilkan data mahasiswa
st.write(dataMhs)