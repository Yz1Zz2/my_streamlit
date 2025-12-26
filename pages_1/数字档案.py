import pandas as pd   # 导入Pandas库，用于数据处理和创建数据框
import streamlit as st  # 导入Streamlit库，用于创建Web应用


# 设置页面主标题 - 学生档案
st.title("🥇学生 小明2048-数字档案")

# 基础信息部分
st.header("🔑基础信息")
st.text("学生ID:STU-2024-005")  # 显示学生ID
st.markdown("注册时间: :green[2025-12-15]|精神状态：✅正常")  # 显示注册时间和精神状态
st.markdown("当前教室: :green[教学楼702]|安全等级：🔒机密")  # 显示当前教室和安全等级

# 技能矩阵部分
st.title("📊技能矩阵")

# 技能掌握度展示
st.subheader('技能掌握度')
# 使用三列布局展示不同编程语言的掌握程度
c1, c2, c3 = st.columns(3)
c1.metric(label="C语言",help="提示", value="95%", delta="2℃")  # C语言技能，95%掌握度，提升2℃
c2.metric(label="Pyhon",help="提示",value="86%", delta="6%")  # Python技能，86%掌握度，提升6%
c3.metric(label="Java",help="提示", value="88%", delta="-9%")  # Java技能，88%掌握度，下降9%

# 定义任务日志数据，用于创建数据框
data = {
 '作业提交数':[15, 18, 22, 20, 25],  # 每月作业提交数量
    '学习时长(小时)':[120, 145, 160, 155, 180],  # 每月学习时长
    '代码行数':[850, 1200, 1500, 1400, 1800],  # 每月编写代码行数
}
# 定义数据框的索引（月份）
index = pd.Series(['01月', '02月', '03月', '04月', '05月'], name='月份')
# 根据数据和索引创建数据框
df = pd.DataFrame(data, index=index)

# Streamlit课程进度部分
st.title("Streamlit课程进度")
# 显示进度条，当前进度为15%
st.progress(15)
# 显示进度条下方的文字说明
st.text("Streamlit课程进度")

# 任务日志表格
st.subheader('任务日志')
# 使用st.table显示数据框，以表格形式展示任务日志
st.table(df)

# 最新代码成果部分
st.subheader('💻最新代码成果')
# 创建要显示的Python代码块的内容
python_code = '''<div style="font-weight: bold; color: #333; margin-bottom: 10px;">SYSTEM MESSAGE</div>
        <div style="display: flex; justify-content: space-between; margin-bottom: 10px;">
            <div>
                <div style="font-size: 14px; color: #666;">TARGET:</div>
                <div style="font-size: 16px;">学生档案系统</div>
            </div>")
'''
# 显示代码块，包含行号
st.code(python_code, line_numbers=True)

# 分隔线
st.markdown('***')

# 系统状态部分
st.subheader("📡 系统状态")
# 显示系统标识
st.markdown(':green[>> SYSTEM]')
# 创建一个容器来显示系统消息
with st.container():
    # 系统消息框，使用HTML和CSS进行样式设计
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
