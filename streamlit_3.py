import streamlit as st

import streamlit as st
st.set_page_config(page_title='相册网站',page_icon='🐹')
image_ua = [
    {
        'url': 'https://cn.bing.com/images/search?view=detailV2&ccid=hUHZVg4%2f&id=766F5A6459DAD7CE7C2EA76B68B90E951649875E&thid=OIP.hUHZVg4_yVVS5Spr4Lk7-wHaFb&mediaurl=https%3a%2f%2fpic.nximg.cn%2ffile%2f20240420%2f28864261_235606233126_2.jpg&exph=751&expw=1024&q=%e5%a4%a7%e8%b1%a1&FORM=IRPRST&ck=3E0D80E04BBF3E6E4819F25CA51BE95C&selectedIndex=53&itb=0',
        'text': '大象'
    },
    {
        'url': 'https://so1.360tres.com/t01a28e6c2de7216517.jpg',
        'text': '长颈鹿'
    },
    {
        'url': 'https://ts4.tc.mm.bing.net/th/id/OIP-C.0bTOktwCJzRcyLwnpW2algHaFj?cb=ucfimg2&ucfimg=1&rs=1&pid=ImgDetMain&o=7&rm=3',
        'text': '老虎'
    },
]

# 初始化索引
if 'ind' not in st.session_state:
    st.session_state['ind'] = 0

# --- 修正3: 修正 st.image 的索引逻辑和括号 ---
st.image(image_ua[st.session_state['ind']]['url'], caption=image_ua[st.session_state['ind']]['text'])

# --- 修正4: 修正函数名拼写错误 st.colums -> st.columns ---
c1, c2 = st.columns(2)

# 定义“下一张”按钮的回调函数
def nextImg():
    st.session_state['ind'] = (st.session_state['ind'] + 1) % len(image_ua)

# --- 修正5: 定义“上一张”按钮的回调函数 ---
def prevImg():
    # 确保索引在列表范围内，处理负数索引
    st.session_state['ind'] = (st.session_state['ind'] - 1 + len(image_ua)) % len(image_ua)

# --- 修正6: 将按钮正确放置在列中，并绑定事件 ---
with c1:
    st.button('上一张', use_container_width=True, on_click=prevImg)

with c2:
    st.button('下一张', use_container_width=True, on_click=nextImg)

