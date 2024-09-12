# file: lib/ansible/plugins/filter/urls.py:42-55
# asked: {"lines": [49, 50], "branches": []}
# gained: {"lines": [49, 50], "branches": []}

import pytest
from ansible.plugins.filter.urls import do_urlencode
from ansible.module_utils.six import iteritems, string_types

def test_do_urlencode_with_non_iterable():
    class NonIterable:
        def __str__(self):
            return "NonIterable"

    non_iterable = NonIterable()
    with pytest.raises(TypeError):
        do_urlencode(non_iterable)

def test_do_urlencode_with_iterable_but_not_dict_or_string():
    iterable = [('key1', 'value1'), ('key2', 'value2')]
    result = do_urlencode(iterable)
    assert result == 'key1=value1&key2=value2'

def test_do_urlencode_with_dict():
    dictionary = {'key1': 'value1', 'key2': 'value2'}
    result = do_urlencode(dictionary)
    assert result == 'key1=value1&key2=value2'

def test_do_urlencode_with_string():
    string = 'test_string'
    result = do_urlencode(string)
    assert result == 'test_string'
