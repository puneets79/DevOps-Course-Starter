import requests
import os
from todo_app.data import Item

def get_items():
    """
    Fetches all saved items from Trello.

    Returns:
        list: The list of Trello items.
    """
    key=str(os.getenv('API_KEY'))
    token=str(os.getenv('API_TOKEN'))
    board = os.getenv('BOARD_ID')
    url = f'https://api.trello.com/1/boards/{board}/lists?cards=open&key={key}&token={token}'
    
    
    response = requests.get(url=url)
    responseList = response.json()
    cards=[]
    for item in responseList:
      for card in item['cards']:
        myCard = Item.Item.from_trello_card(card,item)
        cards.append(myCard)
    
    return cards
def get_lists():
    """
    Fetches the the lists from Trello.

    Returns:
        list: The list of Trello Lists.
    """
    key=str(os.getenv('API_KEY'))
    token=str(os.getenv('API_TOKEN'))
    url = "https://api.trello.com/1/boards/"+os.getenv('BOARD_ID')+"/lists?key="+key+"&token="+token

    response = requests.get(url=url)
    responseList = response.json()
    return responseList

def get_item(id):
    """
    Fetch a single card from Trello

    Returns:
        Dictionary: The Trello card requested.
    """
    key=str(os.getenv('API_KEY'))
    token=str(os.getenv('API_TOKEN'))
    url = "https://api.trello.com/1/cards/"+id+"?key="+key+"&token="+token

    response = requests.get(url=url)
    card = response.json()
    return card

def save_item(item):
    """
    Updates a Trello card

   
    """
    url = "https://api.trello.com/1/cards/"+item['id']
    key=str(os.getenv('API_KEY'))
    token=str(os.getenv('API_TOKEN'))

    headers = {
      "Accept": "application/json"
    }

    query = {
      'key': key,
      'token': token,
      'name' : item['name'],
      'idList' : item['status'],
      'desc' : item['desc']
    }

    response = requests.request(
      "PUT",
      url,
      headers=headers,
      params=query
    )
    

def delete_item(id):
    """
    Deletes a Trello card

   
    """
    url = "https://api.trello.com/1/cards/"+id
    key=str(os.getenv('API_KEY'))
    token=str(os.getenv('API_TOKEN'))
    query = {
      'key': key,
      'token': token,
      }

    response = requests.request(
      "DELETE",
      url,
      params=query
    )
    print (response.text)

def add_item(item):
    """
    Adds a Trello card

   
    """
    url = "https://api.trello.com/1/cards"
    headers = {
      "Accept": "application/json"
    }
    key=str(os.getenv('API_KEY'))
    token=str(os.getenv('API_TOKEN'))
    query = {
      'key': key,
      'token': token,
      'name' : item['name'],
      'idList' : item['idList'],
      'desc' : item['desc']
      }

    response = requests.request(
      "POST",
      url,
      params=query
    )
    print (response.text)
