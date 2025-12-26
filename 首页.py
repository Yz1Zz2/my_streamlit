import streamlit as st

# 全局设置
st.set_page_config(
    page_title="综合应用",
    layout="wide",
    page_icon='🎠'
)

# 侧边栏导航
st.sidebar.title("导航菜单")
page = st.sidebar.selectbox(
    "选择功能模块",
    [
        "首页",
        "个人简历制作",
        "南宁美食数据",
        "数字档案",
        "简易音乐播放器",
        "视频播放网站"
    ]
)

# ==================== 首页 ====================
if page == "首页":
    st.title("这里是主页")
    st.image("https://www.gxvnu.edu.cn/lib/images/bannner4.jpg", use_container_width=True)
    st.write("""
    广西职业师范学院（GuangXi Vocational Normal University），坐落于广西壮族自治区南宁市，是广西壮族自治区人民政府直属、自治区教育厅主管的公办全日制普通本科学校，入选教育部 “新工科”研究与实践项目。 [1] [3]
    学校前身为开办于1951年5月的广西省行政干部训练班，历经广西人民革命大学、广西省人民政府行政干部学校、广西壮族自治区五七干校和南宁市五七干校、广西壮族自治区经济干部学校、广西壮族自治区经济管理干部学院等历史时期，2019年6月，经教育部批准设置为“广西职业师范学院”。 [2]2021年10月，广西职业师范学院罗文校区正式启用。 [25]2022年，学校被评为广西壮族自治区绿色学校。 [33]
    截至2025年3月，学校有罗文校区和相思湖校区；开设普通本科专业33个 [3]，建有广西高校重点实验室1个，自治区级实验教学中心2个，广西高等学校特色专业及课程一体化建设项目3个，自治区级虚拟教研室建设试点2个 [3] [19] [26]；截至2025年4月，学校有12个二级学院（部） [40]，有自治区级本科一流课程4门，自治区级课程思政示范课5门 [3]；截至2024年12月，学校总占地面积37.92万平方米，教学、科研仪器设备资产总值1.45亿元 [34]；有专任教师464人、外聘教师190人，全日制在校学生人数14371人 [34]。截至2024年9月，学校图书馆拥有纸质图书143.77万册，2024年年新增215790册，生均纸质图书99.77册；拥有电子期刊36.27万册，学位论文1013.82万册，音视频0.0小时。 [34]
    """)

# ==================== 个人简历制作 ====================
elif page == "个人简历制作":
    # 设置页面配置
    st.set_page_config(page_title="个人简历生成器", layout="wide", page_icon='👨‍🎓')
    
    # 创建两列布局
    c1, c2 = st.columns([1, 2])
    
    # 左侧：用户信息输入
    with c1:
        user_name = st.text_input("姓名")
        user_work = st.text_input("职位")
        user_phone = st.text_input("手机号")
        user_email = st.text_input("邮箱")
        user_date = st.date_input("出生日期")
        user_sex = st.radio('性别', ['男', '女', '其他'], horizontal=True, index=0)
        use_xl = st.selectbox('学历', ['初中', '中专', '高中', '大专', '本科', '研究生', '博士'])
        user_language = st.multiselect('语言能力', ['中文', '英语', '法语', '日语', '俄语', '西班牙语'])
        user_jineng = st.multiselect('技能能力', ['Java', 'Python', 'HTML', 'Js', 'Type/Scripts', 'C++'])
        use_age = st.slider('工作经验', 0, 30)
        salary_range = st.slider('期望薪资范围', 5000, 12000, (6000, 8000))
        user_grjj = st.text_area(label='个人简介：', placeholder='请输入您的个人简介')
        user_time = st.time_input("每日最佳联系时间:")
        user_avatar = st.file_uploader("上传头像", type=['jpg', 'jpeg', 'png', 'webp'], help="支持 jpg, png, webp 格式")
    
    # 右侧：简历预览
    with c2:
        st.header("简历预览")
        if not user_name:
            st.info("请在左侧输入信息以生成简历。")
        else:
            col_avatar, col_title = c2.columns([1, 3])
            with col_avatar:
                if user_avatar is not None:
                    st.image(user_avatar, width=150, use_container_width=False)
                else:
                    st.markdown("### 👤")
            with col_title:
                st.title(user_name)
                st.write(f"*{user_work}*")
            
            st.divider()
            col_a, col_b = c2.columns(2)
            with col_a:
                st.write(f"**手机号码：** {user_phone}")
                st.write(f"**电子邮箱：** {user_email}")
            with col_b:
                st.write(f"**性别：** {user_sex}")
                st.write(f"**出生日期：** {user_date}")
                st.write(f"**最高学历：** {use_xl}")
            
            st.divider()
            st.subheader("个人简介")
            st.write(user_grjj)
            st.subheader("技能与能力")
            st.write(f"**工作经验：** {use_age} 年")
            st.write(f"**期望薪资：** {salary_range[0]} - {salary_range[1]} 元")
            st.write(f"**掌握技能：** {', '.join(user_jineng) if user_jineng else '暂无'}")
            st.write(f"**语言能力：** {', '.join(user_language) if user_language else '暂无'}")
            st.write(f"**最佳联系时间：** {user_time}")

