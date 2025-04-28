import requests

CLIENT_ID = 'g0a6hxzhzx72ojxtbkehh368y60pia'
CLIENT_SECRET = 'q3y5w7wkbkoit88k8fq3vjc9h4wpsq'

def gerar_token():
    url = 'https://id.twitch.tv/oauth2/token'
    params = {
        'client_id': CLIENT_ID,
        'client_secret': CLIENT_SECRET,
        'grant_type': 'client_credentials'
    }
    response = requests.post(url, params=params)
    if response.status_code == 200:
        data = response.json()
        print('TOKEN GERADO COM SUCESSO:')
        print('Access Token:', data['access_token'])
        print('Expira em:', data['expires_in'], 'segundos')
    else:
        print('Erro ao gerar token:')
        print(response.status_code)
        print(response.json())

if __name__ == '__main__':
    gerar_token()
