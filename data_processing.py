import pandas as pd
import streamlit as st
import plotly.express as px

def process_data(file_name):
    try:
        df = pd.read_excel(file_name, engine='openpyxl')
    except FileNotFoundError:
        st.error(f"File '{file_name}' not found.")
        return None

    return df

def generate_bar_chart(df, selected_state=None):
    if df is not None:
        grouped_data = df.groupby(['STATE', 'CITY']).size().reset_index(name='CompanyCount')
        grouped_data = grouped_data.sort_values(by=['STATE', 'CompanyCount'], ascending=[True, False])

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

        return fig
    else:
        return None
