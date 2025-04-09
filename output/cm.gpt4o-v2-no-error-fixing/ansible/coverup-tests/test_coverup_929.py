# file: lib/ansible/plugins/filter/urls.py:26-27
# asked: {"lines": [27], "branches": []}
# gained: {"lines": [27], "branches": []}

import pytest
from ansible.plugins.filter.urls import do_urldecode

def test_do_urldecode_py3(monkeypatch):
    # Mock PY3 to be True
    monkeypatch.setattr("ansible.module_utils.six.PY3", True)
    
    # Test data
    encoded_string = "hello%20world"
    expected_result = "hello world"
    
    # Call the function
    result = do_urldecode(encoded_string)
    
    # Assert the result
    assert result == expected_result

def test_do_urldecode_py2(monkeypatch):
    # Mock PY3 to be False
    monkeypatch.setattr("ansible.module_utils.six.PY3", False)
    
    # Test data
    encoded_string = "hello%20world"
    expected_result = "hello world"
    
    # Call the function
    result = do_urldecode(encoded_string)
    
    # Assert the result
    assert result == expected_result
