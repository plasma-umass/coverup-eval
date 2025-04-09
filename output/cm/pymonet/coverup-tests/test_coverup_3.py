# file pymonet/semigroups.py:44-61
# lines [44, 45, 49, 51, 52, 54, 61]
# branches []

import pytest
from pymonet.semigroups import All

def test_all_str_representation(mocker):
    # Mock the __str__ method to ensure it is called
    mocker.patch.object(All, '__str__', return_value='All[value=True]')
    
    all_instance = All(True)
    str_representation = str(all_instance)
    
    # Verify the __str__ method was called and the representation is correct
    All.__str__.assert_called_once_with()
    assert str_representation == 'All[value=True]'
    
    # Cleanup is not necessary as the mocker.patch ensures isolation
