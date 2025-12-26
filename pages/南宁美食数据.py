import streamlit as st
import pandas as pd
import numpy as np
import random

# 设置页面配置
st.set_page_config(
    page_title="南宁美食数据仪表盘",
    page_icon="🍜",
    layout="wide"
)

# 简化的CSS样式
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

# 标题
st.markdown('<h1 class="main-header">🍜 南宁美食数据仪表盘</h1>', unsafe_allow_html=True)

# 餐厅数据
restaurants_data = {
    "餐厅": ["甘家界牌柠檬鸭", "中山路美食街", "万国酒家", "复记老友粉", "阿光烧烤", 
             "舒记老友", "老友记", "三品王", "梁记卷筒粉", "建政路夜市"],
    "类型": ["桂菜", "小吃街", "粤菜", "老友粉", "烧烤", "老友粉", "老友粉", "快餐", "小吃", "夜市"],
    "评分": [4.6, 4.4, 4.5, 4.3, 4.2, 4.4, 4.1, 4.0, 4.3, 4.5],
    "人均消费(元)": [68, 35, 88, 18, 45, 20, 16, 25, 12, 30],
    "latitude": [22.8170, 22.8220, 22.8190, 22.8122, 22.7950, 22.8350, 22.8250, 22.8420, 22.8280, 22.8180],
    "longitude": [108.3665, 108.3565, 108.3685, 108.2666, 108.3465, 108.3185, 108.3765, 108.3250, 108.3850, 108.3450]
}

# 创建DataFrame
df = pd.DataFrame(restaurants_data)

# 生成12个月的价格走势数据
@st.cache_data
def generate_price_trends():
    months = ['1月', '2月', '3月', '4月', '5月', '6月', 
              '7月', '8月', '9月', '10月', '11月', '12月']
    
    price_trends = []
    for _, restaurant in df.iterrows():
        base_price = restaurant['人均消费(元)']
        for i, month in enumerate(months):
            # 模拟季节性价格波动
            seasonal_factor = 1 + 0.1 * np.sin(2 * np.pi * i / 12)
            random_factor = 1 + np.random.normal(0, 0.03)
            price = base_price * seasonal_factor * random_factor
            
            price_trends.append({
                '餐厅': restaurant['餐厅'],
                '月份': month,
                '价格': round(price, 2)
            })
    
    return pd.DataFrame(price_trends)

# 生成月度销售数据
@st.cache_data
def generate_monthly_sales():
    months = ['1月', '2月', '3月', '4月', '5月', '6月', 
              '7月', '8月', '9月', '10月', '11月', '12月']
    
    sales_data = []
    for _, restaurant in df.iterrows():
        base_sales = random.randint(1200, 3500)
        for i, month in enumerate(months):
            # 模拟销售波动
            seasonal_factor = 1 + 0.15 * np.sin(2 * np.pi * i / 12 + np.pi/4)
            random_factor = 1 + np.random.normal(0, 0.1)
            sales = base_sales * seasonal_factor * random_factor
            
            sales_data.append({
                '餐厅': restaurant['餐厅'],
                '月份': month,
                '销量': int(sales)
            })
    
    return pd.DataFrame(sales_data)

# 获取数据
price_df = generate_price_trends()
sales_df = generate_monthly_sales()

# 侧边栏筛选
st.sidebar.title("📊 数据筛选")
selected_type = st.sidebar.selectbox(
    "选择餐厅类型",
    ["全部", "桂菜", "小吃街", "粤菜", "老友粉", "烧烤", "快餐", "小吃", "夜市"]
)

# 筛选数据
if selected_type != "全部":
    df_filtered = df[df['类型'] == selected_type]
    price_df_filtered = price_df[price_df['餐厅'].isin(df_filtered['餐厅'])]
    sales_df_filtered = sales_df[sales_df['餐厅'].isin(df_filtered['餐厅'])]
else:
    df_filtered = df
    price_df_filtered = price_df
    sales_df_filtered = sales_df

# 顶部指标卡片
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

# 主要内容区域
st.header("📊 数据可视化分析")

# 第一行：柱状图和折线图
col1, col2 = st.columns(2)

with col1:
    st.subheader("📊 餐厅评分对比")
    chart_data = df_filtered.set_index('餐厅')['评分']
    st.bar_chart(chart_data, color="#FF6B35")

with col2:
    st.subheader("📈 月度销量趋势")
    line_data = sales_df_filtered.pivot(index='月份', columns='餐厅', values='销量')
    st.line_chart(line_data)

# 第二行：面积图和价格走势图
col1, col2 = st.columns(2)

with col1:
    st.subheader("📉 销量面积图")
    area_data = sales_df_filtered.groupby('月份')['销量'].sum()
    st.area_chart(area_data, color="#667eea")

with col2:
    st.subheader("💹 12个月价格走势")
    price_data = price_df.pivot(index='月份', columns='餐厅', values='价格')
    st.line_chart(price_data)

# 地图展示
st.header("🗺️ 餐厅地理位置分布")

# 创建地图数据
map_data = df_filtered[['latitude', 'longitude']].rename(columns={
    'latitude': 'lat',
    'longitude': 'lon'
})

# 使用Streamlit内置地图
st.map(map_data, zoom=10, use_container_width=True)

# 添加餐厅信息
st.subheader("📍 餐厅位置信息")
for _, row in df_filtered.iterrows():
    st.write(f"**{row['餐厅']}** - {row['类型']} | 评分: {row['评分']} | 人均: ¥{row['人均消费(元)']}")

# 详细数据表格
st.header("📋 餐厅详细信息")

# 格式化数据展示
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

# 页脚
st.markdown("---")
st.markdown("""
<div style='text-align: center; color: #718096; margin-top: 1rem;'>
    <p>🍜 南宁美食数据仪表盘 | 数据更新时间：2025年12月22日 09:28</p>
    <p>探索南宁地道美食，品味壮乡风情 🌟</p>
</div>
""", unsafe_allow_html=True)
