# file apimd/parser.py:56-59
# lines [56, 58, 59]
# branches []

import pytest
from apimd.parser import is_magic

def test_is_magic():
    # Test for non-magic name
    assert not is_magic("normal_function"), "Should return False for non-magic names"

    # Test for magic name
    assert is_magic("__init__"), "Should return True for magic names"

    # Test for namespaced magic name
    assert is_magic("class.__init__"), "Should return True for namespaced magic names"

    # Test for namespaced non-magic name
    assert not is_magic("class.normal_function"), "Should return False for namespaced non-magic names"

    # Test for name with only leading magic pattern
    assert not is_magic("__notmagic"), "Should return False for names with only leading magic pattern"

    # Test for name with only trailing magic pattern
    assert not is_magic("notmagic__"), "Should return False for names with only trailing magic pattern"
