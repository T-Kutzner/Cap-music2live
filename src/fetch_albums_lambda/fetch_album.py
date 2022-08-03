import requests
import base64
import variables

GET_TOKEN_URL = "https://accounts.spotify.com/api/token"
BASIC_API_URL = "https://api.spotify.com"

client_id = variables.client_id
client_secret = variables.client_secret

def get_access_token_from_api():
    auth = 'Basic ' + base64.b64encode((client_id + ':' + client_secret).encode()).decode()
    response_token = requests.post(GET_TOKEN_URL, headers={'Authorization' : auth, 'Content-Type' : 'application/x-www-form-urlencoded'}, data = {'grant_type' : 'client_credentials'})
    return response_token.json()


def get_artist_id_from_api(credentials, artist_name):
    auth = 'Bearer ' + credentials['access_token']
    response_artist = requests.get(BASIC_API_URL + '/v1/search?q=' + artist_name + '&type=artist&market=DE&limit=1&offset=0', headers={'Authorization' : auth})
    id_of_artist = (response_artist.json())['artists']['items'][0]['id']
    return id_of_artist


def get_album_data_from_api(credentials, artist_id):
    auth = 'Bearer ' + credentials['access_token']
    response_albums = requests.get(BASIC_API_URL + '/v1/artists/' + artist_id + '/albums?offset=0&limit=50&include_groups=album&market=DE', headers={'Authorization' : auth})
    
    albums_list = []
    
    albums = (response_albums.json())['items']

    for album in albums:
        if not album['name'] in map(lambda a: a['album_name'], albums_list):
            albums_item = {
                'artist_name' : album['artists'][0]['name'],
                'artist_id' : album['artists'][0]['id'],
                'album_name' : album['name'],
                'album_id' : album['id'],
                'release_date' : album['release_date']
            }
            albums_list.append(albums_item)

    return albums_list


def handler(event, context):
    credentials = get_access_token_from_api()
    artist_id = get_artist_id_from_api(credentials, 'Billy Talent')

    print("Load album data")
    albums = get_album_data_from_api(credentials, artist_id)
    print(albums)
    album_api_data = get_album_data_from_api(credentials, artist_id)
    print(album_api_data)

    #print("Save data")
    

if __name__ == "__main__":
    handler({}, {})