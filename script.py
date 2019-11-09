import requests
import json
import sys
from pprint import PrettyPrinter

pp = PrettyPrinter(indent=2)

def load_auth(fn):
    with open(fn) as f:
        data = json.load(f)
        return data["client_id"], data["client_secret"]

def get_credentials(client_id, client_secret):
    data = {
            "client_id": client_id, 
            "client_secret": client_secret,
            "grant_type": "client_credentials",
        }

    print('DATA:', data)

    r = requests.post(url='https://api.gfycat.com/v1/oauth/token', data=str(data))
    d = r.json()
    expires_in = d['expires_in']
    access_token = d['access_token']
    print('\nResponse to credentials:', access_token)
    return access_token

def download_gfy(access_token, gfyid):
    header = {'Authorization': 'Bearer {}'.format(access_token)}
    url = 'https://api.gfycat.com/v1/gfycats/{}'.format(gfyid)

    r = requests.get(url=url, headers=header)
    #print('\n\t\tResponse:')
    #pp.pprint(r.json())
    return r.json()

def largest_gif_url(response):
    return response['gfyItem']['gifUrl']

if __name__ == '__main__':
    print('OAuth File Name:', sys.argv[1])
    client_id,client_secret = load_auth(sys.argv[1])
    print("\tClient ID: {}\n\tClient Secret: {}".format(client_id,client_secret))
    access_token = get_credentials(client_id, client_secret)
    gfyid = sys.argv[2]
    response = download_gfy(access_token, gfyid)
    url = largest_gif_url(response)
    print('\n\t\tLargest Gif URL:', url)


    
