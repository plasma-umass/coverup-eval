# file mimesis/enums.py:221-230
# lines [221, 222, 227, 228, 229, 230]
# branches []

import pytest
from mimesis.enums import NumTypes

def test_numtypes_enum():
    assert NumTypes.FLOATS.value == 'floats'
    assert NumTypes.INTEGERS.value == 'integers'
    assert NumTypes.COMPLEXES.value == 'complexes'
    assert NumTypes.DECIMALS.value == 'decimals'

    # Ensure all enum members are tested
    assert len(NumTypes) == 4
    for num_type in NumTypes:
        assert num_type in [NumTypes.FLOATS, NumTypes.INTEGERS, NumTypes.COMPLEXES, NumTypes.DECIMALS]
