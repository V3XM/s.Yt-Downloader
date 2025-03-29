import streamlit as st
import yt_dlp

st.title("YouTube Downloader 🎥")

# اختيار نوع التحميل
type_choice = st.radio("Select Download Type:", ["Video", "Playlist"])

# إدخال رابط الفيديو أو قائمة التشغيل
url = st.text_input("Enter YouTube URL:")

if st.button("Download"):
    if url:
        try:
            options = {'format': 'bestvideo+bestaudio/best'}
            
            if type_choice == "Playlist":
                options.update({
                    'noplaylist': False,
                    'outtmpl': '%(playlist_index)s - %(title)s.%(ext)s'
                })

            with st.spinner("Downloading... ⏳"):
                yt_dlp.YoutubeDL(options).download([url])

            st.success("✅ Download completed successfully!")

        except Exception as e:
            st.error(f"❌ Error: {e}")
    else:
        st.warning("⚠️ Please enter a valid URL!")
