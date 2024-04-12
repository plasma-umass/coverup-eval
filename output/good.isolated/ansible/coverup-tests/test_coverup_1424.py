# file lib/ansible/plugins/filter/urls.py:20-23
# lines [23]
# branches ['21->23']

import pytest
from ansible.plugins.filter.urls import unicode_urldecode

# Assuming the existence of a PY3 constant in the module, we need to mock it
# to ensure that the test covers the Python 2 code path.

def test_unicode_urldecode_py2(mocker):
    # Mock the PY3 constant to be False to simulate Python 2 environment
    mocker.patch('ansible.plugins.filter.urls.PY3', False)
    
    # Mock the to_text and to_bytes functions to simply return the input value
    # for the purpose of this test.
    mocker.patch('ansible.plugins.filter.urls.to_text', side_effect=lambda x: x)
    mocker.patch('ansible.plugins.filter.urls.to_bytes', side_effect=lambda x: x)
    
    # Input string that needs to be url-decoded
    input_string = 'hello%20world%21'
    expected_output = 'hello world!'
    
    # Call the function and assert the expected output
    output = unicode_urldecode(input_string)
    assert output == expected_output
