from gtts import gTTS
import streamlit as st 
st.title("⬆️ Sistem Antrian Pasien di RS Suka Sehat")
def generate_tts(text, filename="antrian.mp3"):
    tts = gTTS(text, lang='id', slow=True)
    tts.save(filename)
    return filename
# membuat session untuk antrian
if "queue" not in st.session_state:
    st.session_state.queue= []
if "current" not in st.session_state:
    st.session_state.current = 0
with st.form("form"):
    nomor = st.text_input("Masukan nomor antrian")
    submit = st.form_submit_button("Tambah")
    if submit and nomor:
        st.session_state.queue.append(nomor)
        st.success(f"nomor antrian {nomor} sudah ditambahkan")
st.subheader("Daftar Antrian")
for i, n in enumerate (st.session_state.queue, 1):
    st.write(f"{i}. {n}")
if st.button("Panggil Daftar Antrian"):
    if st.session_state.queue:
        panggil = st.session_state.queue.pop(0)
        st.session_state.current +=1
        teks = f"urutan antrian {st.session_state.current},untuk nomor antrian {panggil} silahkan ke loket 1"
        st.success(teks)
        filename = generate_tts(teks)
        audio_file = open(filename, "rb")
        audio_bytes = audio_file.read()
        st.audio(audio_bytes, format="audio/mp3", autoplay=True)
    else:
        st.warning("Tidak ada antrian")
        