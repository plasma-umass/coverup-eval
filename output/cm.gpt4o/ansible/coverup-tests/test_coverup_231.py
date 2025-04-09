# file lib/ansible/plugins/filter/core.py:424-437
# lines [424, 425, 426, 427, 428, 429, 431, 433, 434, 435, 437]
# branches ['426->427', '426->428', '428->429', '428->431', '434->435', '434->437']

import pytest
from unittest.mock import Mock
from ansible.plugins.filter.core import extract

@pytest.fixture
def mock_environment():
    return Mock()

def test_extract_with_no_morekeys(mock_environment):
    mock_environment.getitem.side_effect = lambda container, key: container[key]
    container = {'a': 1}
    result = extract(mock_environment, 'a', container)
    assert result == 1

def test_extract_with_morekeys_list(mock_environment):
    mock_environment.getitem.side_effect = lambda container, key: container[key]
    container = {'a': {'b': 2}}
    result = extract(mock_environment, 'a', container, ['b'])
    assert result == 2

def test_extract_with_morekeys_single(mock_environment):
    mock_environment.getitem.side_effect = lambda container, key: container[key]
    container = {'a': {'b': 2}}
    result = extract(mock_environment, 'a', container, 'b')
    assert result == 2
