# file: pytutils/lazy/simple_import.py:24-61
# asked: {"lines": [24, 29, 32, 34, 35, 38, 47, 49, 53, 54, 55, 57, 59, 61], "branches": [[53, 54], [53, 59]]}
# gained: {"lines": [24, 29, 32, 34, 35, 38, 49, 53, 54, 55, 57, 59, 61], "branches": [[53, 54]]}

import sys
import pytest
from types import ModuleType
from pytutils.lazy.simple_import import make_lazy

class NonLocal:
    def __init__(self, value):
        self.value = value

class _LazyModuleMarker:
    pass

def test_make_lazy(monkeypatch):
    # Mock __import__ to control the import process
    def mock_import(name, *args):
        if name == 'fake_module':
            fake_module = ModuleType('fake_module')
            fake_module.some_attr = 'some_value'
            return fake_module
        return __import__(name, *args)

    monkeypatch.setattr('builtins.__import__', mock_import)

    # Ensure the module is not already in sys.modules
    if 'fake_module' in sys.modules:
        del sys.modules['fake_module']

    # Call make_lazy to create the lazy module
    make_lazy('fake_module')

    # Access an attribute to trigger the lazy loading
    assert sys.modules['fake_module'].some_attr == 'some_value'

    # Ensure the module is now fully loaded
    assert isinstance(sys.modules['fake_module'], ModuleType)

    # Clean up
    del sys.modules['fake_module']
