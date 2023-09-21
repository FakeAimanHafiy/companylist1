import streamlit as st

def sidebar():
    st.sidebar.title('Company Information')
    
    # Create a container in the sidebar
    container = st.sidebar.container()
    
    # Add some text to the container
    container.write('This is a test container.')
    
    # You can add more content to the container as needed
    container.write('You can add more text or widgets here.')

    st.empty()  # This can be used to create empty space between the sidebar and the main content
