# file httpie/output/processing.py:16-23
# lines [16, 18, 19, 20, 21, 22, 23]
# branches ['20->exit', '20->21', '21->exit', '21->22', '22->21', '22->23']

import pytest
from unittest.mock import patch, MagicMock
from httpie.output.processing import Conversion

@pytest.fixture
def mock_plugin_manager(mocker):
    return mocker.patch('httpie.output.processing.plugin_manager')

@pytest.fixture
def mock_is_valid_mime(mocker):
    return mocker.patch('httpie.output.processing.is_valid_mime')

def test_get_converter_valid_mime(mock_plugin_manager, mock_is_valid_mime):
    mock_is_valid_mime.return_value = True
    mock_converter_class = MagicMock()
    mock_converter_class.supports.return_value = True
    mock_plugin_manager.get_converters.return_value = [mock_converter_class]

    mime = 'application/json'
    converter = Conversion.get_converter(mime)

    mock_is_valid_mime.assert_called_once_with(mime)
    mock_plugin_manager.get_converters.assert_called_once()
    mock_converter_class.supports.assert_called_once_with(mime)
    assert converter == mock_converter_class.return_value

def test_get_converter_invalid_mime(mock_is_valid_mime):
    mock_is_valid_mime.return_value = False

    mime = 'invalid/mime'
    converter = Conversion.get_converter(mime)

    mock_is_valid_mime.assert_called_once_with(mime)
    assert converter is None

def test_get_converter_no_supported_converter(mock_plugin_manager, mock_is_valid_mime):
    mock_is_valid_mime.return_value = True
    mock_converter_class = MagicMock()
    mock_converter_class.supports.return_value = False
    mock_plugin_manager.get_converters.return_value = [mock_converter_class]

    mime = 'application/json'
    converter = Conversion.get_converter(mime)

    mock_is_valid_mime.assert_called_once_with(mime)
    mock_plugin_manager.get_converters.assert_called_once()
    mock_converter_class.supports.assert_called_once_with(mime)
    assert converter is None
