# file: apimd/parser.py:156-158
# asked: {"lines": [156, 158], "branches": []}
# gained: {"lines": [156, 158], "branches": []}

import pytest
from apimd.parser import _type_name

def test_type_name():
    class DummyClass:
        pass

    dummy_instance = DummyClass()
    assert _type_name(dummy_instance) == "test_type_name.<locals>.DummyClass"
    assert _type_name(123) == "int"
    assert _type_name("test") == "str"
    assert _type_name(None) == "NoneType"
