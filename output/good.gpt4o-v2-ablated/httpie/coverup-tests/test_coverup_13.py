# file: httpie/output/processing.py:16-23
# asked: {"lines": [16, 18, 19, 20, 21, 22, 23], "branches": [[20, 0], [20, 21], [21, 0], [21, 22], [22, 21], [22, 23]]}
# gained: {"lines": [16, 18, 19, 20, 21, 22, 23], "branches": [[20, 0], [20, 21], [21, 0], [21, 22], [22, 21], [22, 23]]}

import pytest
from unittest.mock import Mock, patch
from httpie.output.processing import Conversion

@pytest.fixture
def mock_plugin_manager():
    with patch('httpie.output.processing.plugin_manager') as mock:
        yield mock

@pytest.fixture
def mock_is_valid_mime():
    with patch('httpie.output.processing.is_valid_mime') as mock:
        yield mock

def test_get_converter_valid_mime_supported(mock_plugin_manager, mock_is_valid_mime):
    mock_is_valid_mime.return_value = True
    mock_converter_class = Mock()
    mock_converter_class.supports.return_value = True
    mock_plugin_manager.get_converters.return_value = [mock_converter_class]

    mime = 'application/json'
    converter = Conversion.get_converter(mime)

    assert converter == mock_converter_class.return_value
    mock_is_valid_mime.assert_called_once_with(mime)
    mock_plugin_manager.get_converters.assert_called_once()
    mock_converter_class.supports.assert_called_once_with(mime)
    mock_converter_class.assert_called_once_with(mime)

def test_get_converter_valid_mime_not_supported(mock_plugin_manager, mock_is_valid_mime):
    mock_is_valid_mime.return_value = True
    mock_converter_class = Mock()
    mock_converter_class.supports.return_value = False
    mock_plugin_manager.get_converters.return_value = [mock_converter_class]

    mime = 'application/json'
    converter = Conversion.get_converter(mime)

    assert converter is None
    mock_is_valid_mime.assert_called_once_with(mime)
    mock_plugin_manager.get_converters.assert_called_once()
    mock_converter_class.supports.assert_called_once_with(mime)
    mock_converter_class.assert_not_called()

def test_get_converter_invalid_mime(mock_plugin_manager, mock_is_valid_mime):
    mock_is_valid_mime.return_value = False

    mime = 'invalid/mime'
    converter = Conversion.get_converter(mime)

    assert converter is None
    mock_is_valid_mime.assert_called_once_with(mime)
    mock_plugin_manager.get_converters.assert_not_called()
