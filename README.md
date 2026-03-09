# YouTube Video Downloader 🎥

Un'applicazione web leggera e intuitiva sviluppata in Python per scaricare video da YouTube alla massima qualità disponibile. L'interfaccia grafica è gestita tramite Streamlit, mentre il motore di download è basato sulla potente libreria yt-dlp.

## 🌟 Funzionalità

- **Interfaccia Web Semplice:** Inserisci l'URL del video e avvia il download con un clic.
- **Anteprima Dati:** Prima del download, l'app estrae e mostra la miniatura (thumbnail) del video, il titolo e il nome del creatore.
- **Qualità Massima:** Configurata per scaricare automaticamente il formato video/audio migliore disponibile (`'format': 'best'`).
- **Feedback in Real-time:** Spinner di caricamento durante il fetch dei dati e messaggi di successo o errore a fine operazione.

## 🛠️ Tecnologie Utilizzate

- **Python 3.x**
- **Streamlit:** Per la creazione della UI interattiva.
- **yt-dlp:** Fork moderno e aggiornato di youtube-dl per l'estrazione e il download dei file multimediali.

## 🚀 Installazione e Avvio

1. Clona il repository sulla tua macchina:
   ```bash
   git clone 'repo'
   cd NOME_REPO

    Installa le librerie necessarie:
    Bash

    pip install streamlit yt-dlp

    Avvia l'applicazione web tramite Streamlit:
    Bash

    streamlit run app.py

    (Sostituisci app.py con il nome del tuo file script)

    Si aprirà automaticamente una nuova scheda nel tuo browser predefinito all'indirizzo http://localhost:8501.

## 📂 Struttura dell'Output

I video scaricati verranno salvati automaticamente nella stessa directory in cui viene eseguito lo script, rinominati con il titolo originale del video e l'estensione corretta (grazie all'opzione 'outtmpl': '%(title)s.%(ext)s').

---
