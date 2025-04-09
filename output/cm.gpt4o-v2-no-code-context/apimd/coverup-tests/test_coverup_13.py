# file: apimd/parser.py:36-43
# asked: {"lines": [36, 38, 39, 40, 41, 42, 43], "branches": [[39, 40], [39, 43], [41, 39], [41, 42]]}
# gained: {"lines": [36, 38, 39, 40, 41, 42, 43], "branches": [[39, 40], [39, 43], [41, 39], [41, 42]]}

import pytest

# Assuming the _attr function is part of a class or module, we need to import it.
# For this example, let's assume it's part of a module named 'apimd.parser'
from apimd.parser import _attr

class TestAttrFunction:
    def test_attr_single_level(self):
        class TestObj:
            def __init__(self):
                self.value = 42

        obj = TestObj()
        result = _attr(obj, 'value')
        assert result == 42

    def test_attr_nested_level(self):
        class TestObj:
            def __init__(self):
                self.child = self.Child()

            class Child:
                def __init__(self):
                    self.value = 42

        obj = TestObj()
        result = _attr(obj, 'child.value')
        assert result == 42

    def test_attr_non_existent_attr(self):
        class TestObj:
            def __init__(self):
                self.value = 42

        obj = TestObj()
        result = _attr(obj, 'non_existent')
        assert result is None

    def test_attr_partial_non_existent_attr(self):
        class TestObj:
            def __init__(self):
                self.child = self.Child()

            class Child:
                def __init__(self):
                    self.value = 42

        obj = TestObj()
        result = _attr(obj, 'child.non_existent')
        assert result is None
