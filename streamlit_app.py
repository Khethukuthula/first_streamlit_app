import streamlit as st
import snowflake.connector

# Streamlit app setup
st.title("Upload Data to Snowflake")

# Snowflake connection setup
conn = snowflake.connector.connect(
    user='mhlongo',
    password='Khetha370',
    account='IU52295.ca-central-1.aws.snowflakecomputing.com',
    warehouse='INTL_WH',
    database='INTL.DB',
    schema='PUBLIC',
)

# Streamlit user interface
data_to_upload = st.text_input("ISO_Countries_UTF8_pipe(1).csv")
submit_button = st.button("Upload to Snowflake")

if submit_button and data_to_upload:
    # Data processing and Snowflake insertion
    cursor = conn.cursor()
    try:
        cursor.execute(f"INSERT INTO your_table_name (column1) VALUES ('{data_to_upload}')")
        st.success("Data uploaded successfully!")
    except Exception as e:
        st.error(f"Error: {str(e)}")

# Close the Snowflake connection
conn.close()
