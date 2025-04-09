# file: pytutils/props.py:1-10
# asked: {"lines": [1, 2, 6, 7, 9, 10], "branches": []}
# gained: {"lines": [1, 2, 6, 7, 9, 10], "branches": []}

import pytest
from pytutils.props import roclassproperty

class TestClass:
    @roclassproperty
    def test_property(cls):
        return "test_value"

def test_roclassproperty():
    # Access the class property to trigger __get__
    assert TestClass.test_property == "test_value"
