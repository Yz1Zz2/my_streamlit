import streamlit as st
st.set_page_config(page_title="视频中心")


video_arr=[
    {
        'url':'https://www.w3school.com.cn/example/html5/mov_bbb.mp4',
        'title':'不知名-第一集'
        },
        {
        'url':'https://www.w3schools.com/html/movie.mp4',
        'title':'不知名-第二集'
        },
        {
        'url':'https://media.w3.org/2010/05/sintel/trailer.mp4',
        'title':'不知名-第三集'
        }

    ]

if 'ind' not in st.session_state:
    st.session_state['ind']=0

st.title(video_arr[st.session_state['ind']]['title'])
st.video(video_arr[st.session_state['ind']]['url'])


def playVideo(e):
    st.session_state['ind']=int(e)

# 创建与视频数量相等的列（例如3个视频就创建3列）
cols = st.columns(len(video_arr))

# 遍历每一列，并在每一列中放置一个按钮
for i, col in enumerate(cols):
    with col:
        st.button(f'第{i+1}集',use_container_width=True,on_click=playVideo, args=(i,))
