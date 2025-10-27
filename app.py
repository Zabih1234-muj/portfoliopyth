import streamlit as st
import streamlit.components.v1 as components

# Page configuration
st.set_page_config(page_title="My Portfolio", page_icon=":tada:", layout="centered")

# Header
st.title("Welcome to My Portfolio")
st.subheader("Hi, I'm Zabih Ullah!")
st.write("This is my personal portfolio built with Streamlit.")

# About Me Section
st.header("About Me")
st.write("""
I am a Full Stack Developer / Data Analyst / Designer.
I love creating web apps, data visualizations, and interactive dashboards.
""")

# Projects Section
st.header("Projects")
projects = {
    "Project 1": "A simple calculator app using Streamlit.",
    "Project 2": "Data analysis dashboard with Python & Pandas.",
    "Project 3": "Interactive portfolio website.",
}

for project, description in projects.items():
    st.subheader(project)
    st.write(description)

# Optional: Embed HTML
st.header("Custom HTML Section")
html_code = """
<div style="background-color:lightblue; padding:20px; text-align:center; border-radius:10px;">
<h2>Hello from HTML!</h2>
<p>You can style this however you like.</p>
</div>
"""
components.html(html_code, height=150)

# Contact Section
st.header("Contact Me")
st.write("Email: zabihullah@example.com")
st.write("LinkedIn: [Zabih Ullah](https://www.linkedin.com)")
st.write("GitHub: [Zabih Ullah](https://github.com)")

