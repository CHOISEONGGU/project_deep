import streamlit as st
from Functional import GetResult

st.set_page_config(page_title="DL", layout="wide")

def get() : return GetResult().get_result()

def user_interface():
    st.error("## TDD - Testing...")
    df, area, direction, address = get()

    # 사이드바 
    with st.sidebar : 
        if df is not None : 
            st.write("일치하는 업체가 없습니다.") if df.empty else st.dataframe(df)
    
    # U_I
    st.write(f"""
            ### 지역 선택 = {area}
            ### 지역 선택 후 지역들 = {direction}
            ### 유저 인풋 데이터 = {address}
            ### 데이터프레임👇df 컬럼 깨져서 나옴
    """)

    st.write(f"""
            {df}
    """)
    with st.expander("# 메커니즘_설명 / 용량이 엄청 클 것 으로 예상 되기에 백엔드적으로도 줄여서 하기 위함. "):
        st.image("https://i.imgur.com/SgRVHOk.jpg", width = 1000)

    # image = [
    #     "https://i.imgur.com/t4O7ozH.jpg", 
    #     "https://i.imgur.com/idnsDBs.gif", 
    #     "https://i.imgur.com/fvRG1Tj.gif"
    #     ]

    # for i in range(len(image)) :
    #     with st.expander(f"사진_{i+1}"):
    #         st.image(image[i])


    # containers = [st.container() for i in range(len(image))]
    # for i in range(len(image)) :
    #     with containers[i] : 
    #         st.image(image[i], width = 700)
    # # =====================================================================
    # messages = ['success', 'info', 'warning', 'error']

    # for i in range(2):
    #     for message in messages:
    #         getattr(st, message)(f'This is a {message} message')