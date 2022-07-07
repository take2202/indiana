import pandas as pd 
import streamlit as st
import numpy as np
from st_aggrid import AgGrid
from st_aggrid.shared import GridUpdateMode

from st_aggrid.grid_options_builder import GridOptionsBuilder

st.set_page_config(page_title="Indeed Analysis", layout="wide") 
st.title("Indeed Analysis")

uploaded_file = st.file_uploader("Upload CSV", type=".csv")

if uploaded_file:
    df = pd.read_csv(uploaded_file,header=1)
    df = df.dropna(axis=0)
    df = df.astype({'表示回数 スポンサー': float,'表示回数 オーガニック': float,'表示回数 合計': float,
    'クリック数 スポンサー': float,'クリック数 オーガニック': float,'クリック数 合計': float,'平均 CPC': float,'平均応募開始単価': float,'平均 CPA': float,'合計費用': float})
    df = df.reindex(columns=['ステータス','職種名','勤務地','企業名','参照番号','掲載元サイト','最終更新日','掲載日','URL',
    '表示回数 スポンサー','クリック数 スポンサー','応募開始数 スポンサー','応募数 スポンサー','クリック率 スポンサー','応募開始率 スポンサー','応募完了率 スポンサー',
    '応募率 スポンサー','平均 CPC','平均応募開始単価','平均 CPA','合計費用','表示回数 オーガニック','クリック数 オーガニック','応募開始数 オーガニック','応募数 オーガニック (internal)',
    'クリック率 オーガニック','応募開始率 オーガニック','応募完了率 オーガニック (internal)','応募率 オーガニック (internal)','表示回数 合計','クリック数 合計','応募開始数 合計','応募数 合計 (internal)',
    'クリック率 合計','応募開始率 合計','応募完了率 合計 (internal)','応募率 合計 (internal)'])
    st.markdown("### 求人パフォーマンスレポート")
    
    gb = GridOptionsBuilder.from_dataframe(df)
    gb.configure_side_bar()
    gb.configure_selection(selection_mode="multiple", use_checkbox=True)
    gb.configure_default_column(groupable=True, value=True, enableRowGroup=True, aggFunc="sum", editable=True)
    gridOptions = gb.build()

    AgGrid(df, gridOptions=gridOptions, enable_enterprise_modules=True, allow_unsafe_jscode=True, update_mode=GridUpdateMode.SELECTION_CHANGED)
    

def main():
    text = st.text_area(label='message')

if __name__ == '__main__':
    main()