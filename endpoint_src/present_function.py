import boto3

dynamoDB_table_name = "albums"
dynamoDB = boto3.resource("dynamodb")
dynamoDB_table = dynamoDB.Table(dynamoDB_table_name)


def get_album_data():
    response_album_data = dynamoDB_table.scan()
    album_items = response_album_data["Items"]#items or Items?
    items_list = []
    for item in album_items:
        items_list.append(item)
    return items_list

def map_data(items_list):
    items = []
    for item in items_list:
        item_tuple = (item['artist_id'], item['artist_name'], item['album_name'], item['album_id'], item['release_date'], item['date'])
        items.append(item_tuple)
    return items

def present_album_data():
    items_list = get_album_data()
    return map_data(items_list)


def main_function():
    items_list = get_album_data()
    map_data(items_list)
    print(present_album_data())