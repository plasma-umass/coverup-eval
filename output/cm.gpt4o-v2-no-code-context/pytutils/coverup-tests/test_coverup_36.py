# file: pytutils/props.py:25-37
# asked: {"lines": [], "branches": [[33, 35]]}
# gained: {"lines": [], "branches": [[33, 35]]}

import pytest
from pytutils.props import lazyperclassproperty

class TestClass:
    @lazyperclassproperty
    def example_property(cls):
        return "example_value"

def test_lazyperclassproperty(monkeypatch):
    # Ensure the property is not set initially
    attr_name = '_TestClass_lazy_example_property'
    if hasattr(TestClass, attr_name):
        monkeypatch.delattr(TestClass, attr_name)
    
    assert not hasattr(TestClass, attr_name)
    
    # Access the property to trigger the lazy loading
    assert TestClass.example_property == "example_value"
    
    # Ensure the property is now set
    assert hasattr(TestClass, attr_name)
    assert getattr(TestClass, attr_name) == "example_value"
    
    # Access the property again to ensure it returns the cached value
    assert TestClass.example_property == "example_value"
