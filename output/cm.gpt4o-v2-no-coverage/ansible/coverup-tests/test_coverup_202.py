# file: lib/ansible/plugins/filter/urls.py:42-55
# asked: {"lines": [42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55], "branches": [[44, 45], [44, 46], [46, 47], [46, 51], [51, 52], [51, 53]]}
# gained: {"lines": [42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55], "branches": [[44, 45], [44, 46], [46, 47], [46, 51], [51, 52], [51, 53]]}

import pytest
from ansible.plugins.filter.urls import do_urlencode
from ansible.module_utils.six import iteritems, string_types

def test_do_urlencode_dict(monkeypatch):
    def mock_unicode_urlencode(value, for_qs=False):
        return str(value)
    
    monkeypatch.setattr('ansible.plugins.filter.urls.unicode_urlencode', mock_unicode_urlencode)
    
    value = {'key1': 'value1', 'key2': 'value2'}
    result = do_urlencode(value)
    assert result == 'key1=value1&key2=value2'

def test_do_urlencode_string(monkeypatch):
    def mock_unicode_urlencode(value, for_qs=False):
        return str(value)
    
    monkeypatch.setattr('ansible.plugins.filter.urls.unicode_urlencode', mock_unicode_urlencode)
    
    value = 'test_string'
    result = do_urlencode(value)
    assert result == 'test_string'

def test_do_urlencode_iterable(monkeypatch):
    def mock_unicode_urlencode(value, for_qs=False):
        return str(value)
    
    monkeypatch.setattr('ansible.plugins.filter.urls.unicode_urlencode', mock_unicode_urlencode)
    
    value = [('key1', 'value1'), ('key2', 'value2')]
    result = do_urlencode(value)
    assert result == 'key1=value1&key2=value2'

def test_do_urlencode_non_iterable(monkeypatch):
    def mock_unicode_urlencode(value, for_qs=False):
        return str(value)
    
    monkeypatch.setattr('ansible.plugins.filter.urls.unicode_urlencode', mock_unicode_urlencode)
    
    value = 12345
    result = do_urlencode(value)
    assert result == '12345'
