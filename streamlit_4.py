import streamlit as st

# 读取音频URL
audio_file = 'https://music.163.com/song/media/outer/url?id=5257138.mp3'

st.audio(audio_file)