# ==================== 南宁美食数据 ====================
elif page == "南宁美食数据":
    import pandas as pd
    import numpy as np
    import random
    
    st.set_page_config(
        page_title="南宁美食数据仪表盘",
        page_icon="🍜",
        layout="wide"
    )
    
    st.markdown("""
    <style>
        .main-header {
            text-align: center;
            color: #FF6B35;
            margin-bottom: 2rem;
        }
        .metric-card {
            background: #f0f2f6;
            padding: 1rem;
            border-radius: 10px;
            margin-bottom: 1rem;
        }
    </style>
    """, unsafe_allow_html=True)
    
    st.markdown('<h1 class="main-header">🍜 南宁美食数据仪表盘</h1>', unsafe_allow_html=True)
    
    restaurants_data = {
        "餐厅": ["甘家界牌柠檬鸭", "中山路美食街", "万国酒家", "复记老友粉", "阿光烧烤", 
                 "舒记老友", "老友记", "三品王", "梁记卷筒粉", "建政路夜市"],
        "类型": ["桂菜", "小吃街", "粤菜", "老友粉", "烧烤", "老友粉", "老友粉", "快餐", "小吃", "夜市"],
        "评分": [4.6, 4.4, 4.5, 4.3, 4.2, 4.4, 4.1, 4.0, 4.3, 4.5],
        "人均消费(元)": [68, 35, 88, 18, 45, 20, 16, 25, 12, 30],
        "latitude": [22.8170, 22.8220, 22.8190, 22.8122, 22.7950, 22.8350, 22.8250, 22.8420, 22.8280, 22.8180],
        "longitude": [108.3665, 108.3565, 108.3685, 108.2666, 108.3465, 108.3185, 108.3765, 108.3250, 108.3850, 108.3450]
    }
    
    df = pd.DataFrame(restaurants_data)
    
    @st.cache_data
    def generate_price_trends():
        months = ['1月', '2月', '3月', '4月', '5月', '6月', 
                  '7月', '8月', '9月', '10月', '11月', '12月']
        
        price_trends = []
        for _, restaurant in df.iterrows():
            base_price = restaurant['人均消费(元)']
            for i, month in enumerate(months):
                seasonal_factor = 1 + 0.1 * np.sin(2 * np.pi * i / 12)
                random_factor = 1 + np.random.normal(0, 0.03)
                price = base_price * seasonal_factor * random_factor
                
                price_trends.append({
                    '餐厅': restaurant['餐厅'],
                    '月份': month,
                    '价格': round(price, 2)
                })
        
        return pd.DataFrame(price_trends)

    @st.cache_data
    def generate_monthly_sales():
        months = ['1月', '2月', '3月', '4月', '5月', '6月', 
                  '7月', '8月', '9月', '10月', '11月', '12月']
        
        sales_data = []
        for _, restaurant in df.iterrows():
            base_sales = random.randint(1200, 3500)
            for i, month in enumerate(months):
                seasonal_factor = 1 + 0.15 * np.sin(2 * np.pi * i / 12 + np.pi/4)
                random_factor = 1 + np.random.normal(0, 0.1)
                sales = base_sales * seasonal_factor * random_factor
                
                sales_data.append({
                    '餐厅': restaurant['餐厅'],
                    '月份': month,
                    '销量': int(sales)
                })
        
        return pd.DataFrame(sales_data)

    price_df = generate_price_trends()
    sales_df = generate_monthly_sales()
    
    st.sidebar.title("📊 数据筛选")
    selected_type = st.sidebar.selectbox(
        "选择餐厅类型",
        ["全部", "桂菜", "小吃街", "粤菜", "老友粉", "烧烤", "快餐", "小吃", "夜市"]
    )
    
    if selected_type != "全部":
        df_filtered = df[df['类型'] == selected_type]
        price_df_filtered = price_df[price_df['餐厅'].isin(df_filtered['餐厅'])]
        sales_df_filtered = sales_df[sales_df['餐厅'].isin(df_filtered['餐厅'])]
    else:
        df_filtered = df
        price_df_filtered = price_df
        sales_df_filtered = sales_df

    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("🏪 餐厅总数", len(df_filtered))
    with col2:
        avg_rating = df_filtered['评分'].mean()
        st.metric("⭐ 平均评分", f"{avg_rating:.1f}")
    with col3:
        avg_price = df_filtered['人均消费(元)'].mean()
        st.metric("💰 平均消费", f"¥{avg_price:.0f}")
    with col4:
        total_sales = sales_df_filtered['销量'].sum()
        st.metric("📈 总销量", f"{total_sales:,}")

    st.header("📊 数据可视化分析")
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("📊 餐厅评分对比")
        chart_data = df_filtered.set_index('餐厅')['评分']
        st.bar_chart(chart_data, color="#FF6B35")
    with col2:
        st.subheader("📈 月度销量趋势")
        line_data = sales_df_filtered.pivot(index='月份', columns='餐厅', values='销量')
        st.line_chart(line_data)

    col1, col2 = st.columns(2)
    with col1:
        st.subheader("📉 销量面积图")
        area_data = sales_df_filtered.groupby('月份')['销量'].sum()
        st.area_chart(area_data, color="#667eea")
    with col2:
        st.subheader("💹 12个月价格走势")
        price_data = price_df.pivot(index='月份', columns='餐厅', values='价格')
        st.line_chart(price_data)

    st.header("🗺️ 餐厅地理位置分布")
    map_data = df_filtered[['latitude', 'longitude']].rename(columns={
        'latitude': 'lat',
        'longitude': 'lon'
    })
    st.map(map_data, zoom=10, use_container_width=True)

    st.subheader("📍 餐厅位置信息")
    for _, row in df_filtered.iterrows():
        st.write(f"**{row['餐厅']}** - {row['类型']} | 评分: {row['评分']} | 人均: ¥{row['人均消费(元)']}")

    st.header("📋 餐厅详细信息")
    display_df = df_filtered.copy().rename(columns={
        '餐厅': '餐厅名称',
        '类型': '餐厅类型',
        '评分': '评分',
        '人均消费(元)': '人均消费(元)',
        'latitude': '纬度',
        'longitude': '经度'
    })
    st.dataframe(
        display_df,
        use_container_width=True,
        hide_index=True,
        column_config={
            "评分": st.column_config.ProgressColumn(
                "评分",
                help="餐厅评分（0-5分）",
                format="%.1f",
                min_value=0,
                max_value=5
            ),
            "人均消费(元)": st.column_config.NumberColumn(
                "人均消费",
                format="¥%d 元"
            ),
            "纬度": st.column_config.NumberColumn(
                "纬度",
                format="%.6f"
            ),
            "经度": st.column_config.NumberColumn(
                "经度",
                format="%.6f"
            )
        }
    )

    st.markdown("---")
    st.markdown("""
    <div style='text-align: center; color: #718096; margin-top: 1rem;'>
        <p>🍜 南宁美食数据仪表盘 | 数据更新时间：2025年12月22日 09:28</p>
        <p>探索南宁地道美食，品味壮乡风情 🌟</p>
    </div>
    """, unsafe_allow_html=True)

