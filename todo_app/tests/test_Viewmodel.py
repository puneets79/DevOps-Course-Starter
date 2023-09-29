from todo_app.data import Item, ViewModel
def create_items():
    test_items = []
    myItem = Item.Item('1','Todo Item', 'To do','Test Todo Item')
    test_items.append(myItem)
    myItem = Item.Item('2','Doing Item', 'Doing','Test Doing Item')
    test_items.append(myItem)
    myItem = Item.Item('3','Done Item', 'Done','Test Done Item')
    test_items.append(myItem)
    myList = ViewModel.ViewModel(test_items)
    return myList

def test_get_todos():
    test_list = create_items()
    todos = test_list.todo_items

    assert len(todos) == 1
    assert todos[0].status == 'To do'

def test_get_doing():
    test_list = create_items()
    doing = test_list.doing_items

    assert len(doing) == 1
    assert doing[0].status == 'Doing'

def test_get_done():
    test_list = create_items()
    done = test_list.done_items

    assert len(done) == 1
    assert done[0].status == 'Done'
