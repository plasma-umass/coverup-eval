# file lib/ansible/plugins/filter/core.py:440-457
# lines [440, 441, 457]
# branches []

import pytest
from unittest.mock import patch
from jinja2 import Environment

# Assuming the function is imported from the module
from ansible.plugins.filter.core import do_groupby

@pytest.fixture
def mock_environment():
    return Environment()

def test_do_groupby(mock_environment):
    value = [
        {'name': 'apple', 'type': 'fruit'},
        {'name': 'carrot', 'type': 'vegetable'},
        {'name': 'banana', 'type': 'fruit'},
    ]
    attribute = 'type'

    with patch('ansible.plugins.filter.core._do_groupby') as mock_do_groupby:
        mock_do_groupby.return_value = [
            ('fruit', [{'name': 'apple', 'type': 'fruit'}, {'name': 'banana', 'type': 'fruit'}]),
            ('vegetable', [{'name': 'carrot', 'type': 'vegetable'}])
        ]

        result = do_groupby(mock_environment, value, attribute)

        assert result == [
            ('fruit', [{'name': 'apple', 'type': 'fruit'}, {'name': 'banana', 'type': 'fruit'}]),
            ('vegetable', [{'name': 'carrot', 'type': 'vegetable'}])
        ]

        mock_do_groupby.assert_called_once_with(mock_environment, value, attribute)
