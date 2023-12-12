import streamlit as st
import requests

st.title("Fake News Detector")

st.markdown('''
            The technological surge in the past few years has led to a plethora of
            misinformation being spread among the vast corners of the Internet.
            This detector aims to predict whether a given text, namely a news article,
            conveys real information, fake information, or is rather suspicious on the whole.
            ''')

st.markdown('''
            All you need to do is input a text below and we will return an answer,
            as well as the probability.
            ''')
