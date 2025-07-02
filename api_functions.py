import requests
from config import BASE_URL

def create_order(order_data):
    response = requests.post(
        f"{BASE_URL}/api/v1/orders",
        json=order_data
    )
    response.raise_for_status()
    return response

def get_order_by_track(track):
    response = requests.get(
        f"{BASE_URL}/api/v1/orders/track",
        params={"t": track}
    )
    response.raise_for_status()
    return response