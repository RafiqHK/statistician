import streamlit as st
import pandas as pd

def upload_file():
    uploaded_file = st.file_uploader("Upload an Excel file", type=["xlsx", "xls"])
    if uploaded_file is not None:
        try:
            df = pd.read_excel(uploaded_file)
            st.success("File uploaded successfully!")
            return df
        except Exception as e:
            st.error(f"Error loading file: {str(e)}")
    return None