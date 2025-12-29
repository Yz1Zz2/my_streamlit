import pandas as pd
import pickle
import streamlit as st


def introduce_page():
    """
    应用介绍页面
    显示应用的欢迎信息和背景介绍
    """
    st.write("# 欢迎使用")
    st.sidebar.success("单击预测医疗费用")
    st.markdown(
        """
        # 预测医疗费用
        这个应用利用机器学习模型来预测医疗费用，为保险公司的保险定价提供参考。
        
        ## 背景介绍
        - 开发目标: 帮助保险公司合理定价保险产品，控制风险
        - 模型算法: 利用随机森林回归算法训练医疗费用预测模型
        
        ## 使用指南
        - 输入准确完整的被保险人信息，可以得到更准确的费用预测
        - 预测结果可以作为保险定价的重要参考，但需审慎决策
        - 有任何问题欢迎联系我们的技术支持
        技术支持: 📧[support@example.com](mailto:support@example.com)
        """
    )


def predict_page():
    """
    预测页面
    处理用户输入并使用机器学习模型进行医疗费用预测
    """
    st.markdown(
        """
        ## 使用说明
        这个应用利用机器学习模型来预测医疗费用，为保险公司的保险定价提供参考
        - **输入信息**：在下面输入被保险人的个人信息、疾病信息等
        - **输入信息**：在下面输入被保险人的个人信息、疾病信息等
        """
    )

    # 创建用户输入表单
    with st.form("user_inputs"):
        # 年龄输入（最小值为0）
        age = st.number_input("年龄", min_value=0)
        
        # 性别选择（单选按钮）
        sex = st.radio("性别", options=["男性", "女性"])
        
        # BMI输入（最小值为0.0）
        bmi = st.number_input("BMI", min_value=0.0)
        
        # 子女数量输入（步长为1，最小值为0）
        children = st.number_input("子女数量", step=1, min_value=0)
        
        # 吸烟状态选择（单选按钮）
        smoke = st.radio("是否吸烟", ("是", "否"))
        
        # 地区选择（下拉框）
        region = st.selectbox("区域", ["东南部", "西南部", "东北部", "西北部"])
        
        # 提交按钮
        submitted = st.form_submit_button("预测费用")
        
        # 当表单提交时
        if submitted:
            # 格式化原始输入数据
            raw_format_data = [age, sex, bmi, children, smoke, region]
            
            # 初始化性别相关变量
            sex_female, sex_male = 0, 0
            
            # 根据性别设置对应的数值（用于模型输入）
            if sex == "女性":
                sex_female = 1
            elif sex == "男性":
                sex_male = 1
                
            # 初始化吸烟状态变量
            smoke_yes, smoke_no = 0, 0
            
            # 根据吸烟状态设置对应的数值
            if smoke == "是":
                smoke_yes = 1
            elif smoke == "否":
                smoke_no = 1
                
            # 初始化地区相关变量
            region_northeast, region_southeast, region_northwest, region_southwest = 0, 0, 0, 0
            
            # 根据地区设置对应的数值
            if region == "东北部":
                region_northeast = 1
            elif region == "东南部":
                region_southeast = 1
            elif region == "西北部":
                region_northwest = 1
            elif region == "西南部":
                region_southwest = 1
                
            # 转换为模型需要的格式数据
            model_format_data = [
                age,
                bmi,
                children,
                sex_female,
                sex_male,
                smoke_no,
                smoke_yes,
                region_northeast,
                region_southeast,
                region_northwest,
                region_southwest
            ]
            
            # 加载预训练的随机森林模型
            with open("rfr_model.pkl", "rb") as f:
                rfr_model = pickle.load(f)
                
            # 将数据转换为DataFrame格式
            format_data_df = pd.DataFrame(data=[model_format_data], columns=rfr_model.feature_names_in_)
            
            # 进行预测
            predict_result = rfr_model.predict(format_data_df)[0]
            
            # 显示预测结果
            st.write("根据您输入的数据，预测该客户的医疗费用是：", round(predict_result, 2))
            
            # 显示技术支持信息
            st.write("技术支持: 📧[support@example.com](mailto:support@example.com)")


# 设置页面配置
st.set_page_config(page_title="医疗费用预测", page_icon="🏥")

# 创建侧边栏导航
nav = st.sidebar.radio("导航", ["简介", "预测医疗费用"])

# 根据导航选择显示不同页面
if nav == "简介":
    introduce_page()
else:
    predict_page()
