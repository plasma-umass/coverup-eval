# file: lib/ansible/module_utils/urls.py:658-670
# asked: {"lines": [658, 659, 662, 663, 664, 666, 670], "branches": []}
# gained: {"lines": [658, 659, 662, 663, 664, 666, 670], "branches": []}

import pytest
from ansible.module_utils.urls import ParseResultDottedDict

def test_parse_result_dotted_dict_init():
    data = {'scheme': 'http', 'netloc': 'example.com', 'path': '/index.html'}
    prdd = ParseResultDottedDict(data)
    assert prdd['scheme'] == 'http'
    assert prdd['netloc'] == 'example.com'
    assert prdd['path'] == '/index.html'
    assert prdd.__dict__ == prdd

def test_parse_result_dotted_dict_as_list():
    data = {'scheme': 'http', 'netloc': 'example.com', 'path': '/index.html', 'params': '', 'query': 'a=1', 'fragment': 'section1'}
    prdd = ParseResultDottedDict(data)
    result_list = prdd.as_list()
    expected_list = ['http', 'example.com', '/index.html', '', 'a=1', 'section1']
    assert result_list == expected_list

def test_parse_result_dotted_dict_as_list_missing_keys():
    data = {'scheme': 'http', 'netloc': 'example.com'}
    prdd = ParseResultDottedDict(data)
    result_list = prdd.as_list()
    expected_list = ['http', 'example.com', None, None, None, None]
    assert result_list == expected_list
