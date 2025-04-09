# file: lib/ansible/utils/version.py:85-125
# asked: {"lines": [95, 98, 99, 100, 101, 103, 106, 109, 110, 111, 112, 113, 114, 116, 119, 122, 125], "branches": [[98, 99], [98, 100], [100, 101], [100, 103], [109, 110], [109, 111], [111, 112], [111, 113], [113, 114], [113, 116]]}
# gained: {"lines": [95, 98, 99, 100, 101, 106, 109, 110, 111, 112, 113, 116, 119, 122, 125], "branches": [[98, 99], [98, 100], [100, 101], [109, 110], [109, 111], [111, 112], [111, 113], [113, 116]]}

import pytest
from ansible.utils.version import _Numeric

def test_numeric_repr():
    num = _Numeric(5)
    assert repr(num) == '5'

def test_numeric_eq():
    num1 = _Numeric(5)
    num2 = _Numeric(5)
    num3 = _Numeric(6)
    assert num1 == num2
    assert num1 != num3
    assert num1 == 5
    assert num1 != 6

def test_numeric_ne():
    num1 = _Numeric(5)
    num2 = _Numeric(5)
    num3 = _Numeric(6)
    assert not (num1 != num2)
    assert num1 != num3
    assert not (num1 != 5)
    assert num1 != 6

def test_numeric_lt():
    num1 = _Numeric(5)
    num2 = _Numeric(6)
    assert num1 < num2
    assert num1 < 6
    with pytest.raises(ValueError):
        num1 < "string"

def test_numeric_le():
    num1 = _Numeric(5)
    num2 = _Numeric(5)
    num3 = _Numeric(6)
    assert num1 <= num2
    assert num1 <= num3
    assert num1 <= 5
    assert num1 <= 6

def test_numeric_gt():
    num1 = _Numeric(6)
    num2 = _Numeric(5)
    assert num1 > num2
    assert num1 > 5
    assert not (num1 > 6)

def test_numeric_ge():
    num1 = _Numeric(6)
    num2 = _Numeric(5)
    num3 = _Numeric(6)
    assert num1 >= num2
    assert num1 >= num3
    assert num1 >= 6
    assert not (num2 >= num1)
