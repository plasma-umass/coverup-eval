# file lib/ansible/plugins/filter/core.py:127-137
# lines [127, 130, 132, 133, 134, 135, 136, 137]
# branches ['133->134', '133->135', '135->136', '135->137']

import pytest
import re
from ansible.plugins.filter.core import regex_findall

def test_regex_findall_multiline_ignorecase(mocker):
    # Mock the to_text function to return the value as is
    mocker.patch('ansible.plugins.filter.core.to_text', side_effect=lambda x, **kwargs: x)

    # Test with multiline and ignorecase set to True
    result = regex_findall('Test String\nAnother Line', 'line$', multiline=True, ignorecase=True)
    assert result == ['Line'], "Expected to find 'Line' at the end of the second line with multiline and ignorecase flags"

    # Test with multiline set to False and ignorecase set to True
    result = regex_findall('Test String\nAnother Line', 'line$', multiline=False, ignorecase=True)
    assert result == ['Line'], "Expected to find 'Line' at the end of the string with ignorecase flag"

    # Test with multiline set to True and ignorecase set to False
    result = regex_findall('Test String\nAnother Line', 'line$', multiline=True, ignorecase=False)
    assert result == [], "Expected to find no matches without ignorecase flag"

    # Test with multiline and ignorecase set to False
    result = regex_findall('Test String\nAnother Line', 'line$', multiline=False, ignorecase=False)
    assert result == [], "Expected to find no matches without any flags"

    # Cleanup is handled by pytest-mock through the mocker fixture
