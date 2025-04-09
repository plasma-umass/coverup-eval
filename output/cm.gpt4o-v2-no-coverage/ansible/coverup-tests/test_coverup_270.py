# file: lib/ansible/plugins/filter/core.py:424-437
# asked: {"lines": [424, 425, 426, 427, 428, 429, 431, 433, 434, 435, 437], "branches": [[426, 427], [426, 428], [428, 429], [428, 431], [434, 435], [434, 437]]}
# gained: {"lines": [424, 425, 426, 427, 428, 429, 431, 433, 434, 435, 437], "branches": [[426, 427], [426, 428], [428, 429], [428, 431], [434, 435], [434, 437]]}

import pytest
from jinja2 import Environment
from ansible.plugins.filter.core import extract

@pytest.fixture
def environment():
    return Environment()

def test_extract_no_morekeys(environment):
    container = {'a': 1}
    result = extract(environment, 'a', container)
    assert result == 1

def test_extract_morekeys_as_list(environment):
    container = {'a': {'b': 2}}
    result = extract(environment, 'a', container, ['b'])
    assert result == 2

def test_extract_morekeys_as_single_key(environment):
    container = {'a': {'b': 2}}
    result = extract(environment, 'a', container, 'b')
    assert result == 2

def test_extract_key_not_found(environment, monkeypatch):
    container = {'a': 1}
    
    def mock_getitem(value, key):
        raise KeyError(key)
    
    monkeypatch.setattr(environment, 'getitem', mock_getitem)
    
    with pytest.raises(KeyError):
        extract(environment, 'b', container)

def test_extract_with_multiple_keys(environment):
    container = {'a': {'b': {'c': 3}}}
    result = extract(environment, 'a', container, ['b', 'c'])
    assert result == 3
