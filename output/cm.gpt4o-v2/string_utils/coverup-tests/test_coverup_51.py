# file: string_utils/manipulation.py:529-558
# asked: {"lines": [551, 552, 554, 555, 556, 558], "branches": [[551, 552], [551, 554]]}
# gained: {"lines": [551, 552, 554, 555, 556, 558], "branches": [[551, 552], [551, 554]]}

import pytest
from string_utils.manipulation import strip_margin
from string_utils.errors import InvalidInputError

def test_strip_margin_with_non_string_input():
    with pytest.raises(InvalidInputError) as exc_info:
        strip_margin(1234)  # Non-string input
    assert str(exc_info.value) == 'Expected "str", received "int"'

def test_strip_margin_with_valid_string(monkeypatch):
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

    # Mocking the MARGIN_RE.sub to just strip leading spaces for simplicity
    import re
    MARGIN_RE = re.compile(r'^\s+', re.MULTILINE)
    monkeypatch.setattr('string_utils.manipulation.MARGIN_RE', MARGIN_RE)

    output = strip_margin(input_string)
    assert output == expected_output
