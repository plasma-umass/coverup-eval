# file: httpie/output/processing.py:16-23
# asked: {"lines": [16, 18, 19, 20, 21, 22, 23], "branches": [[20, 0], [20, 21], [21, 0], [21, 22], [22, 21], [22, 23]]}
# gained: {"lines": [16, 18, 19, 20, 21, 22, 23], "branches": [[20, 0], [20, 21], [21, 0], [21, 22], [22, 21], [22, 23]]}

import pytest
from httpie.output.processing import Conversion
from httpie.plugins import ConverterPlugin
from httpie.plugins.registry import plugin_manager
from unittest.mock import patch

class DummyConverter(ConverterPlugin):
    @classmethod
    def supports(cls, mime):
        return mime == 'application/json'

def test_get_converter_valid_mime(monkeypatch):
    def mock_is_valid_mime(mime):
        return True

    monkeypatch.setattr('httpie.output.processing.is_valid_mime', mock_is_valid_mime)
    monkeypatch.setattr(plugin_manager, 'get_converters', lambda: [DummyConverter])

    converter = Conversion.get_converter('application/json')
    assert converter is not None
    assert isinstance(converter, DummyConverter)

def test_get_converter_invalid_mime(monkeypatch):
    def mock_is_valid_mime(mime):
        return False

    monkeypatch.setattr('httpie.output.processing.is_valid_mime', mock_is_valid_mime)

    converter = Conversion.get_converter('application/json')
    assert converter is None

def test_get_converter_no_supported_converter(monkeypatch):
    def mock_is_valid_mime(mime):
        return True

    class UnsupportedConverter(ConverterPlugin):
        @classmethod
        def supports(cls, mime):
            return False

    monkeypatch.setattr('httpie.output.processing.is_valid_mime', mock_is_valid_mime)
    monkeypatch.setattr(plugin_manager, 'get_converters', lambda: [UnsupportedConverter])

    converter = Conversion.get_converter('application/json')
    assert converter is None
