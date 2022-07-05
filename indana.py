import pandas as pd 
import streamlit as st
import numpy as np
from st_aggrid import AgGrid
from st_aggrid.grid_options_builder import GridOptionsBuilder


st.set_page_config(page_title="Indeed Analysis", layout="wide") 
st.title("Indeed Analysis")

uploaded_file = st.file_uploader("Upload CSV", type=".csv")

if uploaded_file:
    df = pd.read_csv(uploaded_file,header=1)

    st.markdown("### 求人パフォーマンスレポート")
    
    gb = GridOptionsBuilder.from_dataframe(df)
    gb.configure_side_bar()
    gb.configure_default_column(groupable=True, value=True, enableRowGroup=True, aggFunc="sum", editable=True)
    gridOptions = gb.build()

    AgGrid(df, gridOptions=gridOptions, enable_enterprise_modules=True)

def main():
    text = st.text_area(label='message')

if __name__ == '__main__':
    main()
    
    
