import streamlit as st

def sidebar():
    # Create a container in the sidebar
    sidebar_container = st.sidebar.container()

    # Add content to the container
    with sidebar_container:
        st.title('Company Information')
        st.header('Sidebar Header')
        st.write('This is the sidebar content.')

    # You can add more content to the sidebar outside the container if needed
    # st.sidebar.write('Other sidebar content here')

