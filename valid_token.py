import requests

TWITCH_CLIENT_ID = 'g0a6hxzhzx72ojxtbkehh368y60pia'
TWITCH_ACCESS_TOKEN = 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9...'
CHANNEL_NAME = 'furiatv'

url = f"https://api.twitch.tv/helix/streams?user_login={CHANNEL_NAME}"
headers = {
    'Client-ID': TWITCH_CLIENT_ID,
    'Authorization': f'Bearer {TWITCH_ACCESS_TOKEN}'
}

response = requests.get(url, headers=headers)
print(response.status_code)
print(response.json())
