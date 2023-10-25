import os
from dotenv import load_dotenv, find_dotenv
from flask.testing import FlaskClient
import pytest
import requests
from todo_app import app

@pytest.fixture
def client():
    # Use our test integration config instead of the 'real' version
    file_path = find_dotenv('.env.test')
    load_dotenv(file_path, override=True)

    # Create the new app.
    test_app = app.create_app()

    # Use the app to create a test_client that can be used in our tests.
    with test_app.test_client() as client:
        yield client

class StubResponse():
    def __init__(self, fake_response_data):
        self.fake_response_data = fake_response_data

    def json(self):
        return self.fake_response_data

def stub(url, params={}):
    test_board_id = os.environ.get('BOARD_ID')
    key = os.environ.get('API_KEY')
    token = os.environ.get('API_TOKEN')
    trello_url = f'https://api.trello.com/1/boards/{test_board_id}/lists?cards=open&key={key}&token={token}'
    if url == trello_url:
        fake_response_data = [{
            'id': '123abc',
            'name': 'To do',
            'cards': [{'id': '456', 'name': 'Test card', 'desc': 'Test Card'}]
        }]
        return StubResponse(fake_response_data)

    raise Exception(f'Integration test did not expect URL "{url} but {trello_url}"')

def test_index_page(monkeypatch: pytest.MonkeyPatch, client: FlaskClient):
    # This replaces any call to requests.get with our own function
    monkeypatch.setattr(requests, 'get', stub)

    response = client.get('/')
    print (response.data.decode())
    assert response.status_code == 200
    assert 'Test card' in response.data.decode()

