import streamlit as st
import pandas as pd
from ag_grid import ag_grid

df = pd.DataFrame(
    [
        {
            "Product": "Laptop",
            "Category": "Electronics",
            "Price": 1200,
            "Stock": 50,
            "Brand": "BrandA",
        },
        {
            "Product": "Smartphone",
            "Category": "Electronics",
            "Price": 800,
            "Stock": 150,
            "Brand": "BrandB",
        },
        {
            "Product": "Tablet",
            "Category": "Electronics",
            "Price": 300,
            "Stock": 100,
            "Brand": "BrandC",
        },
        {
            "Product": "Headphones",
            "Category": "Accessories",
            "Price": 150,
            "Stock": 200,
            "Brand": "BrandD",
        },
        {
            "Product": "Smartwatch",
            "Category": "Wearables",
            "Price": 200,
            "Stock": 120,
            "Brand": "BrandE",
        },
    ]
)

column_defs = [
    {"field": "Product", "filter": True, "editable": True},
    {"field": "Category", "filter": True, "editable": True},
    {
        "field": "Price",
        "filter": True,
        "editable": True,
        "valueFormatter": "value.toLocaleString('pt-BR', { style: 'currency', currency: 'BRL' })",
    },
    {"field": "Stock", "filter": True, "editable": True},
    {"field": "Brand", "filter": True, "editable": True},
]

edited_dataframe = ag_grid(
    df=df,
    column_defs=column_defs,
    style="height: 500px; width: 620px",
    locale_text="AG_GRID_LOCALE_BR",
    row_selection="multiple",
    key="my_grid",
)
st.write(edited_dataframe)
