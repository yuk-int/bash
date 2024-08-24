import streamlit as st
import redis
from dotenv import load_dotenv
import os
import json
import pandas as pd
from streamlit_autorefresh import st_autorefresh

load_dotenv()

st.title("classroom")
st.header("sensor:blue[cool] :sunglasses:")

redis_conn = redis.Redis(host='localhost', port=6379)

b_list = redis_conn.lrange('btn/func1',-10,-1)
#byte list to str
str_list = [byte.decode('utf-8') for byte in b_list]
dict = [json.loads(string) for string in str_list]
#st.write(dict)
df = pd.DataFrame(dict)


st.dataframe(df,
             hide_index=True,
             column_config={
                 "Status":st.column_config.CheckboxColumn(label="botton status", width="small"),
                 "Date":st.column_config.DatetimeColumn(label="time", width="small")
             })