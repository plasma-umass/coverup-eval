# file: pytutils/lazy/lazy_import.py:136-149
# asked: {"lines": [136, 145, 146, 147, 148, 149], "branches": []}
# gained: {"lines": [136, 145, 146, 147, 148, 149], "branches": []}

import pytest

from pytutils.lazy.lazy_import import ScopeReplacer

def test_scope_replacer_initialization():
    scope = {}
    factory = lambda self, scope, name: "real_object"
    name = "test_obj"
    
    replacer = ScopeReplacer(scope, factory, name)
    
    # Accessing private attributes directly using object.__getattribute__
    assert object.__getattribute__(replacer, '_scope') == scope
    assert object.__getattribute__(replacer, '_factory') == factory
    assert object.__getattribute__(replacer, '_name') == name
    assert object.__getattribute__(replacer, '_real_obj') is None
    assert scope[name] is replacer

def test_scope_replacer_cleanup(monkeypatch):
    scope = {}
    factory = lambda self, scope, name: "real_object"
    name = "test_obj"
    
    replacer = ScopeReplacer(scope, factory, name)
    
    # Accessing private attributes directly using object.__getattribute__
    assert object.__getattribute__(replacer, '_scope') == scope
    assert object.__getattribute__(replacer, '_factory') == factory
    assert object.__getattribute__(replacer, '_name') == name
    assert object.__getattribute__(replacer, '_real_obj') is None
    assert scope[name] is replacer
    
    # Clean up
    monkeypatch.delitem(scope, name, raising=False)
    assert name not in scope
