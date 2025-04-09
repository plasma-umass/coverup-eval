# file: pytutils/lazy/lazy_import.py:449-475
# asked: {"lines": [449, 474, 475], "branches": []}
# gained: {"lines": [449, 474, 475], "branches": []}

import pytest
from pytutils.lazy.lazy_import import lazy_import

def test_lazy_import(monkeypatch):
    class MockImportProcessor:
        def __init__(self, lazy_import_class=None):
            self.lazy_import_class = lazy_import_class

        def lazy_import(self, scope, text):
            scope['mocked'] = True
            return 'mocked_result'

    monkeypatch.setattr('pytutils.lazy.lazy_import.ImportProcessor', MockImportProcessor)

    scope = {}
    text = '''
    from some_module import (
        foo,
        bar,
        baz,
    )
    import some_module.branch
    import some_module.transport
    '''
    result = lazy_import(scope, text)
    
    assert result == 'mocked_result'
    assert 'mocked' in scope
    assert scope['mocked'] is True
