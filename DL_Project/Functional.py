from SideBar import GetSideBar
from Data import GetData

import random
import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import matplotlib.pyplot as plotly

class GetResult:
    def __init__(self) -> None:
        self.df, \
        self.area, \
        self.direction = GetSideBar().choice_result_sidebar()

        self.total, \
        self.gapyeong, \
        self.pocheon = GetData().create_price()

    def handle_df(self, df) :
        if df is not None :
            df = (df.drop_duplicates(subset=['name'], keep='first')\
                    .sort_values(by='ranking', ascending=False)\
                    [['name', 'ranking']]\
                    .rename(columns={'name': '🏕️ 업체명', 'ranking': '⭐ 별점'})\
                    .reset_index(drop=True))
            df.index.name = "🏆 순위"
            df.index += 1
            return df
            
        else : return None

    def handle_price(self, dic) : 
        if dic == "전체" : df = self.total
        elif dic == "가평군" : df = self.gapyeong
        elif dic == "포천시" : df = self.pocheon
        else : df = None

        keyword = pd.DataFrame(df["🤜가격 산정"][:11]).transpose()
        colors = ['rgb({},{},{})'.format(random.randint(0,255), random.randint(0,255), random.randint(0,255)) for i in range(len(df))]
        fig = go.Figure(go.Bar(y=df.index, x=df["🤜가격 산정"], orientation='h', marker=dict(color=colors)))
        
        fig.update_layout(
            title='😁 옵션 별 가격 순위표 😁', 
            xaxis_title='가격', 
            yaxis_title='옵션',
            xaxis_title_font_color='black',
            yaxis_title_font_color='black',

            xaxis=dict(tickfont=dict(color='green')),
            yaxis=dict(tickfont=dict(color='green')),
            
            width = 1200,
            height = 800,
            
            plot_bgcolor='rgb(230, 245, 230)',
            paper_bgcolor='#e6f5e6'
            )
        fig.update_xaxes(tickformat=",.0f")

        st.plotly_chart(fig)
        st.dataframe(keyword)


    def choice_result(self) : return self.handle_df(self.df), self.area, self.direction

    def price_result(self): return self.handle_price(self.direction)

