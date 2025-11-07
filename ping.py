import requests

url = "https://api.zcan.in/health"

try:
    res = requests.get(url, timeout=10)
    print(f"Pinged render server: {res.status_code}")
except Exception as e:
    print(f"Failed to hit render server: {e}")
