# file: lib/ansible/module_utils/urls.py:658-670
# asked: {"lines": [658, 659, 662, 663, 664, 666, 670], "branches": []}
# gained: {"lines": [658, 659, 662, 663, 664, 666, 670], "branches": []}

import pytest
from ansible.module_utils.urls import ParseResultDottedDict

def test_ParseResultDottedDict_init():
    data = {'scheme': 'http', 'netloc': 'example.com', 'path': '/index.html'}
    prdd = ParseResultDottedDict(data)
    assert prdd.scheme == 'http'
    assert prdd.netloc == 'example.com'
    assert prdd.path == '/index.html'

def test_ParseResultDottedDict_as_list():
    data = {'scheme': 'http', 'netloc': 'example.com', 'path': '/index.html', 'params': '', 'query': 'id=1', 'fragment': 'section'}
    prdd = ParseResultDottedDict(data)
    result_list = prdd.as_list()
    expected_list = ['http', 'example.com', '/index.html', '', 'id=1', 'section']
    assert result_list == expected_list
