import io
import requests

from urllib.parse import urljoin

from config import *


def get_data(suburl, result_type='text'):
    url = urljoin(SERVER_URL, suburl)
    response = requests.get(url)
    if response.status_code != 200:
        if result_type == 'text':
            return "Hey! We are down for a while :( Try again later ;)"
        else:
            return open("pics/500.png", "rb")

    if result_type == 'image':
        return io.BytesIO(response.content)

    return response.content

def get_prediction(labeled):
    url = "/labeled-picture" if labeled else "/picture"
    # file = open(name, 'rb')
    return {
        'picture': get_data(url, 'image'), 
        'message': get_data("/predict")
    }