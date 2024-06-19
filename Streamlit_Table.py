import streamlit as st
import pandas as pd
import seaborn as sns

dataset=st.container()

with dataset:
    st.write("Titanic Dataset")
    df=sns.load_dataset('titanic')
    st.write(df.head())
    st.write("Male Vs Female")
    st.bar_chart(df.sex.value_counts())