# file: lib/ansible/utils/version.py:85-125
# asked: {"lines": [85, 86, 91, 92, 94, 95, 97, 98, 99, 100, 101, 103, 105, 106, 108, 109, 110, 111, 112, 113, 114, 116, 118, 119, 121, 122, 124, 125], "branches": [[98, 99], [98, 100], [100, 101], [100, 103], [109, 110], [109, 111], [111, 112], [111, 113], [113, 114], [113, 116]]}
# gained: {"lines": [85, 86, 91, 92, 94, 95, 97, 98, 99, 100, 101, 103, 105, 106, 108, 109, 110, 111, 112, 113, 116, 118, 119, 121, 122, 124, 125], "branches": [[98, 99], [98, 100], [100, 101], [100, 103], [109, 110], [109, 111], [111, 112], [111, 113], [113, 116]]}

import pytest
from ansible.utils.version import _Numeric

def test_numeric_init():
    num = _Numeric("10")
    assert num.specifier == 10

def test_numeric_repr():
    num = _Numeric("10")
    assert repr(num) == "10"

def test_numeric_eq():
    num1 = _Numeric("10")
    num2 = _Numeric("10")
    num3 = _Numeric("20")
    assert num1 == num2
    assert num1 != num3
    assert num1 == 10
    assert num1 != 20
    assert num1 != "10"

def test_numeric_ne():
    num1 = _Numeric("10")
    num2 = _Numeric("20")
    assert num1 != num2
    assert num1 != 20
    assert num1 != "10"

def test_numeric_lt():
    num1 = _Numeric("10")
    num2 = _Numeric("20")
    assert num1 < num2
    assert num1 < 20
    with pytest.raises(ValueError):
        num1 < "10"

def test_numeric_le():
    num1 = _Numeric("10")
    num2 = _Numeric("20")
    assert num1 <= num2
    assert num1 <= 10
    assert num1 <= 20
    with pytest.raises(ValueError):
        num1 <= "10"

def test_numeric_gt():
    num1 = _Numeric("20")
    num2 = _Numeric("10")
    assert num1 > num2
    assert num1 > 10
    assert num1 > 5
    with pytest.raises(ValueError):
        num1 > "10"

def test_numeric_ge():
    num1 = _Numeric("20")
    num2 = _Numeric("10")
    assert num1 >= num2
    assert num1 >= 10
    assert num1 >= 20
    with pytest.raises(ValueError):
        num1 >= "10"
