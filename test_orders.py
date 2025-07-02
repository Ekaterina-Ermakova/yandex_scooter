import pytest
from api_functions import create_order, get_order_by_track
from test_data import ORDER_PAYLOAD

def test_order_creation():
    response = create_order(ORDER_PAYLOAD)
    
    assert response.status_code == 201
    assert "track" in response.json()
    assert isinstance(response.json()["track"], int)

def test_get_order_by_track():
    create_response = create_order(ORDER_PAYLOAD)
    track = create_response.json()["track"]
    
    response = get_order_by_track(track)
    
    assert response.status_code == 200
    order_data = response.json()
    assert "order" in order_data
    assert order_data["order"]["track"] == track
    
    #Ермакова Екатерина Сергеевна, 31А когорта, Финальный проект. Инженер по тестированию расширенный