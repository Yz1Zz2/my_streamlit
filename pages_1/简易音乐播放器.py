# 导入 Streamlit 库，并使用别名 st
import streamlit as st

# 设置网页的基本配置，包括标题和浏览器标签页的图标
st.set_page_config(page_title='音乐网站', page_icon='🐹')

# 定义图片数据列表，每个元素是一个字典，包含图片的URL和标题
music_data = [
    {
        'url': 'https://music.163.com/song/media/outer/url?id=1465082816.mp3',
        'img': 'http://p1.music.126.net/HqEkuaWZfqnpci4EtxF41w==/109951165163056041.jpg?param=130y130',
        'text':'专辑封面',
        'title': '苦海无涯',
        'artist':'法老 / Yoken_Official',
        'time':'3:38'
        
        
    },
    {
        'url': 'https://music.163.com/song/media/outer/url?id=3329668871.mp3',
        'img': 'http://p1.music.126.net/qDDB6HshQrqwyKzE9778QA==/109951172450091661.jpg?param=130y130',
        'text':'专辑封面',
        'title': '恭喜发财（R&B版）',
        'artist':'mchaCheers',
         'time':'3:55'
    },
    {
        'url': 'https://music.163.com/song/media/outer/url?id=3329668871.mp3',
        'img': 'http://p1.music.126.net/WphIFnDUpf4JhxKTZbRo0A==/109951172454584686.jpg?param=130y130',
        'text':'专辑封面',
        'title': '友情提示 (Live)',
        'artist':'薛之谦',
         'time':'3:55'
    },
]

# 初始化会话状态（Session State），用于记录当前显示的图片索引
# 'ind' 不在 st.session_state 中时，说明是第一次运行，将其初始化为 0
if 'ind' not in st.session_state:
    st.session_state['ind'] = 0

# 获取当前播放的歌曲
current_song = music_data[st.session_state['ind']]

# 标题和描述
st.title('🎵 简易音乐播放器')


# 创建一个两列的布局，用于并排放置按钮
c1, c2 = st.columns([1,2])

# 定义“下一张”按钮的回调函数
def nextImg():
    # 将索引加1，并使用取模运算 (%) 实现循环
    # 当索引等于列表长度时，会回到 0，实现“最后一张的下一张是第一张”
    st.session_state['ind'] = (st.session_state['ind'] + 1) % len(music_data)
def prevImg():
    # 确保索引在列表范围内，处理负数索引
    st.session_state['ind'] = (st.session_state['ind'] - 1 + len(music_data)) % len(music_data)

# 在第一列中放置“上一张”按钮，点击时调用 prevImg 函数
with c1:
     st.image(current_song['img'], width=200)  # 显示专辑封面
     st.text(current_song['text'])
# 在第二列中放置“下一张”按钮，点击时调用 nextImg 函数
with c2:
    st.subheader(f"{current_song['title']}")  # 歌曲标题（加粗）
    st.text(f"歌手: {current_song['artist']}")  # 歌手信息
    st.text(f"时长: {current_song['time']}")  # 歌曲时长
        # 在右列中再创建两列，用于放置“上一首”和“下一首”按钮
    button_col1, button_col2 = st.columns(2)
    
    # “上一首”按钮（左列）
    with button_col1:
        st.button('⏮ 上一首', use_container_width=True,on_click=prevImg)  # 绑定 prevImg 回调函数
    
    # “下一首”按钮（右列）
    with button_col2:
        st.button('⏭ 下一首', use_container_width=True,on_click=nextImg)  # 绑定 nextImg 回调函数

 # 1. 创建一个容器（或列）来包裹音频播放器
with st.container():
    st.audio(current_song['url'])  # 音频播放器会自动适应容器宽度
       
    

