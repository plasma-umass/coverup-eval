# file lib/ansible/plugins/filter/urls.py:31-39
# lines [39]
# branches ['37->39']

import pytest
from unittest.mock import patch
from ansible.plugins.filter.urls import unicode_urlencode

def test_unicode_urlencode_py2(mocker):
    # Mocking PY3 to be False to simulate Python 2 environment
    mocker.patch('ansible.plugins.filter.urls.PY3', False)
    mocker.patch('ansible.plugins.filter.urls.to_bytes', side_effect=lambda x: x.encode('utf-8'))
    mocker.patch('ansible.plugins.filter.urls.to_text', side_effect=lambda x: x)
    
    # Test data
    test_string = 'test string'
    expected_output = 'test%20string'
    
    # Run the function
    result = unicode_urlencode(test_string)
    
    # Assertions
    assert result == expected_output
