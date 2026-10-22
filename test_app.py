import pytest
from app import app

@pytest.fixture

def client():
    """Sets up test client for flask"""
    app.config['Test'] = True
    with app.test_client() as client:
        yield client

def test_home_page(client):
    """Test that the flask home page can be accessed"""
    response = client.get('/')
    assert response.status_code == 200

def test_missing_file(client):
    """ Test that request missing upload file"""
    response = client.post('/prediction', data ={} )
    assert response.status_code in [200,400]

def test_valid_request(client):
    """Test valid request"""
    img_path = "test_images/2/Sign 2 (97).jpeg"

    with open(img_path, 'rb') as img:
        data = {
            'file':(img,'test_image.jpeg')
        }
        response = client.post('/prediction', data = data, content_type = "multipart/form-data")

    assert response.status_code == 200