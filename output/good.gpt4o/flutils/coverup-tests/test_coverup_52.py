# file flutils/objutils.py:206-231
# lines [206, 228, 229, 230, 231]
# branches ['228->229', '228->231', '229->228', '229->230']

import pytest
from collections.abc import ValuesView, KeysView
from collections import UserList
from flutils.objutils import is_subclass_of_any

def test_is_subclass_of_any():
    # Test case where obj is a subclass of one of the provided classes
    obj = dict(a=1, b=2)
    assert is_subclass_of_any(obj.keys(), ValuesView, KeysView, UserList) == True

    # Test case where obj is not a subclass of any of the provided classes
    assert is_subclass_of_any(obj.keys(), ValuesView, UserList) == False

    # Test case where obj is a direct instance of one of the provided classes
    class CustomDict(dict):
        pass

    custom_obj = CustomDict()
    assert is_subclass_of_any(custom_obj, dict, list) == True

    # Test case where no classes are provided
    assert is_subclass_of_any(obj.keys()) == False

    # Test case where obj is None
    assert is_subclass_of_any(None, ValuesView, KeysView, UserList) == False

    # Test case where obj is a class itself
    assert is_subclass_of_any(dict(), dict, list) == True
