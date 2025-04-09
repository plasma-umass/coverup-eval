# file lib/ansible/utils/version.py:85-125
# lines [85, 86, 91, 92, 94, 95, 97, 98, 99, 100, 101, 103, 105, 106, 108, 109, 110, 111, 112, 113, 114, 116, 118, 119, 121, 122, 124, 125]
# branches ['98->99', '98->100', '100->101', '100->103', '109->110', '109->111', '111->112', '111->113', '113->114', '113->116']

import pytest
from ansible.utils.version import _Numeric

def test_numeric_comparison():
    num1 = _Numeric("5")
    num2 = _Numeric("10")
    num3 = _Numeric("5")
    num4 = 10
    num5 = 5

    # Test __eq__
    assert num1 == num3
    assert num1 != num2
    assert num1 != num4
    assert num1 == num5

    # Test __ne__
    assert num1 != num2
    assert num1 != num4
    assert num1 == num3

    # Test __lt__
    assert num1 < num2
    assert num1 < num4
    with pytest.raises(ValueError):
        num1 < "string"

    # Test __le__
    assert num1 <= num3
    assert num1 <= num2
    assert num1 <= num5

    # Test __gt__
    assert num2 > num1
    assert num4 > num1
    assert num2 > num5

    # Test __ge__
    assert num2 >= num1
    assert num1 >= num3
    assert num4 >= num1

    # Test __repr__
    assert repr(num1) == "5"
    assert repr(num2) == "10"
