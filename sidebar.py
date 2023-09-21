import streamlit as st

def create_sidebar_container():
    return st.sidebar.container()

def update_sidebar_container(container, company_name, company_address):
    container.write(f"**Company Name:** {company_name}")
    container.write(f"**Company Address:** {company_address}")
