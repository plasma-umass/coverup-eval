# file pymonet/semigroups.py:44-61
# lines [52, 61]
# branches []

import pytest
from pymonet.semigroups import All

def test_all_concat_and_str_methods(mocker):
    # Test the __str__ method
    all_true = All(True)
    assert str(all_true) == 'All[value=True]'

    all_false = All(False)
    assert str(all_false) == 'All[value=False]'

    # Test the concat method
    assert all_true.concat(all_false).value is False
    assert all_false.concat(all_true).value is False
    assert all_true.concat(all_true).value is True
    assert all_false.concat(all_false).value is False
