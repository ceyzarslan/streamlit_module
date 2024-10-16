import streamlit as st
import requests as req

st.set_page_config(layout="wide")

url = 'https://dummyjson.com/recipes?limit=0'
res = req.get(url)
if res.status_code == 200:
    recipes = res.json()['recipes']
    st.title(f"Recipes ({len(recipes)}): ")
    numCols = 5
    for i in range(0, len(recipes), numCols):
        cols = st.columns(numCols, gap='small')
        for j, col in enumerate(cols):
            if i + j < len(recipes):
                with col:
                    with st.container(border=True):
                        r = recipes[i + j]
                        st.write(r['name'])
                        st.image(r['image'])
                        st.divider()

else:
    st.error("Recipes not found")
