import streamlit as st
import yt_dlp

# 🎥 عنوان الموقع
st.title("YouTube Video Downloader 🎥")

# 📌 اختيار نوع التحميل (فيديو أو قائمة تشغيل)
type_choice = st.radio("Select Download Type:", ["Video", "Playlist"])

# 🔗 إدخال رابط الفيديو أو قائمة التشغيل
url = st.text_input("Enter YouTube URL:")

# ⏬ زر التحميل
if st.button("Download"):
    if url:
        try:
            options = {}

            if type_choice == "Video":
                options = {'format': 'bestvideo+bestaudio/best'}  # تحميل الفيديو فقط

            elif type_choice == "Playlist":
                options = {
                    'format': 'bestvideo+bestaudio/best',
                    'noplaylist': False,
                    'outtmpl': '%(playlist_index)s - %(title)s.%(ext)s'
                }

            with st.spinner("Downloading... ⏳"):
                yt_dlp.YoutubeDL(options).download([url])

            st.success("✅ Download completed successfully!")
        
        except Exception as e:
            st.error(f"❌ Error: {e}")
    else:
        st.warning("⚠️ Please enter a valid URL!")
