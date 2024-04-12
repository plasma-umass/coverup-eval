# file lib/ansible/plugins/filter/core.py:424-437
# lines [424, 425, 426, 427, 428, 429, 431, 433, 434, 435, 437]
# branches ['426->427', '426->428', '428->429', '428->431', '434->435', '434->437']

import pytest
from jinja2.runtime import Context
from ansible.plugins.filter.core import extract

class MockEnvironment:
    def getitem(self, obj, attribute):
        return obj.get(attribute)

@pytest.fixture
def mock_environment(mocker):
    env = MockEnvironment()
    mocker.patch('ansible.plugins.filter.core.environmentfilter', lambda x: x)
    return env

def test_extract_with_morekeys_as_list(mock_environment):
    container = {'a': {'b': {'c': 'value'}}}
    morekeys = ['b', 'c']
    result = extract(mock_environment, 'a', container, morekeys)
    assert result == 'value'

def test_extract_with_morekeys_as_non_list(mock_environment):
    container = {'a': {'b': 'value'}}
    morekeys = 'b'
    result = extract(mock_environment, 'a', container, morekeys)
    assert result == 'value'

def test_extract_with_morekeys_as_none(mock_environment):
    container = {'a': 'value'}
    result = extract(mock_environment, 'a', container)
    assert result == 'value'
