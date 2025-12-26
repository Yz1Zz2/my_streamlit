import numpy as np
import pandas as pd
import streamlit as st
import plotly.express as px


pd.set_option('display.unicode.east_asian_width', True)

def get_dataframe_from_excel():
    # 请确保 Excel 文件在当前目录下
    df = pd.read_excel('（商场销售数据）supermarket_sales.xlsx',
                     sheet_name='销售数据',
                     skiprows=1,
                     index_col='订单号'
                     )
    df['小时数'] = pd.to_datetime(df['时间'], format="%H:%M:%S").dt.hour
    return df

# [修正2] Streamlit 是 web 应用，print 不会直接显示在页面上，建议删除或保留调试用
sale_df = get_dataframe_from_excel()

def add_sidebar_func(df):
    with st.sidebar:
        st.header("请筛选数据：")
        
        # 1. 城市筛选
        city_unique = df["城市"].unique()
        city = st.multiselect(
            "选择城市", # 建议加上 label
            options=city_unique,
            default=city_unique,
        )

        # 2. 顾客类型筛选
        customer_type_unique = df["顾客类型"].unique()
        customer_type = st.multiselect(  # [修正3] 变量名改为 customer_type，不要覆盖上面的 unique
            "选择顾客类型",
            options=customer_type_unique,
            default=customer_type_unique,
        )
        
        # 3. 性别筛选
        gender_unique = df["性别"].unique()
        gender = st.multiselect(  # [修正4] 修正了缩进，现在与 gender_unique 对齐
            "选择性别",
            options=gender_unique,
            default=gender_unique,
        )

    # [修正5] query 和 return 移到了 with 块外面，结构更清晰
    # [修正6] 修正了 query 中的变量拼写: @ciy -> @city
    df_selection = df.query("城市==@city & 顾客类型==@customer_type & 性别==@gender")

    return df_selection

def product_line_chart(df):
    sales_by_product_line=(df_selection.groupby(by=['产品类型'])[["总价"]].sum().sort_values(by="总价"))
    fig_product_sales=px.bar(
        sales_by_product_line,
        x="总价",
        y=sales_by_product_line.index,
        orientation="h",
        title="<b>按产品类型划分的销售额</b>"

    
        )
    return fig_product_sales

def hour_chart(df):

    sales_by_hour=(
         df.groupby(by=["小时数"])[["总价"]].sum()
    )
       
    fig_hour_sales=px.bar(
            sales_by_hour,
            x=sales_by_hour.index,
            y="总价",
            title="<b>按小时数划分的销售额</b>"
            )
    return fig_hour_sales
       
def main_page_demo(df):
    st.title('📊销售仪表板')
    left_key_col,middle_key_col,right_key_col=st.columns(3)
    total_sales=int(df['总价'].sum())
    average_rating=round(df['评分'].mean(),1)
    star_rating_string=":star:"*int(round(average_rating,0))
    average_sale_by_transaction=round(df["总价"].mean(),2)
    with left_key_col:
        st.subheader("总销售额：")
        st.subheader(f'RMB ${total_sales:,}')
    with middle_key_col:
        st.subheader("顾客评分的平均值")
        st.subheader(f'{average_rating}{star_rating_string}')
    with right_key_col:
        st.subheader("每单的平均销售额")
        st.subheader(f'RMB ${average_sale_by_transaction}')

    st.divider()
    left_chart_col,right_chart_col=st.columns(2)
    with left_chart_col:
        hour_fig=hour_chart(df)
        st.plotly_chart(hour_fig,use_container_width=True)
    with right_chart_col:
        product_fig=product_line_chart(df)
        st.plotly_chart(product_fig,use_container_width=True)
def run_app():
        st.set_page_config(
            page_title="销售仪表板",
            page_icon=":bar_chart:",
            layout="wide"
        )
        

sale_df=get_dataframe_from_excel()
df_selection = add_sidebar_func(sale_df)
product_fig=product_line_chart(df_selection)
main_page_demo(df_selection)
if __name__=="__main__":
    run_app()