# ==================== 数字档案 ====================
elif page == "数字档案":
    import pandas as pd
    
    st.title("🥇学生 小明2048-数字档案")
    
    st.header("🔑基础信息")
    st.text("学生ID:STU-2024-005")
    st.markdown("注册时间: :green[2025-12-15]|精神状态：✅正常")
    st.markdown("当前教室: :green[教学楼702]|安全等级：🔒机密")
    
    st.title("📊技能矩阵")
    st.subheader('技能掌握度')
    c1, c2, c3 = st.columns(3)
    c1.metric(label="C语言",help="提示", value="95%", delta="2℃")
    c2.metric(label="Pyhon",help="提示",value="86%", delta="6%")
    c3.metric(label="Java",help="提示", value="88%", delta="-9%")
    
    data = {
        '作业提交数':[15, 18, 22, 20, 25],
        '学习时长(小时)':[120, 145, 160, 155, 180],
        '代码行数':[850, 1200, 1500, 1400, 1800],
    }
    index = pd.Series(['01月', '02月', '03月', '04月', '05月'], name='月份')
    df = pd.DataFrame(data, index=index)
    
    st.title("Streamlit课程进度")
    st.progress(15)
    st.text("Streamlit课程进度")
    
    st.subheader('任务日志')
    st.table(df)
    
    st.subheader('💻最新代码成果')
    python_code = '''<div style="font-weight: bold; color: #333; margin-bottom: 10px;">SYSTEM MESSAGE</div>
        <div style="display: flex; justify-content: space-between; margin-bottom: 10px;">
            <div>
                <div style="font-size: 14px; color: #666;">TARGET:</div>
                <div style="font-size: 16px;">学生档案系统</div>
            </div>")
    '''
    st.code(python_code, line_numbers=True)
    
    st.markdown('***')
    st.subheader("📡 系统状态")
    st.markdown(':green[>> SYSTEM]')
    with st.container():
        st.markdown("""
        <div style="background-color: #f0f2f6; padding: 15px; border-radius: 5px; border: 1px solid #e0e0e0;">
            <div style="font-weight: bold; color: #333; margin-bottom: 10px;">SYSTEM MESSAGE</div>
            <div style="display: flex; justify-content: space-between; margin-bottom: 10px;">
                <div>
                    <div style="font-size: 14px; color: #666;">TARGET:</div>
                    <div style="font-size: 16px;">学生档案系统</div>
                </div>
                <div>
                    <div style="font-size: 14px; color: #666;">COUNTDOWN:</div>
                    <div style="font-size: 16px;">2025-06-03 15:24:58</div>
                </div>
                <div>
                    <div style="font-size: 14px; color: #666;">系统状态:</div>
                    <div style="font-size: 16px;">在线 连接状态: 已加密</div>
                </div>
            </div>
            <div style="display: flex; justify-content: space-between;">
                <div>
                    <div style="font-size: 14px; color: #666;">数据同步:</div>
                    <div style="font-size: 16px;">最后同步: 2分钟前</div>
                </div>
                <div>
                    <div style="font-size: 14px; color: #666;">安全等级:</div>
                    <div style="font-size: 16px;">高级</div>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)

# ==================== 简易音乐播放器 ====================
elif page == "简易音乐播放器":
    st.set_page_config(page_title='音乐网站', page_icon='🐹')
    
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
    
    if 'ind' not in st.session_state:
        st.session_state['ind'] = 0
    
    current_song = music_data[st.session_state['ind']]
    
    st.title('🎵 简易音乐播放器')
    c1, c2 = st.columns([1,2])
    
    def nextImg():
        st.session_state['ind'] = (st.session_state['ind'] + 1) % len(music_data)
    
    def prevImg():
        st.session_state['ind'] = (st.session_state['ind'] - 1 + len(music_data)) % len(music_data)
    
    with c1:
        st.image(current_song['img'], width=200)
        st.text(current_song['text'])
    
    with c2:
        st.subheader(f"{current_song['title']}")
        st.text(f"歌手: {current_song['artist']}")
        st.text(f"时长: {current_song['time']}")
        button_col1, button_col2 = st.columns(2)
        
        with button_col1:
            st.button('⏮ 上一首', use_container_width=True, on_click=prevImg)
        
        with button_col2:
            st.button('⏭ 下一首', use_container_width=True, on_click=nextImg)
    
    with st.container():
        st.audio(current_song['url'])

# ==================== 视频播放网站 ====================
elif page == "视频播放网站":
    st.set_page_config(page_title="视频中心")
    
    video_arr = [
        {'url':'https://www.w3school.com.cn/example/html5/mov_bbb.mp4', 'title':'不知名-第一集'},
        {'url':'https://www.w3schools.com/html/movie.mp4', 'title':'不知名-第二集'},
        {'url':'https://media.w3.org/2010/05/sintel/trailer.mp4', 'title':'不知名-第三集'}
    ]
    
    if 'ind' not in st.session_state:
        st.session_state['ind'] = 0
    
    st.title(video_arr[st.session_state['ind']]['title'])
    st.video(video_arr[st.session_state['ind']]['url'])
    
    def playVideo(e):
        st.session_state['ind'] = int(e)
    
    cols = st.columns(len(video_arr))
    for i, col in enumerate(cols):
        with col:
            st.button(f'第{i+1}集', use_container_width=True, on_click=playVideo, args=(i,))
