import boto3

DB_TABLE_NAME = "albums"

dynamoDB = boto3.resource("dynamodb")
dynamoDB_table = dynamoDB.Table(DB_TABLE_NAME)


def fetch_album_data():
    response_album_data = dynamoDB_table.scan()
    album_data = response_album_data["Items"]
    albums_list = []

    for album in album_data:
        albums_list.append(album)
    return albums_list


def map_album_data(albums_list):
    mapped_albums = []
    for album in albums_list:
        album_tuple = (album['artist_name'], album['album_name'], album['release_date'])
        mapped_albums.append(album_tuple)
    return mapped_albums


def main_function():
    albums_list = fetch_album_data()
    return map_album_data(albums_list)