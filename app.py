import pandas as pd
import streamlit as st
from deta import Deta  # pip install deta
from datetime import datetime
from deta import Deta  # pip install deta


DETA_KEY = st.secrets.deta.DETA_KEY
deta = Deta(DETA_KEY)
db = deta.Base("MacAddress")


check_date = st.date_input("날짜를 선택해주세요",datetime.now())

if check_date:
    temp = db.fetch(query={'datetime?contains':f'{check_date}'}).items
    if len(temp)>1:
        df = pd.DataFrame(temp)
        df_count = df.groupby(['Mac']).count()
        macs= df['Mac'].unique().tolist()
        st.write(df_count)
        st.write(f'활성이용 갯수 : {len(macs)}')
        st.write(macs)
    else:
        st.write("없어요")