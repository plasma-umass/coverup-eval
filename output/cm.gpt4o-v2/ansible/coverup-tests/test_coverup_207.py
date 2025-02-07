# file: lib/ansible/plugins/filter/core.py:424-437
# asked: {"lines": [424, 425, 426, 427, 428, 429, 431, 433, 434, 435, 437], "branches": [[426, 427], [426, 428], [428, 429], [428, 431], [434, 435], [434, 437]]}
# gained: {"lines": [424, 425, 426, 427, 428, 429, 431, 433, 434, 435, 437], "branches": [[426, 427], [426, 428], [428, 429], [428, 431], [434, 435], [434, 437]]}

import pytest
from jinja2 import Environment, Undefined
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
    container = {'a': {'b': 3}}
    result = extract(environment, 'a', container, 'b')
    assert result == 3

def test_extract_key_not_found(environment):
    container = {'a': {'b': 4}}
    result = extract(environment, 'a', container, 'c')
    assert isinstance(result, Undefined)
