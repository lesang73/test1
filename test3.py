import requests
import streamlit as st
import os
# from dotenv import load_dotenv

# .env 파일에서 환경 변수 로드
# load_dotenv()

# 환경 변수에서 API 키, Base ID, Table Name 읽어오기
base_id = os.environ.get("AIRTABLE_BASE_ID")
api_key = os.environ.get("AIRTABLE_API_KEY")
table_name = os.environ.get("AIRTABLE_TABLE_NAME")


headers = {
    'Authorization': f'Bearer {api_key}',
}

url = f'https://api.airtable.com/v0/{base_id}/{table_name}'

response = requests.get(url, headers=headers)

# Streamlit을 사용하여 결과 표시
if response.status_code == 200:
    records = response.json().get("records", [])
    if records:
        for record in records:
            st.write(record)
    else:
        st.write("No records found.")
else:
    st.error("Failed to fetch data from Airtable.")
