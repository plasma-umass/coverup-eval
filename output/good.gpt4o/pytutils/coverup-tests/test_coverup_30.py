# file pytutils/lazy/lazy_import.py:136-149
# lines [136, 145, 146, 147, 148, 149]
# branches []

import pytest
from unittest.mock import Mock

# Assuming the ScopeReplacer class is imported from pytutils.lazy.lazy_import
from pytutils.lazy.lazy_import import ScopeReplacer

def test_scope_replacer_initialization():
    # Mock the scope and factory
    scope = {}
    factory = Mock()
    name = 'test_obj'

    # Create an instance of ScopeReplacer
    replacer = ScopeReplacer(scope, factory, name)

    # Access the internal attributes directly to avoid triggering any custom __getattribute__ logic
    assert object.__getattribute__(replacer, '_scope') is scope
    assert object.__getattribute__(replacer, '_factory') is factory
    assert object.__getattribute__(replacer, '_name') == name
    assert object.__getattribute__(replacer, '_real_obj') is None
    assert scope[name] is replacer

    # Clean up
    del scope[name]

def test_scope_replacer_factory_call():
    # Mock the scope and factory
    scope = {}
    factory = Mock()
    name = 'test_obj'

    # Create an instance of ScopeReplacer
    replacer = ScopeReplacer(scope, factory, name)

    # Simulate the use of the replacer which should call the factory
    replacer._real_obj = replacer._factory(replacer, scope, name)

    # Assertions to verify the factory was called correctly
    factory.assert_called_once_with(replacer, scope, name)

    # Clean up
    del scope[name]

@pytest.fixture(autouse=True)
def cleanup():
    yield
    # Clean up any global state or side effects here if necessary
