# file: semantic_release/settings.py:80-94
# asked: {"lines": [80, 87, 89, 90, 92, 93, 94], "branches": []}
# gained: {"lines": [80, 87, 89, 90, 92, 93, 94], "branches": []}

import pytest
import importlib
from semantic_release.settings import current_commit_parser, ImproperConfigurationError

def test_current_commit_parser_success(monkeypatch):
    class MockModule:
        @staticmethod
        def mock_parser():
            return "parsed"

    def mock_import_module(name):
        if name == "mock_module":
            return MockModule
        raise ImportError

    monkeypatch.setattr(importlib, "import_module", mock_import_module)
    monkeypatch.setattr("semantic_release.settings.config", {"commit_parser": "mock_module.mock_parser"})

    parser = current_commit_parser()
    assert parser() == "parsed"

def test_current_commit_parser_import_error(monkeypatch):
    def mock_import_module(name):
        raise ImportError

    monkeypatch.setattr(importlib, "import_module", mock_import_module)
    monkeypatch.setattr("semantic_release.settings.config", {"commit_parser": "nonexistent.module"})

    with pytest.raises(ImproperConfigurationError) as excinfo:
        current_commit_parser()
    assert 'Unable to import parser' in str(excinfo.value)

def test_current_commit_parser_attribute_error(monkeypatch):
    class MockModule:
        pass

    def mock_import_module(name):
        if name == "mock_module":
            return MockModule
        raise ImportError

    monkeypatch.setattr(importlib, "import_module", mock_import_module)
    monkeypatch.setattr("semantic_release.settings.config", {"commit_parser": "mock_module.nonexistent_parser"})

    with pytest.raises(ImproperConfigurationError) as excinfo:
        current_commit_parser()
    assert 'Unable to import parser' in str(excinfo.value)
