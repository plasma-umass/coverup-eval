# file string_utils/manipulation.py:52-76
# lines [64, 68]
# branches ['63->64', '67->68']

import pytest
from string_utils.manipulation import __RomanNumbers

@pytest.fixture
def mock_mappings(mocker):
    mappings = {
        0: {1: 'I', 5: 'V'},
        1: {1: 'X', 5: 'L'},
        2: {1: 'C', 5: 'D'},
        3: {1: 'M'}
    }
    mocker.patch.object(__RomanNumbers, '_RomanNumbers__mappings', mappings)

def test_encode_digit_for_value_four_and_five(mock_mappings):
    assert __RomanNumbers._RomanNumbers__encode_digit(0, 4) == 'IV'
    assert __RomanNumbers._RomanNumbers__encode_digit(0, 5) == 'V'
