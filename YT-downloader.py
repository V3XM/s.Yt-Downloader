import streamlit as st
import yt_dlp
import os

st.title("YouTube Downloader 🎥")

# اختيار نوع التحميل
type_choice = st.radio("Select Download Type:", ["Video", "Playlist"])

# إدخال رابط الفيديو أو قائمة التشغيل
url = st.text_input("Enter YouTube URL:")

# مسار تخزين الملفات
download_folder = "downloads"
os.makedirs(download_folder, exist_ok=True)

if st.button("Download"):
    if url:
        try:
            output_template = os.path.join(download_folder, "%(title)s.%(ext)s")
            options = {'format': 'bestvideo+bestaudio/best', 'outtmpl': output_template}

            if type_choice == "Playlist":
                options.update({'noplaylist': False})

            with st.spinner("Downloading... ⏳"):
                yt_dlp.YoutubeDL(options).download([url])

            # العثور على الملف الذي تم تحميله
            downloaded_files = os.listdir(download_folder)
            if downloaded_files:
                latest_file = max(
                    [os.path.join(download_folder, f) for f in downloaded_files],
                    key=os.path.getctime,
                )

                # إتاحة رابط التحميل
                with open(latest_file, "rb") as f:
                    st.download_button(
                        label="Click here to download the file",
                        data=f,
                        file_name=os.path.basename(latest_file),
                        mime="video/mp4",
                    )

            st.success("✅ Download completed successfully!")

        except Exception as e:
            st.error(f"❌ Error: {e}")
    else:
        st.warning("⚠️ Please enter a valid URL!")
