import streamlit as st
import pandas as pd
from st_aggrid import AgGrid

# https://pablocfonseca-streamlit-aggrid-examples-example-jyosi3.streamlitapp.com/

df = pd.DataFrame({'col1': [1, 2, 3], 'col2': [4, 5, 6]})
AgGrid(
    df
)