import pandas as pd
import streamlit as st
import plotly.express as px


st.title("Company Per District")

# Specify the file name
file_name = "MMU ITP List 13_9_9_11.xlsx"

try:
    df = pd.read_excel(file_name, engine='openpyxl')
except FileNotFoundError:
    st.error(f"File '{file_name}' not found.")

# Sidebar for state selection
if df is not None:
    selected_state = st.sidebar.selectbox("Select a State", df['STATE'].unique())
else:
    selected_state = None

# Data processing
if df is not None:
    grouped_data = df.groupby(['STATE', 'CITY']).size().reset_index(name='CompanyCount')
    grouped_data = grouped_data.sort_values(by=['STATE', 'CompanyCount'], ascending=[True, False])

    # Create bar chart
    if selected_state:
        filtered_data = grouped_data[grouped_data['STATE'] == selected_state]
        fig = px.bar(
            filtered_data,
            x='CompanyCount',
            y='CITY',
            orientation='h',
            labels={'CITY': 'City', 'CompanyCount': 'Number of Companies'},
            title=f'Company Distribution per City in {selected_state}'
        )
    else:
        fig = px.bar(
            grouped_data,
            x='CompanyCount',
            y='CITY',
            orientation='h',
            labels={'CITY': 'City', 'CompanyCount': 'Number of Companies'},
            title='Company Distribution per City in Malaysia (Sorted by State and City)'
        )

    # Display the plotly figure
    st.plotly_chart(fig)
