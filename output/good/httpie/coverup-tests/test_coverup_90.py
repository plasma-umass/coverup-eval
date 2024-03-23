# file httpie/output/processing.py:16-23
# lines [20, 21, 22, 23]
# branches ['20->exit', '20->21', '21->exit', '21->22', '22->21', '22->23']

import pytest
from httpie.output.processing import Conversion
from httpie.plugins.base import ConverterPlugin
from unittest.mock import MagicMock

# Mock plugin that supports a specific mime type
class MockConverterPlugin(ConverterPlugin):
    def __init__(self, mime):
        self.mime = mime

    @classmethod
    def supports(cls, mime: str) -> bool:
        return mime == 'application/mock'

# Test function to cover lines 20-23
def test_get_converter_with_supported_mime(mocker):
    # Mock the is_valid_mime function to return True
    mocker.patch('httpie.output.processing.is_valid_mime', return_value=True)
    # Mock the plugin_manager.get_converters to return a list with our MockConverterPlugin
    mock_plugin_manager = MagicMock()
    mock_plugin_manager.get_converters.return_value = [MockConverterPlugin]
    mocker.patch('httpie.output.processing.plugin_manager', mock_plugin_manager)
    
    # Call the method under test
    converter = Conversion.get_converter('application/mock')
    
    # Assert that the returned converter is an instance of MockConverterPlugin
    assert isinstance(converter, MockConverterPlugin)
    # Assert that the mime type is set correctly
    assert converter.mime == 'application/mock'
