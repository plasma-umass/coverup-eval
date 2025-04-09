# file: apimd/parser.py:156-158
# asked: {"lines": [156, 158], "branches": []}
# gained: {"lines": [156, 158], "branches": []}

import pytest
from apimd.parser import _type_name

def test_type_name_with_builtin_type():
    assert _type_name(123) == 'int'
    assert _type_name("test") == 'str'
    assert _type_name(3.14) == 'float'

def test_type_name_with_custom_class():
    class CustomClass:
        pass

    instance = CustomClass()
    assert _type_name(instance) == 'test_type_name_with_custom_class.<locals>.CustomClass'

def test_type_name_with_nested_class():
    class OuterClass:
        class InnerClass:
            pass

    instance = OuterClass.InnerClass()
    assert _type_name(instance) == 'test_type_name_with_nested_class.<locals>.OuterClass.InnerClass'
