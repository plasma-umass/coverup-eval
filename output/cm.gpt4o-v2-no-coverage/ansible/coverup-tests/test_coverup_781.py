# file: lib/ansible/plugins/filter/core.py:440-457
# asked: {"lines": [440, 441, 457], "branches": []}
# gained: {"lines": [440, 441, 457], "branches": []}

import pytest
from jinja2 import Environment
from jinja2.filters import do_groupby as _do_groupby
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
    
    # Expected result using the original _do_groupby function
    expected = [tuple(t) for t in _do_groupby(environment, value, attribute)]
    
    # Actual result using the overridden do_groupby function
    result = do_groupby(environment, value, attribute)
    
    assert result == expected
    assert all(isinstance(item, tuple) for item in result)
