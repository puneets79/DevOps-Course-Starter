class Item:
    def __init__(self, id, name, status,desc):
        self.id = id
        self.name = name
        self.status = status
        self.desc = desc

    @classmethod
    def from_trello_card(cls, card, list):
        return cls(card['id'], card['name'], list['name'],card['desc'])