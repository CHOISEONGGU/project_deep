import streamlit as st
import base64
from pydub.playback import play
from Functional import GetResult

def set_page(): 
    st.set_page_config(page_title="for Doksan Seo teacher",
                        page_icon="🏕️", 
                        layout="wide", 
                        initial_sidebar_state="auto",
                        )

class User_Interface :
    def __init__(self) -> None:
        self.cut = st.markdown("---")
        
    def cutting(self): return self.cut

    def set_background(self): 
        st.markdown("""<style>
                    .main {
                            background-image: url('https://t1.daumcdn.net/cfile/blog/99C6924C5B65B8BD02');
                            background-size: cover;
                        }
                        </style> """, unsafe_allow_html=True)
        
    def start_background(self): 
        st.markdown("""<style>
                    .main {
                            background-image: url('https://i.imgur.com/idnsDBs.gif');
                            background-size: cover;
                        }
                    </style> """, unsafe_allow_html=True)

    def title_ment(self, area, direction, count) : 
        st.markdown(f"<div style='background-color: green; \
                            padding: 10px; color: white; font-size: 48px;\
                            font-weight: bold; display: inline-block;'> \
                            👉{area} {direction} {count}곳 의 업체 결과\
                            </div>", unsafe_allow_html=True) 
    def refactoring_ment(self): 
        st.markdown(f"<div style='background-color: white; \
                        padding: 10px; color: green; font-size: 48px;\
                        font-weight: bold; display: inline-block;'> \
                        👉{ment} \
                        </div>", unsafe_allow_html=True)
    def sidebar_print_df(self, df):
        if len(df) > 10 :
            st.write("# Best!"), st.dataframe(df.head(), width=600)
            st.write("# Worst!"), st.dataframe(df.tail(), width=600)
        else : 
            st.write("분석할 업체의 수 가 충분하지 않습니다.")  

class User_Experience :
    def __init__(self) -> None:
        self.audio_path = "DL_Project/Data_csv/outdoor_crackling_fire_sound.mp3"
        self.audio = open(self.audio_path, 'rb').read()

    def set_BGM(self):
        st.markdown(f'<audio autoplay loop="true" src="data:audio/mp3;base64,\
                    {base64.b64encode(self.audio).decode()}"></audio>',\
                    unsafe_allow_html = True)          











