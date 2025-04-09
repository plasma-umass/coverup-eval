# file: pytutils/lazy/lazy_import.py:449-475
# asked: {"lines": [449, 474, 475], "branches": []}
# gained: {"lines": [449, 474, 475], "branches": []}

import pytest
from pytutils.lazy.lazy_import import lazy_import

class MockImportProcessor:
    def __init__(self, lazy_import_class=None):
        self.lazy_import_class = lazy_import_class
        self.imports = {}

    def lazy_import(self, scope, text):
        self._build_map(text)
        self._convert_imports(scope)

    def _build_map(self, text):
        self.imports = {"mock": "mocked"}

    def _convert_imports(self, scope):
        scope.update(self.imports)

@pytest.fixture
def mock_import_processor(monkeypatch):
    monkeypatch.setattr("pytutils.lazy.lazy_import.ImportProcessor", MockImportProcessor)

def test_lazy_import_with_default_class(mock_import_processor):
    scope = {}
    text = "import mock"
    lazy_import(scope, text)
    assert "mock" in scope
    assert scope["mock"] == "mocked"

def test_lazy_import_with_custom_class(mock_import_processor):
    class CustomImportReplacer:
        pass

    scope = {}
    text = "import mock"
    lazy_import(scope, text, lazy_import_class=CustomImportReplacer)
    assert "mock" in scope
    assert scope["mock"] == "mocked"
