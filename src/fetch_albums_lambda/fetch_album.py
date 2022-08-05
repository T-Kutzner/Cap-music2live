import requests
import base64
import boto3
from datetime import datetime
import os


GET_TOKEN_URL = "https://accounts.spotify.com/api/token"
BASIC_API_URL = "https://api.spotify.com"

api_client_id = os.environ['API_CLIENT_ID']
api_client_secret = os.environ['API_CLIENT_SECRET']

album_table_name = os.environ['ALBUM_TABLE_NAME']

dynamodb_resource = boto3.resource('dynamodb')
album_table = dynamodb_resource.Table(album_table_name)


def get_access_token_from_api():
    auth = 'Basic ' + base64.b64encode((api_client_id + ':' + api_client_secret).encode()).decode()
    response_token = requests.post(GET_TOKEN_URL, headers={'Authorization' : auth, 'Content-Type' : 'application/x-www-form-urlencoded'}, data = {'grant_type' : 'client_credentials'})
    return response_token.json()


def get_artist_id_from_api(credentials, artist_name):
    auth = 'Bearer ' + credentials['access_token']
    response_artist = requests.get(BASIC_API_URL + '/v1/search?q=' + artist_name + '&type=artist&market=DE&limit=1&offset=0', headers={'Authorization' : auth})
    return (response_artist.json())['artists']['items'][0]['id']


def get_album_data_from_api(credentials, artist_id):
    auth = 'Bearer ' + credentials['access_token']
    response_albums = requests.get(BASIC_API_URL + '/v1/artists/' + artist_id + '/albums?offset=0&limit=50&include_groups=album&market=DE', headers={'Authorization' : auth})
    return (response_albums.json())['items']


def map_album_data(album_api_data):
    albums_list = []
    today = datetime.now()
    for album in album_api_data:
        if not album['name'] in map(lambda a: a['album_name'], albums_list):
            albums_list.append({
                'artist_id' : album['artists'][0]['id'],
                'artist_name' : album['artists'][0]['name'],
                'album_name' : album['name'],
                'album_id' : album['id'],
                'release_date' : album['release_date'],
                'date' : today.strftime('%Y-%m-%d %H:%M:%S')
            })
    return albums_list


def save_album_data(mapped_album_data):
    for album in mapped_album_data:
        album_table.put_item(Item = album)


def handler(event, context):
    credentials = get_access_token_from_api()
    artist_id = get_artist_id_from_api(credentials, 'Billy Talent')
    album_api_data = get_album_data_from_api(credentials, artist_id)
    mapped_album_data = map_album_data(album_api_data)
    save_album_data(mapped_album_data)
    

if __name__ == "__main__":
    handler({}, {})