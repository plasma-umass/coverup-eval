# file: httpie/output/processing.py:16-23
# asked: {"lines": [16, 18, 19, 20, 21, 22, 23], "branches": [[20, 0], [20, 21], [21, 0], [21, 22], [22, 21], [22, 23]]}
# gained: {"lines": [16, 18, 19, 20, 21, 22, 23], "branches": [[20, 0], [20, 21], [21, 0], [21, 22], [22, 21], [22, 23]]}

import pytest
from unittest.mock import Mock, patch
from httpie.output.processing import Conversion

# Mocking the dependencies
@pytest.fixture
def mock_is_valid_mime(monkeypatch):
    mock = Mock(return_value=True)
    monkeypatch.setattr('httpie.output.processing.is_valid_mime', mock)
    return mock

@pytest.fixture
def mock_plugin_manager(monkeypatch):
    mock = Mock()
    monkeypatch.setattr('httpie.output.processing.plugin_manager', mock)
    return mock

def test_get_converter_valid_mime(mock_is_valid_mime, mock_plugin_manager):
    # Mocking a converter class
    class MockConverter:
        def __init__(self, mime):
            self.mime = mime

        @staticmethod
        def supports(mime):
            return True

    mock_plugin_manager.get_converters.return_value = [MockConverter]

    converter = Conversion.get_converter('application/json')
    assert converter is not None
    assert isinstance(converter, MockConverter)
    assert converter.mime == 'application/json'

def test_get_converter_no_supported_converter(mock_is_valid_mime, mock_plugin_manager):
    # Mocking a converter class that does not support the mime type
    class MockConverter:
        def __init__(self, mime):
            self.mime = mime

        @staticmethod
        def supports(mime):
            return False

    mock_plugin_manager.get_converters.return_value = [MockConverter]

    converter = Conversion.get_converter('application/json')
    assert converter is None

def test_get_converter_invalid_mime(monkeypatch, mock_plugin_manager):
    # Mocking is_valid_mime to return False
    mock_is_valid_mime = Mock(return_value=False)
    monkeypatch.setattr('httpie.output.processing.is_valid_mime', mock_is_valid_mime)

    converter = Conversion.get_converter('application/json')
    assert converter is None
