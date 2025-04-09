# file: lib/ansible/plugins/filter/core.py:440-457
# asked: {"lines": [440, 441, 457], "branches": []}
# gained: {"lines": [440, 441, 457], "branches": []}

import pytest
from jinja2 import Environment
from ansible.plugins.filter.core import do_groupby

@pytest.fixture
def environment():
    return Environment()

def test_do_groupby_with_namedtuple(environment):
    from collections import namedtuple

    # Create a namedtuple class
    Item = namedtuple('Item', ['category', 'value'])
    
    # Create a list of namedtuple instances
    items = [
        Item(category='fruit', value='apple'),
        Item(category='fruit', value='banana'),
        Item(category='vegetable', value='carrot'),
        Item(category='vegetable', value='lettuce')
    ]
    
    # Group by 'category'
    result = do_groupby(environment, items, 'category')
    
    # Verify the result is a list of tuples
    assert isinstance(result, list)
    assert all(isinstance(group, tuple) for group in result)
    
    # Verify the content of the result
    expected = [
        ('fruit', [Item(category='fruit', value='apple'), Item(category='fruit', value='banana')]),
        ('vegetable', [Item(category='vegetable', value='carrot'), Item(category='vegetable', value='lettuce')])
    ]
    assert result == expected

def test_do_groupby_with_dict(environment):
    # Create a list of dictionaries
    items = [
        {'category': 'fruit', 'value': 'apple'},
        {'category': 'fruit', 'value': 'banana'},
        {'category': 'vegetable', 'value': 'carrot'},
        {'category': 'vegetable', 'value': 'lettuce'}
    ]
    
    # Group by 'category'
    result = do_groupby(environment, items, 'category')
    
    # Verify the result is a list of tuples
    assert isinstance(result, list)
    assert all(isinstance(group, tuple) for group in result)
    
    # Verify the content of the result
    expected = [
        ('fruit', [{'category': 'fruit', 'value': 'apple'}, {'category': 'fruit', 'value': 'banana'}]),
        ('vegetable', [{'category': 'vegetable', 'value': 'carrot'}, {'category': 'vegetable', 'value': 'lettuce'}])
    ]
    assert result == expected
