import streamlit as st

# 设置页面配置：标题、布局和图标
st.set_page_config(page_title="个人简历生成器", layout="wide", page_icon='👨‍🎓')

# 创建两列布局，比例为1:2
c1, c2 = st.columns([1, 2])

# 左侧列：用户信息输入区域
with c1:
    # 姓名输入框
    user_name = st.text_input("姓名")
    
    # 职位输入框
    user_work = st.text_input("职位")
    
    # 手机号输入框
    user_phone = st.text_input("手机号")
    
    # 邮箱输入框
    user_email = st.text_input("邮箱")
    
    # 出生日期选择器
    user_date = st.date_input("出生日期")
    
    # 性别单选按钮，水平排列，默认选择"男"
    user_sex = st.radio('性别', ['男', '女', '其他'], horizontal=True, index=0)
    
    # 学历下拉选择框
    use_xl = st.selectbox(
        '学历',
        ['初中', '中专', '高中', '大专', '本科', '研究生', '博士']
    )
    
    # 语言能力多选框
    user_language = st.multiselect(
        '语言能力',
        ['中文', '英语', '法语', '日语', '俄语', '西班牙语']
    )
    
    # 技能能力多选框
    user_jineng = st.multiselect(
        '技能能力',
        ['Java', 'Python', 'HTML', 'Js', 'Type/Scripts', 'C++']
    )
    
    # 工作经验滑块，范围0-30年
    use_age = st.slider('工作经验', 0, 30)
    
    # 期望薪资范围滑块，范围5000-12000，默认值(6000, 8000)
    salary_range = st.slider('期望薪资范围', 5000, 12000, (6000, 8000))
    
    # 个人简介文本区域
    user_grjj = st.text_area(label='个人简介：', placeholder='请输入您的个人简介')
    
    # 每日最佳联系时间选择器
    user_time = st.time_input("每日最佳联系时间:")
    
    # 头像上传器，支持jpg、jpeg、png、webp格式
    user_avatar = st.file_uploader(
        "上传头像",
        type=['jpg', 'jpeg', 'png', 'webp'],
        help="支持 jpg, png, webp 格式"
    )

# 右侧列：简历预览区域
with c2:
    # 标题
    st.header("简历预览")
    
    # 如果没有输入姓名，显示提示信息
    if not user_name:
        st.info("请在左侧输入信息以生成简历。")
    else:
        # 创建头部区域：头像 + 姓名（分为两列）
        col_avatar, col_title = c2.columns([1, 3])
        
        with col_avatar:
            # 显示上传的头像，如果没有上传则显示默认头像图标
            if user_avatar is not None:
                st.image(user_avatar, width=150, use_container_width=False)
            else:
                st.markdown("### 👤")
        
        with col_title:
            # 显示姓名
            st.title(user_name)
            # 显示职位
            st.write(f"*{user_work}*")
        
        # 分割线
        st.divider()
        
        # 创建两列布局显示基本信息
        col_a, col_b = c2.columns(2)
        
        with col_a:
            # 显示手机号码
            st.write(f"**手机号码：** {user_phone}")
            # 显示电子邮箱
            st.write(f"**电子邮箱：** {user_email}")
        
        with col_b:
            # 显示性别
            st.write(f"**性别：** {user_sex}")
            # 显示出生日期
            st.write(f"**出生日期：** {user_date}")
            # 显示最高学历
            st.write(f"**最高学历：** {use_xl}")
        
        # 分割线
        st.divider()
        
        # 个人简介部分
        st.subheader("个人简介")
        st.write(user_grjj)
        
        # 技能与能力部分
        st.subheader("技能与能力")
        # 显示工作经验
        st.write(f"**工作经验：** {use_age} 年")
        # 显示期望薪资范围
        st.write(f"**期望薪资：** {salary_range[0]} - {salary_range[1]} 元")
        # 显示掌握技能
        st.write(f"**掌握技能：** {', '.join(user_jineng) if user_jineng else '暂无'}")
        # 显示语言能力
        st.write(f"**语言能力：** {', '.join(user_language) if user_language else '暂无'}")
        
        # 显示最佳联系时间
        st.write(f"**最佳联系时间：** {user_time}")
