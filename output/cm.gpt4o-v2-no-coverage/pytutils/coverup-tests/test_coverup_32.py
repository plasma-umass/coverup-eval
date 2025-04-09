# file: pytutils/lazy/simple_import.py:24-61
# asked: {"lines": [29, 32, 34, 35, 38, 47, 49, 53, 54, 55, 57, 59, 61], "branches": [[53, 54], [53, 59]]}
# gained: {"lines": [29, 32, 34, 35, 38, 49, 53, 54, 55, 57, 59, 61], "branches": [[53, 54]]}

import pytest
import sys
from types import ModuleType
from pytutils.lazy.simple_import import make_lazy, NonLocal, _LazyModuleMarker

def test_make_lazy(monkeypatch):
    # Setup
    module_name = "test_module"
    test_module = ModuleType(module_name)
    test_module.some_attr = "some_value"
    
    # Ensure the module is not already in sys.modules
    if module_name in sys.modules:
        del sys.modules[module_name]
    
    # Mock __import__ to return our test module
    def mock_import(name, *args):
        if name == module_name:
            return test_module
        return original_import(name, *args)
    
    original_import = __import__
    monkeypatch.setattr("builtins.__import__", mock_import)
    
    # Act
    make_lazy(module_name)
    
    # Assert
    assert isinstance(sys.modules[module_name], _LazyModuleMarker)
    assert isinstance(sys.modules[module_name], ModuleType)
    
    # Access an attribute to trigger the actual import
    assert sys.modules[module_name].some_attr == "some_value"
    
    # Cleanup
    del sys.modules[module_name]
    monkeypatch.undo()
