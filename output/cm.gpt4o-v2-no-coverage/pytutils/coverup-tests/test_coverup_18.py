# file: pytutils/props.py:1-10
# asked: {"lines": [1, 2, 6, 7, 9, 10], "branches": []}
# gained: {"lines": [1, 2, 6, 7, 9, 10], "branches": []}

import pytest

from pytutils.props import roclassproperty

class TestRoClassProperty:
    def test_roclassproperty_init(self):
        def dummy_func(cls):
            return "test"
        
        prop = roclassproperty(dummy_func)
        assert prop.f == dummy_func

    def test_roclassproperty_get(self):
        class DummyClass:
            @roclassproperty
            def test_prop(cls):
                return "test_value"
        
        assert DummyClass.test_prop == "test_value"
