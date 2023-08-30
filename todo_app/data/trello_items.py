import requests
import os

def get_items():
    """
    Fetches all saved items from Trello.

    Returns:
        list: The list of Trello items.
    """
    key=str(os.getenv('API_KEY'))
    token=str(os.getenv('API_TOKEN'))
    url = "https://api.trello.com/1/boards/64e9f4bb863cb6be33f77851/lists?cards=open&key="+key+"&token="+token

    response = requests.get(url=url)
    responseList = response.json()
    cards=[]
    for item in responseList:
      for card in item['cards']:
        card['listname']=item['name']
        cards.append(card)
    
    return cards
def get_lists():
    """
    Fetches the the lists from Trello.

    Returns:
        list: The list of Trello Lists.
    """
    key=str(os.getenv('API_KEY'))
    token=str(os.getenv('API_TOKEN'))
    url = "https://api.trello.com/1/boards/64e9f4bb863cb6be33f77851/lists?key="+key+"&token="+token

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
      'idList' : item['status']
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
      'idList' : item['idList']
      }

    response = requests.request(
      "POST",
      url,
      params=query
    )
    print (response.text)
