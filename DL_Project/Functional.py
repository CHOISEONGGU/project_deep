from SideBar import GetSideBar
from Data import GetData

import streamlit as st
import random
import colorsys
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
        # colors = ['rgb({},{},{})'.format(random.randint(0,255), random.randint(0,255), random.randint(0,255)) for i in range(len(df))]
        # ==================================================================
        # 색상 범위 조정을 위한 매개변수
        saturation = 0.5
        lightness = 0.8

        # 데이터프레임의 길이
        n = len(df)

        # 랜덤한 RGB 값 생성 후 HSV로 변환하여 색상 범위를 조정하고 다시 RGB로 변환
        colors = []
        for i in range(n):
            r, g, b = [random.randint(150, 255) for j in range(3)]  # 밝은 색상을 위해 범위를 150~255로 조정
            h, s, v = colorsys.rgb_to_hsv(r/255, g/255, b/255)
            s = saturation
            v = lightness
            r, g, b = [int(c*255) for c in colorsys.hsv_to_rgb(h, s, v)]
            colors.append(f'rgb({r},{g},{b})')
        # ==================================================================
        # 색상 범위
        color_range = [(228, 152, 96), (246, 185, 59), (246, 230, 164), (152, 199, 115), (79, 129, 189)]

        # 데이터프레임의 길이
        n = len(df)

        # 색상 랜덤 선택
        colors = [f'rgb({random.randint(r[0], r[1])},{random.randint(g[0], g[1])},{random.randint(b[0], b[1])})'
                for r, g, b in zip(color_range, color_range, color_range, color_range, color_range)]   
        # ================================================================== 
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

