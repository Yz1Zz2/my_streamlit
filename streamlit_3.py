# 导入 Streamlit 库，并使用别名 st
import streamlit as st

# 设置网页的基本配置，包括标题和浏览器标签页的图标
st.set_page_config(page_title='相册网站', page_icon='🐹')

# 定义图片数据列表，每个元素是一个字典，包含图片的URL和标题
image_ua = [
    {
        'url': 'https://img95.699pic.com/photo/60033/0076.jpg_wh860.jpg',
        'text': '大象'
    },
    {
        'url': 'https://so1.360tres.com/t01a28e6c2de7216517.jpg',
        'text': '长颈鹿'
    },
    {
        'url': 'https://ts1.tc.mm.bing.net/th/id/R-C.3a43bf137b3f55423ae8a5421ddcb31c?rik=ByLfOabJrWDFMw&riu=http%3a%2f%2fp6.qhimg.com%2ft01b1bdb72dcf1217bb.jpg&ehk=ulCmElBs9srg1xHFK341gWOrkFKY9jhnoUgr0OkYX1M%3d&risl=&pid=ImgRaw&r=0',
        'text': '老虎'
    },
]

# 初始化会话状态（Session State），用于记录当前显示的图片索引
# 'ind' 不在 st.session_state 中时，说明是第一次运行，将其初始化为 0
if 'ind' not in st.session_state:
    st.session_state['ind'] = 0

# 根据当前索引 'ind'，从列表中获取并显示对应的图片和标题
st.image(image_ua[st.session_state['ind']]['url'], caption=image_ua[st.session_state['ind']]['text'])

# 创建一个两列的布局，用于并排放置按钮
c1, c2 = st.columns(2)

# 定义“下一张”按钮的回调函数
def nextImg():
    # 将索引加1，并使用取模运算 (%) 实现循环
    # 当索引等于列表长度时，会回到 0，实现“最后一张的下一张是第一张”
    st.session_state['ind'] = (st.session_state['ind'] + 1) % len(image_ua)


# 在第一列中放置“上一张”按钮，点击时调用 prevImg 函数
with c1:
    st.button('上一张', use_container_width=True)

# 在第二列中放置“下一张”按钮，点击时调用 nextImg 函数
with c2:
    st.button('下一张', use_container_width=True, on_click=nextImg)
