# file: pytutils/lazy/lazy_import.py:449-475
# asked: {"lines": [449, 474, 475], "branches": []}
# gained: {"lines": [449, 474, 475], "branches": []}

import pytest
from unittest import mock
from pytutils.lazy.lazy_import import lazy_import

class MockImportProcessor:
    def __init__(self, lazy_import_class=None):
        self.lazy_import_class = lazy_import_class

    def lazy_import(self, scope, text):
        scope['__lazy_imported__'] = text
        return scope

@pytest.fixture
def mock_import_processor(monkeypatch):
    monkeypatch.setattr('pytutils.lazy.lazy_import.ImportProcessor', MockImportProcessor)

def test_lazy_import_with_class(mock_import_processor):
    scope = {}
    text = "import os"
    result = lazy_import(scope, text, lazy_import_class=MockImportProcessor)
    assert '__lazy_imported__' in result
    assert result['__lazy_imported__'] == text

def test_lazy_import_without_class(mock_import_processor):
    scope = {}
    text = "import sys"
    result = lazy_import(scope, text)
    assert '__lazy_imported__' in result
    assert result['__lazy_imported__'] == text
