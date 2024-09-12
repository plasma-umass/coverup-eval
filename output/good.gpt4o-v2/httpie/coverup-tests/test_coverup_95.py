# file: httpie/output/processing.py:16-23
# asked: {"lines": [20, 21, 22, 23], "branches": [[20, 0], [20, 21], [21, 0], [21, 22], [22, 21], [22, 23]]}
# gained: {"lines": [20, 21, 22, 23], "branches": [[20, 0], [20, 21], [21, 22], [22, 23]]}

import pytest
from httpie.output.processing import Conversion
from httpie.plugins import ConverterPlugin
from httpie.plugins.registry import plugin_manager
from httpie.output.processing import is_valid_mime

class MockConverter(ConverterPlugin):
    def __init__(self, mime):
        self.mime = mime

    @classmethod
    def supports(cls, mime):
        return mime == "application/json"

def test_get_converter_valid_mime(monkeypatch):
    def mock_is_valid_mime(mime):
        return True

    def mock_get_converters():
        return [MockConverter]

    monkeypatch.setattr("httpie.output.processing.is_valid_mime", mock_is_valid_mime)
    monkeypatch.setattr(plugin_manager, "get_converters", mock_get_converters)

    converter = Conversion.get_converter("application/json")
    assert converter is not None
    assert isinstance(converter, MockConverter)
    assert converter.mime == "application/json"

def test_get_converter_invalid_mime(monkeypatch):
    def mock_is_valid_mime(mime):
        return False

    monkeypatch.setattr("httpie.output.processing.is_valid_mime", mock_is_valid_mime)

    converter = Conversion.get_converter("invalid/mime")
    assert converter is None
