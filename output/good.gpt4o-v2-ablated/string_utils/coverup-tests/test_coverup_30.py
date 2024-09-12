# file: string_utils/manipulation.py:529-558
# asked: {"lines": [551, 552, 554, 555, 556, 558], "branches": [[551, 552], [551, 554]]}
# gained: {"lines": [551, 552, 554, 555, 556, 558], "branches": [[551, 552], [551, 554]]}

import pytest
from string_utils.manipulation import strip_margin, InvalidInputError
import re

# Mocking the dependencies
MARGIN_RE = re.compile(r'^\s+')
def is_string(input_string):
    return isinstance(input_string, str)

def test_strip_margin_valid_input(monkeypatch):
    # Mocking the MARGIN_RE and is_string function
    monkeypatch.setattr('string_utils.manipulation.MARGIN_RE', MARGIN_RE)
    monkeypatch.setattr('string_utils.manipulation.is_string', is_string)
    
    input_string = '''
                line 1
                line 2
                line 3
                '''
    expected_output = '''
line 1
line 2
line 3
'''
    assert strip_margin(input_string) == expected_output

def test_strip_margin_invalid_input(monkeypatch):
    # Mocking the is_string function
    monkeypatch.setattr('string_utils.manipulation.is_string', lambda x: False)
    
    with pytest.raises(InvalidInputError):
        strip_margin(123)

def test_strip_margin_empty_string(monkeypatch):
    # Mocking the MARGIN_RE and is_string function
    monkeypatch.setattr('string_utils.manipulation.MARGIN_RE', MARGIN_RE)
    monkeypatch.setattr('string_utils.manipulation.is_string', is_string)
    
    input_string = ''
    expected_output = ''
    assert strip_margin(input_string) == expected_output
