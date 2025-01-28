import streamlit as st
from phi.agent import Agent
from phi.model.google import Gemini
from phi.tools.duckduckgo import DuckDuckGo
from google.generativeai import upload_file, get_file
import google.generativeai as gen_ai
import time
from pathlib import Path
import tempfile
from dotenv import load_dotenv
import os
import re
import shutil
import moviepy.video.io.VideoFileClip as mp
from moviepy.video.tools.subtitles import SubtitlesClip
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
from deep_translator import GoogleTranslator
import json
import ffmpeg

# Load environment variables
load_dotenv()
API_KEY = os.getenv("GOOGLE_API_KEY")
if API_KEY:
    gen_ai.configure(api_key=API_KEY)

# Streamlit Page Configuration
st.set_page_config(
    page_title="AI-Powered Video Analyzer",
    layout="wide",
    page_icon="🎥",
    initial_sidebar_state="expanded",
)

# Custom CSS for Colorful UI
st.markdown("""
    <style>
        .sidebar .sidebar-content {
            background-color: #f0f2f6;
        }
        .main { 
            background: #e8f4fd; 
            border-radius: 10px;
            padding: 20px;
        }
        .stTextArea textarea {
            background-color: #f8f9fa;
            font-size: 16px;
            border-radius: 5px;
            height: 120px;
            color: #000000;
        }
    </style>
""", unsafe_allow_html=True)

# Page Title
st.title("🎥 AI-Powered Video Analyzer")
st.header("🌟 Powered by Gemini 2.0 Flash")
