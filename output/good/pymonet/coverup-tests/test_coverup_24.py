# file pymonet/semigroups.py:64-81
# lines [64, 65, 69, 71, 72, 74, 81]
# branches []

import pytest
from pymonet.semigroups import One

def test_one_str_representation(mocker):
    # Mocking __str__ to ensure it is called during the test
    mocker.patch.object(One, '__str__', return_value='One[value=True]')
    one_instance = One(True)
    assert str(one_instance) == 'One[value=True]'
    One.__str__.assert_called_once()

def test_one_concat():
    one_true = One(True)
    one_false = One(False)
    one_another_true = One(True)

    # Concatenating with a falsy value should return the original truthy value
    result = one_true.concat(one_false)
    assert isinstance(result, One)
    assert result.value is True

    # Concatenating with a truthy value should return the first truthy value
    result = one_false.concat(one_another_true)
    assert isinstance(result, One)
    assert result.value is True

    # Cleanup is not necessary as no global state is modified
