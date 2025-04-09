# file: httpie/output/processing.py:16-23
# asked: {"lines": [16, 18, 19, 20, 21, 22, 23], "branches": [[20, 0], [20, 21], [21, 0], [21, 22], [22, 21], [22, 23]]}
# gained: {"lines": [16, 18, 19, 20, 21, 22, 23], "branches": [[20, 0], [20, 21], [21, 0], [21, 22], [22, 21], [22, 23]]}

import pytest
from httpie.output.processing import Conversion
from httpie.plugins import ConverterPlugin
from httpie.plugins.registry import plugin_manager

# Mocking is_valid_mime
def mock_is_valid_mime(mime):
    return mime == "application/json"

# Mocking plugin_manager.get_converters
class MockConverterPlugin(ConverterPlugin):
    def __init__(self, mime):
        self.mime = mime

    @classmethod
    def supports(cls, mime):
        return mime == "application/json"

def mock_get_converters():
    return [MockConverterPlugin]

def test_get_converter_valid_mime(monkeypatch):
    monkeypatch.setattr("httpie.output.processing.is_valid_mime", mock_is_valid_mime)
    monkeypatch.setattr(plugin_manager, "get_converters", mock_get_converters)
    
    converter = Conversion.get_converter("application/json")
    assert isinstance(converter, MockConverterPlugin)
    assert converter.mime == "application/json"

def test_get_converter_invalid_mime(monkeypatch):
    monkeypatch.setattr("httpie.output.processing.is_valid_mime", mock_is_valid_mime)
    monkeypatch.setattr(plugin_manager, "get_converters", mock_get_converters)
    
    converter = Conversion.get_converter("text/plain")
    assert converter is None

def test_get_converter_no_supported_converter(monkeypatch):
    def mock_is_valid_mime(mime):
        return True

    class UnsupportedConverterPlugin(ConverterPlugin):
        @classmethod
        def supports(cls, mime):
            return False

    def mock_get_converters():
        return [UnsupportedConverterPlugin]

    monkeypatch.setattr("httpie.output.processing.is_valid_mime", mock_is_valid_mime)
    monkeypatch.setattr(plugin_manager, "get_converters", mock_get_converters)
    
    converter = Conversion.get_converter("application/xml")
    assert converter is None
