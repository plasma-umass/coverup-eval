# file: string_utils/manipulation.py:108-114
# asked: {"lines": [108, 109, 110, 111, 112, 114], "branches": [[110, 111], [110, 114], [111, 110], [111, 112]]}
# gained: {"lines": [108, 109, 110, 111, 112, 114], "branches": [[110, 111], [110, 114], [111, 110], [111, 112]]}

import pytest
from string_utils.manipulation import __RomanNumbers

def test__index_for_sign_valid_sign():
    assert __RomanNumbers._RomanNumbers__index_for_sign('I') == 0
    assert __RomanNumbers._RomanNumbers__index_for_sign('V') == 0
    assert __RomanNumbers._RomanNumbers__index_for_sign('X') == 1
    assert __RomanNumbers._RomanNumbers__index_for_sign('L') == 1
    assert __RomanNumbers._RomanNumbers__index_for_sign('C') == 2
    assert __RomanNumbers._RomanNumbers__index_for_sign('D') == 2
    assert __RomanNumbers._RomanNumbers__index_for_sign('M') == 3

def test__index_for_sign_invalid_sign():
    with pytest.raises(ValueError, match='Invalid token found: "A"'):
        __RomanNumbers._RomanNumbers__index_for_sign('A')
