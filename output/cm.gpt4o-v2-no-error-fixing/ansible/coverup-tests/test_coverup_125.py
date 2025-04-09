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

def test_extract_morekeys_none(environment):
    container = {'a': {'b': 2}}
    result = extract(environment, 'a', container, morekeys=None)
    assert result == {'b': 2}

def test_extract_morekeys_list(environment):
    container = {'a': {'b': {'c': 3}}}
    result = extract(environment, 'a', container, morekeys=['b', 'c'])
    assert result == 3

def test_extract_morekeys_single(environment):
    container = {'a': {'b': 2}}
    result = extract(environment, 'a', container, morekeys='b')
    assert result == 2
