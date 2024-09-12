# file: httpie/output/processing.py:16-23
# asked: {"lines": [], "branches": [[21, 0], [22, 21]]}
# gained: {"lines": [], "branches": [[21, 0], [22, 21]]}

import pytest
from unittest.mock import Mock, patch
from httpie.output.processing import Conversion
from httpie.plugins import ConverterPlugin
from httpie.plugins.registry import plugin_manager

# Mocking is_valid_mime function
def is_valid_mime(mime: str) -> bool:
    return mime == "application/json"

class MockConverterPlugin(ConverterPlugin):
    def __init__(self, mime):
        self.mime = mime

    @classmethod
    def supports(cls, mime):
        return mime == "application/json"

@pytest.fixture
def mock_plugin_manager(monkeypatch):
    mock_get_converters = Mock(return_value=[MockConverterPlugin])
    monkeypatch.setattr(plugin_manager, "get_converters", mock_get_converters)
    yield

def test_get_converter_valid_mime(mock_plugin_manager):
    converter = Conversion.get_converter("application/json")
    assert isinstance(converter, MockConverterPlugin)
    assert converter.mime == "application/json"

def test_get_converter_invalid_mime(mock_plugin_manager):
    converter = Conversion.get_converter("text/html")
    assert converter is None
