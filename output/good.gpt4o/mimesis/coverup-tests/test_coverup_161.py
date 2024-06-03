# file mimesis/providers/choice.py:12-14
# lines [12, 13]
# branches []

import pytest
from mimesis.providers.choice import Choice

def test_choice_provider():
    choice_provider = Choice()
    
    # Test if the choice provider can select an item from a list
    items = [1, 2, 3, 4, 5]
    selected_item = choice_provider(items)
    assert selected_item in items

    # Test if the choice provider can handle an empty list
    empty_items = []
    with pytest.raises(ValueError):
        choice_provider(empty_items)

    # Test if the choice provider can select an item from a tuple
    items_tuple = (1, 2, 3, 4, 5)
    selected_item = choice_provider(items_tuple)
    assert selected_item in items_tuple

    # Test if the choice provider can select an item from a string
    items_string = "abcde"
    selected_item = choice_provider(items_string)
    assert selected_item in items_string

    # Test if the choice provider can handle a set
    items_set = {1, 2, 3, 4, 5}
    with pytest.raises(TypeError):
        choice_provider(items_set)

    # Test if the choice provider can handle a dictionary (keys)
    items_dict = {1: 'a', 2: 'b', 3: 'c'}
    selected_item = choice_provider(list(items_dict.keys()))
    assert selected_item in items_dict

    # Test if the choice provider can handle a dictionary (values)
    selected_item = choice_provider(list(items_dict.values()))
    assert selected_item in items_dict.values()
