import streamlit as st
import pandas as pd
from pathlib import Path

# Load CSS
def load_css():
    with open('assets/style.css') as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

# Load templates
def load_template(page):
    template_path = f'templates/{page}.html'
    return Path(template_path).read_text()

# Home Page
def home():
    st.markdown(load_template('home'), unsafe_allow_html=True)

# About Page
def about():
    st.markdown(load_template('about'), unsafe_allow_html=True)

# Contact Page
def contact():
    st.markdown(load_template('contact'), unsafe_allow_html=True)

# Classes Page
def classes():
    st.markdown(load_template('classes'), unsafe_allow_html=True)

# Login Page
def login():
    st.markdown(load_template('login'), unsafe_allow_html=True)
    username = st.text_input("Username")
    password = st.text_input("Password", type='password')
    if st.button("Login"):
        st.write("Login Successful")

# Student Data Form
def student_form():
    st.header("Student Data Entry Form")
    name = st.text_input("Student Name")
    grade = st.selectbox("Grade", ["Junior", "Grade 1", "Grade 2", "Grade 12"])
    status = st.selectbox("Status", ["Free", "Paid", "Pending"])
    
    # Save data to an Excel sheet
    if st.button("Submit"):
        data = {'Name': [name], 'Grade': [grade], 'Status': [status]}
        df = pd.DataFrame(data)
        df.to_excel(f'uploads/{name}_details.xlsx')
        st.success(f"Details for {name} saved successfully!")

# Student Search Form
def search_student():
    st.header("Search Student")
    search_name = st.text_input("Enter Student Name or ID")
    
    if st.button("Search"):
        try:
            df = pd.read_excel(f'uploads/{search_name}_details.xlsx')
            st.write(df)
        except FileNotFoundError:
            st.error("Student not found.")

# Main App
def main():
    load_css()
    st.sidebar.title("Navigation")
    menu = st.sidebar.selectbox("Menu", ["Home", "About", "Contact", "Classes", "Login", "Student Form", "Search Student"])
    
    if menu == "Home":
        home()
    elif menu == "About":
        about()
    elif menu == "Contact":
        contact()
    elif menu == "Classes":
        classes()
    elif menu == "Login":
        login()
    elif menu == "Student Form":
        student_form()
    elif menu == "Search Student":
        search_student()

if __name__ == "__main__":
    main()
