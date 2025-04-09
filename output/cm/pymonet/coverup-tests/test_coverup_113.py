# file pymonet/semigroups.py:64-81
# lines [72]
# branches []

import pytest
from pymonet.semigroups import One

def test_one_str_representation():
    one_instance = One(True)
    assert str(one_instance) == 'One[value=True]'
    
    one_instance_false = One(False)
    assert str(one_instance_false) == 'One[value=False]'
