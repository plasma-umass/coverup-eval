# file: pytutils/lazy/lazy_import.py:449-475
# asked: {"lines": [449, 474, 475], "branches": []}
# gained: {"lines": [449, 474, 475], "branches": []}

import pytest
from pytutils.lazy.lazy_import import lazy_import

def test_lazy_import(monkeypatch):
    class MockImportProcessor:
        def __init__(self, lazy_import_class=None):
            self.lazy_import_class = lazy_import_class
            self.scope = None
            self.text = None

        def lazy_import(self, scope, text):
            self.scope = scope
            self.text = text
            return "mocked"

    monkeypatch.setattr('pytutils.lazy.lazy_import.ImportProcessor', MockImportProcessor)

    scope = {}
    text = '''
    from some_module import (
        foo,
        bar,
        baz,
    )
    import another_module
    '''
    result = lazy_import(scope, text)
    
    assert result == "mocked"
    assert scope == {}
    assert text == '''
    from some_module import (
        foo,
        bar,
        baz,
    )
    import another_module
    '''
