# file lib/ansible/plugins/filter/core.py:127-137
# lines [130, 132, 133, 134, 135, 136, 137]
# branches ['133->134', '133->135', '135->136', '135->137']

import pytest
import re
from ansible.plugins.filter.core import regex_findall
from ansible.module_utils._text import to_text

def test_regex_findall(mocker):
    # Mock the to_text function to ensure it is called with the correct parameters
    mock_to_text = mocker.patch('ansible.plugins.filter.core.to_text', wraps=to_text)
    
    value = b"Hello\nWorld"
    regex = r"\w+"
    multiline = True
    ignorecase = True
    
    result = regex_findall(value, regex, multiline=multiline, ignorecase=ignorecase)
    
    # Verify that to_text was called with the correct parameters
    mock_to_text.assert_called_once_with(value, errors='surrogate_or_strict', nonstring='simplerepr')
    
    # Verify the result of the regex_findall function
    assert result == ['Hello', 'World']

    # Test with different flags
    result = regex_findall(value, regex, multiline=False, ignorecase=True)
    assert result == ['Hello', 'World']

    result = regex_findall(value, regex, multiline=True, ignorecase=False)
    assert result == ['Hello', 'World']

    result = regex_findall(value, regex, multiline=False, ignorecase=False)
    assert result == ['Hello', 'World']
