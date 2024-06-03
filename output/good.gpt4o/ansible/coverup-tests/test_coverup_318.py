# file lib/ansible/plugins/filter/core.py:113-124
# lines [113, 116, 118, 119, 120, 121, 122, 123, 124]
# branches ['119->120', '119->121', '121->122', '121->123']

import pytest
import re
from ansible.plugins.filter.core import regex_replace

def test_regex_replace(mocker):
    # Mock the to_text function to ensure it returns the value as a string
    mocker.patch('ansible.plugins.filter.core.to_text', side_effect=lambda x, errors, nonstring: str(x))

    # Test case 1: Basic replacement
    result = regex_replace('Hello World', 'World', 'Universe')
    assert result == 'Hello Universe'

    # Test case 2: Ignore case
    result = regex_replace('Hello world', 'WORLD', 'Universe', ignorecase=True)
    assert result == 'Hello Universe'

    # Test case 3: Multiline replacement
    result = regex_replace('Hello\nWorld', '^World', 'Universe', multiline=True)
    assert result == 'Hello\nUniverse'

    # Test case 4: No match
    result = regex_replace('Hello World', 'Python', 'Universe')
    assert result == 'Hello World'

    # Test case 5: Empty pattern
    result = regex_replace('Hello World', '', 'Universe')
    assert result == 'UniverseHUniverseeUniverselUniverselUniverseoUniverse UniverseWUniverseoUniverserUniverselUniversedUniverse'

    # Test case 6: Empty replacement
    result = regex_replace('Hello World', 'World', '')
    assert result == 'Hello '

    # Test case 7: Non-string input
    result = regex_replace(12345, '2', '9')
    assert result == '19345'
