import streamlit as st
import pandas as pd
from ag_grid import ag_grid

df = pd.DataFrame(
    [
       {"command": "st.selectbox", "rating": 4, "is_widget": True},
       {"command": "st.balloons", "rating": 5, "is_widget": False},
       {"command": "st.time_input", "rating": 3, "is_widget": True},
   ]
)
column_config = [
    { "field": name, "editable": True } for name in df.columns
]

edited_dataframe = ag_grid(
    df=df,
    column_config=column_config,
    style="height: 500px; width: 620px",
    key="my_grid"
)
st.write(edited_dataframe)

