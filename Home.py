import streamlit as st
import pandas

# change width of columns
st.set_page_config(layout="wide")

# create 2 column object instances
column1, column2 = st.columns(2)

with column1:
    st.image("images/photo.png")

with column2:
    st.title("Arden Yan")
    description = """
    My name is Arden! I am currently a student at San Jose State University. I plan to graduate in May 2025 with a 
    Bachelor of Science in Computer Science.
    """
    st.info(description)

directions = """
Below you can find some of the apps and projects I have built. Feel free to contact me!
"""
st.write(directions)

column3, empty_column, column4 = st.columns([1.5, 0.5, 1.5])

# use pandas to get the data
df = pandas.read_csv("data.csv", sep=";")

with column3:
    for index, row in df[:1].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[Source Code]({row['url']})")

with column4:
    for index, row in df[1:].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[Source Code]({row['url']})")
