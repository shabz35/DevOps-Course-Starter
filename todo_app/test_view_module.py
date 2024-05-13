from todo_app.data import item
from todo_app.data.view_model import ViewModel


def test_done_items_property_only_shows_done_items_and_nothing_else():
    #ARRANGE
    items = [
        item.Item(1, "Started Todo", "To Do"),
        item.Item(2, "In Progress Todo", "Doing"),
        item.Item(3, "Finish Todo", "Done")

    ]

    view_model = ViewModel(items)
    

    #ACT
    returned_items = view_model.done_items


    #ASSERT
    assert len(returned_items) ==1
    returned_single_item = returned_items[0]
    assert returned_single_item.status == "Done"

def test_doing_items_property_only_shows_doing_items_and_nothing_else():
    #ARRANGE
    items = [
        item.Item(1, "Started Todo", "To Do"),
        item.Item(2, "In Progress Todo", "Doing"),
        item.Item(3, "Finish Todo", "Done")

    ]

    view_model = ViewModel(items)
    

    #ACT
    returned_items = view_model.doing_items


    #ASSERT
    assert len(returned_items) == 1
    returned_single_item = returned_items[0]
    assert returned_single_item.status == "Doing"

def test_todo_items_property_only_shows_todo_items_and_nothing_else():
    #ARRANGE
    items = [
        item.Item(1, "Started Todo", "To Do"),
        item.Item(2, "In Progress Todo", "Doing"),
        item.Item(3, "Finish Todo", "Done")

    ]

    view_model = ViewModel(items)
    

    #ACT
    returned_items = view_model.todo_items


    #ASSERT
    assert len(returned_items) == 1
    returned_single_item = returned_items[0]
    assert returned_single_item.status == "To Do"