# file: pytutils/lazy/lazy_import.py:181-183
# asked: {"lines": [181, 182, 183], "branches": []}
# gained: {"lines": [181, 182, 183], "branches": []}

import pytest

class MockObject:
    def __init__(self, value):
        self.value = value

def mock_resolve(self):
    return MockObject("resolved_value")

def test_scope_replacer_getattribute(monkeypatch):
    from pytutils.lazy.lazy_import import ScopeReplacer

    scope = {}
    factory = lambda self, scope, name: MockObject("created_value")
    name = "test_obj"

    replacer = ScopeReplacer(scope, factory, name)
    monkeypatch.setattr(ScopeReplacer, "_resolve", mock_resolve)

    assert replacer.value == "resolved_value"
