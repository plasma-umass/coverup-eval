# file: lib/ansible/plugins/filter/urls.py:31-39
# asked: {"lines": [31, 32, 33, 34, 36, 37, 38, 39], "branches": [[33, 34], [33, 36], [37, 38], [37, 39]]}
# gained: {"lines": [31, 32, 33, 34, 36, 37, 38, 39], "branches": [[33, 34], [33, 36], [37, 38], [37, 39]]}

import pytest
from ansible.plugins.filter.urls import unicode_urlencode
from ansible.module_utils.six import PY3
from urllib.parse import quote, quote_plus

def test_unicode_urlencode_for_qs(monkeypatch):
    # Test with for_qs=True
    test_string = "test string"
    expected_output = quote_plus(test_string)
    assert unicode_urlencode(test_string, for_qs=True) == expected_output

def test_unicode_urlencode_not_for_qs(monkeypatch):
    # Test with for_qs=False
    test_string = "test/string"
    expected_output = quote(test_string, safe='/')
    assert unicode_urlencode(test_string, for_qs=False) == expected_output

def test_unicode_urlencode_py2(monkeypatch):
    # Test for Python 2 behavior
    test_string = "test string"
    expected_output = quote_plus(test_string)
    
    def mock_to_text(value):
        return value
    
    def mock_to_bytes(value):
        return value.encode('utf-8')
    
    monkeypatch.setattr('ansible.plugins.filter.urls.to_text', mock_to_text)
    monkeypatch.setattr('ansible.plugins.filter.urls.to_bytes', mock_to_bytes)
    monkeypatch.setattr('ansible.plugins.filter.urls.PY3', False)
    
    assert unicode_urlencode(test_string, for_qs=True) == expected_output

def test_unicode_urlencode_py3(monkeypatch):
    # Test for Python 3 behavior
    test_string = "test string"
    expected_output = quote_plus(test_string)
    
    monkeypatch.setattr('ansible.plugins.filter.urls.PY3', True)
    
    assert unicode_urlencode(test_string, for_qs=True) == expected_output
