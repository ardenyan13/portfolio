import streamlit as sl
import pandas

# change width of columns
sl.set_page_config(layout="wide")

# create 2 column object instances
column1, column2 = sl.columns(2)

with column1:
    sl.image("images/photo.png")

with column2:
    sl.title("Arden Yan")
    description = """
    My name is Arden! I am currently a student at San Jose State University. I plan to graduate in May 2025 with a 
    Bachelor of Science in Computer Science.
    """
    sl.info(description)

directions = """
Below you can find some of the apps and projects I have built. Feel free to contact me!
"""
sl.write(directions)

column3, column4 = sl.columns(2)

df = pandas.read_csv("data.csv", sep=";")

with column3:
    for index, row in df[:1].iterrows():
        sl.header(row["title"])

with column4:
    for index, row in df[1:].iterrows():
        sl.header(row["title"])
