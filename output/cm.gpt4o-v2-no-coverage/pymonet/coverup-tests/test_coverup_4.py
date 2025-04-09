# file: pymonet/semigroups.py:140-157
# asked: {"lines": [140, 141, 145, 147, 148, 150, 157], "branches": []}
# gained: {"lines": [140, 141, 145, 147, 148, 150, 157], "branches": []}

import pytest
from pymonet.semigroups import Max

def test_max_str():
    max_instance = Max(5)
    assert str(max_instance) == 'Max[value=5]'

def test_max_concat():
    max1 = Max(5)
    max2 = Max(10)
    result = max1.concat(max2)
    assert isinstance(result, Max)
    assert result.value == 10

    result = max2.concat(max1)
    assert isinstance(result, Max)
    assert result.value == 10

    max3 = Max(5)
    result = max1.concat(max3)
    assert isinstance(result, Max)
    assert result.value == 5
