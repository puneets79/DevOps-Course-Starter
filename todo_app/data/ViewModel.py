
class ViewModel:
    def __init__(self, list_items):
        self._items = list_items
 
    @property
    def items(self):
        return self._items
    
    @property
    def todo_items(self):
        returned_items = []
        for item in self._items:
            if item.status == "To do":
                returned_items.append(item)
        
        return returned_items
    
    @property
    def doing_items(self):
        returned_items = []
        for item in self._items:
            if item.status == "Doing":
                returned_items.append(item)
        
        return returned_items   
    
    @property
    def done_items(self):
        returned_items = []
        for item in self._items:
            if item.status =="Done":
                returned_items.append(item)
        
        return returned_items   
    
