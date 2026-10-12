import requests

def fetch_profile(user_id):
    response = requests.get(f"https://api.example.com/users/{user_id}")
    return response.json()
