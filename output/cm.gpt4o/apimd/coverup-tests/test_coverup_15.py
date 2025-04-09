# file apimd/parser.py:156-158
# lines [156, 158]
# branches []

import pytest
from apimd.parser import _type_name

def test_type_name():
    class DummyClass:
        pass

    dummy_instance = DummyClass()
    assert _type_name(dummy_instance) == "test_type_name.<locals>.DummyClass"

    dummy_list = []
    assert _type_name(dummy_list) == "list"

    dummy_dict = {}
    assert _type_name(dummy_dict) == "dict"

    dummy_int = 42
    assert _type_name(dummy_int) == "int"

    dummy_str = "test"
    assert _type_name(dummy_str) == "str"

    dummy_func = lambda x: x
    assert _type_name(dummy_func) == "function"
