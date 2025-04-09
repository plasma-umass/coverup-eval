# file: lib/ansible/plugins/filter/core.py:440-457
# asked: {"lines": [440, 441, 457], "branches": []}
# gained: {"lines": [440, 441, 457], "branches": []}

import pytest
from jinja2 import Environment
from ansible.plugins.filter.core import do_groupby

@pytest.fixture
def environment():
    return Environment()

def test_do_groupby(environment):
    value = [
        {'name': 'apple', 'type': 'fruit'},
        {'name': 'carrot', 'type': 'vegetable'},
        {'name': 'banana', 'type': 'fruit'},
        {'name': 'lettuce', 'type': 'vegetable'}
    ]
    attribute = 'type'
    
    result = do_groupby(environment, value, attribute)
    
    expected = [
        ('fruit', [{'name': 'apple', 'type': 'fruit'}, {'name': 'banana', 'type': 'fruit'}]),
        ('vegetable', [{'name': 'carrot', 'type': 'vegetable'}, {'name': 'lettuce', 'type': 'vegetable'}])
    ]
    
    assert result == expected
