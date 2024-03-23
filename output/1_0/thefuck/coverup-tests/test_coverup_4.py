# file thefuck/const.py:4-9
# lines [4, 5, 6, 8, 9]
# branches []

import pytest
from thefuck.const import _GenConst

def test_genconst_repr():
    # Create an instance of _GenConst
    const_name = "test_const"
    gen_const = _GenConst(const_name)

    # Check the __repr__ method
    expected_repr = u'<const: test_const>'
    assert repr(gen_const) == expected_repr
