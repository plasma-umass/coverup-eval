# file apimd/parser.py:156-158
# lines [156, 158]
# branches []

import pytest
from apimd.parser import _type_name

def test__type_name():
    class CustomType:
        pass

    # Test with built-in type
    assert _type_name(123) == 'int'
    assert _type_name('abc') == 'str'

    # Test with custom type
    custom_obj = CustomType()
    assert _type_name(custom_obj) == CustomType.__qualname__

    # Test with None
    assert _type_name(None) == 'NoneType'
