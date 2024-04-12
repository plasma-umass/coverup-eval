# file pymonet/semigroups.py:140-157
# lines [140, 141, 145, 147, 148, 150, 157]
# branches []

import pytest
from pymonet.semigroups import Max

def test_max_concat():
    max1 = Max(10)
    max2 = Max(20)
    max3 = Max(-5)

    # Test concat with larger value
    result1 = max1.concat(max2)
    assert str(result1) == 'Max[value=20]', "Concatenation should result in the larger value"
    assert isinstance(result1, Max), "Result of concat should be an instance of Max"

    # Test concat with smaller value
    result2 = max2.concat(max3)
    assert str(result2) == 'Max[value=20]', "Concatenation should result in the larger value"
    assert isinstance(result2, Max), "Result of concat should be an instance of Max"

    # Test concat with equal value
    result3 = max1.concat(max1)
    assert str(result3) == 'Max[value=10]', "Concatenation with equal values should result in the same value"
    assert isinstance(result3, Max), "Result of concat should be an instance of Max"

    # Test concat with neutral element
    max_neutral = Max(Max.neutral_element)
    result4 = max_neutral.concat(max1)
    assert str(result4) == 'Max[value=10]', "Concatenation with neutral element should result in the non-neutral value"
    assert isinstance(result4, Max), "Result of concat should be an instance of Max"

    result5 = max1.concat(max_neutral)
    assert str(result5) == 'Max[value=10]', "Concatenation with neutral element should result in the non-neutral value"
    assert isinstance(result5, Max), "Result of concat should be an instance of Max"
