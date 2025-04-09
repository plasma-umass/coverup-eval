# file: lib/ansible/plugins/filter/urls.py:42-55
# asked: {"lines": [49, 50], "branches": []}
# gained: {"lines": [49, 50], "branches": []}

import pytest
from ansible.plugins.filter.urls import do_urlencode

def test_do_urlencode_with_non_iterable(monkeypatch):
    class NonIterable:
        pass

    non_iterable_instance = NonIterable()
    
    def mock_unicode_urlencode(value, for_qs=False):
        return str(value)
    
    monkeypatch.setattr('ansible.plugins.filter.urls.unicode_urlencode', mock_unicode_urlencode)
    
    result = do_urlencode(non_iterable_instance)
    assert result == str(non_iterable_instance)

def test_do_urlencode_with_iterable(monkeypatch):
    iterable_instance = [('key1', 'value1'), ('key2', 'value2')]
    
    def mock_unicode_urlencode(value, for_qs=False):
        return str(value)
    
    monkeypatch.setattr('ansible.plugins.filter.urls.unicode_urlencode', mock_unicode_urlencode)
    
    result = do_urlencode(iterable_instance)
    expected_result = 'key1=value1&key2=value2'
    assert result == expected_result
