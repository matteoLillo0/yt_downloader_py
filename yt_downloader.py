'''

Piccolo progetto in python per scaricare video da yt
librerie usate: strealit, yt-dlp (nuova lib)

'''

import streamlit as st
import yt_dlp

# titolo e descrizione 

st.title("Youtube video downloader with Python!")
st.write("Insert a link below to start: ")

link = st.text_input("Videos URL: ") # prende l'url tramite il campo input

if st.button("Download"): # controlliamo se è stato cliccato
    if link: # controlliamo se il link è vuoto
        try:

            # mentre gira lo spinner
            with st.spinner("Download in progress: "):
                
                ydl_opts = {
                    'format': 'best',
                    'outtmpl': '%(title)s.%(ext)s', 
                }
                with yt_dlp.YoutubeDL(ydl_opts) as ydl:

                    # prendere le informazioni
                    info = ydl.extract_info(link, download=False)


                    # stamparle
                    st.image(info["thumbnail"])
                    st.write(f"Title: {info['title']} ")
                    st.write(f"Creator: {info['uploader']}")
                    st.write(f"Duration: {info['duration']}")
                    ydl.download([link])
                st.success(f"Done! '{info['title']} has been downloaded locally!")
        except Exception as e: 
            st.error(f"Errore: {e}")# stampa errore
    else:
        st.write("Please insert a link!")






