import requests #digunakan untuk mengirim request html

base_url = 'https://api.coincap.io/v2/'
base_payload = {}
base_headers = {}


def get_assets() -> str:
    """
    Returns a list of all assets
    TODO: add optional params
    """
    method = 'assets'
    url = base_url + method
    response = requests.get(url)
    print(type(response))
    return response.json()

