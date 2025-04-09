# file apimd/parser.py:56-59
# lines [56, 58, 59]
# branches []

import pytest
from apimd.parser import is_magic

def test_is_magic():
    # Test case where the name is a magic method
    assert is_magic('__init__') == True
    assert is_magic('__str__') == True

    # Test case where the name is not a magic method
    assert is_magic('init') == False
    assert is_magic('str__') == False
    assert is_magic('__str') == False

    # Test case where the name has a dot and is a magic method
    assert is_magic('module.__init__') == True

    # Test case where the name has a dot and is not a magic method
    assert is_magic('module.init') == False
