# file: string_utils/manipulation.py:529-558
# asked: {"lines": [529, 551, 552, 554, 555, 556, 558], "branches": [[551, 552], [551, 554]]}
# gained: {"lines": [529, 551, 552, 554, 555, 556, 558], "branches": [[551, 552], [551, 554]]}

import pytest
from string_utils.manipulation import strip_margin
from string_utils.errors import InvalidInputError
from string_utils.validation import is_string
import re

# Mocking MARGIN_RE for the purpose of testing
MARGIN_RE = re.compile(r'^\s*')

def test_strip_margin_valid_string(monkeypatch):
    test_input = '''
                line 1
                line 2
                line 3
                '''
    expected_output = '''
line 1
line 2
line 3
'''

    # Mocking is_string to always return True
    monkeypatch.setattr('string_utils.validation.is_string', lambda x: True)
    monkeypatch.setattr('string_utils.manipulation.MARGIN_RE', MARGIN_RE)

    result = strip_margin(test_input)
    assert result == expected_output

def test_strip_margin_invalid_input(monkeypatch):
    test_input = 12345  # Not a string

    # Mocking is_string to always return False
    monkeypatch.setattr('string_utils.validation.is_string', lambda x: False)

    with pytest.raises(InvalidInputError) as exc_info:
        strip_margin(test_input)
    
    assert str(exc_info.value) == 'Expected "str", received "int"'

def test_strip_margin_empty_string(monkeypatch):
    test_input = ''
    expected_output = ''

    # Mocking is_string to always return True
    monkeypatch.setattr('string_utils.validation.is_string', lambda x: True)
    monkeypatch.setattr('string_utils.manipulation.MARGIN_RE', MARGIN_RE)

    result = strip_margin(test_input)
    assert result == expected_output
