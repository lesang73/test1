import requests
import os

base_id = os.environ.get("AIRTABLE_BASE_ID")
api_key = os.environ.get("AIRTABLE_API_KEY")
table_name = os.environ.get("AIRTABLE_TABLE_NAME")

headers = {
    'Authorization': f'Bearer {api_key}',
}

url = f'https://api.airtable.com/v0/{base_id}/{table_name}'

response = requests.get(url, headers=headers)

print(response.json())
