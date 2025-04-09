# file: apimd/parser.py:36-43
# asked: {"lines": [38, 39, 40, 41, 42, 43], "branches": [[39, 40], [39, 43], [41, 39], [41, 42]]}
# gained: {"lines": [38, 39, 40, 41, 42, 43], "branches": [[39, 40], [39, 43], [41, 39], [41, 42]]}

import pytest
from apimd.parser import _attr

class TestAttrFunction:
    class Dummy:
        def __init__(self):
            self.a = 'value'
            self.b = None
            self.c = self.Nested()

        class Nested:
            def __init__(self):
                self.d = 'nested_value'

    def test_attr_direct(self):
        obj = self.Dummy()
        assert _attr(obj, 'a') == 'value'

    def test_attr_none(self):
        obj = self.Dummy()
        assert _attr(obj, 'b') is None

    def test_attr_nested(self):
        obj = self.Dummy()
        assert _attr(obj, 'c.d') == 'nested_value'

    def test_attr_nonexistent(self):
        obj = self.Dummy()
        assert _attr(obj, 'x') is None

    def test_attr_partial_nonexistent(self):
        obj = self.Dummy()
        assert _attr(obj, 'c.x') is None
