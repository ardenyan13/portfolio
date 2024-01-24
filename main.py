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

column3, empty_column, column4 = sl.columns([1.5, 0.5, 1.5])

# use pandas to get the data
df = pandas.read_csv("data.csv", sep=";")

with column3:
    for index, row in df[:1].iterrows():
        sl.header(row["title"])
        sl.write(row["description"])
        sl.image("images/" + row["image"])
        sl.write(f"[Source Code]({row['url']})")

with column4:
    for index, row in df[1:].iterrows():
        sl.header(row["title"])
        sl.write(row["description"])
        sl.image("images/" + row["image"])
        sl.write(f"[Source Code]({row['url']})")
