import os
import requests
from dotenv import load_dotenv

load_dotenv('.env')
url = "https://api.apilayer.com/exchangerates_data/convert?to={to}&from={from}&amount={amount}"

payload = {}
headers = os.getenv(API_KEY)

response = requests.request("GET", url, headers=headers, data = payload)

status_code = response.status_code
result = response.text