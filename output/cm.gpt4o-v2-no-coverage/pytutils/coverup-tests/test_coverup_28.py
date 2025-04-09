# file: pytutils/lazy/lazy_import.py:136-149
# asked: {"lines": [136, 145, 146, 147, 148, 149], "branches": []}
# gained: {"lines": [136, 145, 146, 147, 148, 149], "branches": []}

import pytest
from pytutils.lazy.lazy_import import ScopeReplacer

def test_scope_replacer_init():
    scope = {}
    factory = lambda self, scope, name: "real_object"
    name = "test_obj"
    
    replacer = ScopeReplacer(scope, factory, name)
    
    assert scope[name] is replacer
    assert object.__getattribute__(replacer, '_scope') is scope
    assert object.__getattribute__(replacer, '_factory') is factory
    assert object.__getattribute__(replacer, '_name') == name
    assert object.__getattribute__(replacer, '_real_obj') is None

def test_scope_replacer_resolve():
    scope = {}
    factory = lambda self, scope, name: "real_object"
    name = "test_obj"
    
    replacer = ScopeReplacer(scope, factory, name)
    resolved_obj = object.__getattribute__(replacer, '_resolve')()
    
    assert resolved_obj == "real_object"
    assert scope[name] == "real_object"
    assert object.__getattribute__(replacer, '_real_obj') == "real_object"
