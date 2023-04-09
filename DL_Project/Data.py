import pandas as pd
import streamlit as st
from pydub import AudioSegment

@st.cache
class GetData:
    def __init__(self) -> None : 
        self.df_path = "DL_Project/Data_csv/glamping_test_3000.csv"
        self.df = self.load_data()

        self.audio_path1 = "DL_Project/Data_csv/crackling_wood_sound.mp3"
        self.audio_path2 = "DL_Project/Data_csv/crackling_sound_of_oak_bark.mp3"
        self.audio_path3 = "DL_Project/Data_csv/outdoor_crackling_fire_sound.mp3"
        self.audio = self.load_audio

    def load_data(self):
        try :  
            return pd.read_csv(self.df_path)
            
        except Exception as e : 
            return st.error(e)

    def load_audio(self) :
        audio1 = AudioSegment.from_file("audio1.mp3")
        audio2 = AudioSegment.from_file("audio2.mp3")
        audio3 = AudioSegment.from_file("audio3.mp3")

        add_audio = audio1 + audio2 + audio3

        add_audio.export("combined.mp3", format="mp3")
        
        return add_audio


    def create_data(self) : return self.df
    def create_audio(self) : return self.audio
