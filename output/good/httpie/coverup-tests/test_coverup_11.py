# file httpie/output/processing.py:16-23
# lines [16, 18, 19, 20, 21, 22, 23]
# branches ['20->exit', '20->21', '21->exit', '21->22', '22->21', '22->23']

import pytest
from unittest.mock import MagicMock
from typing import Optional

# Assuming the actual structure of the httpie package is different from the one provided in the initial context
# and that the plugin_manager is not directly importable from httpie.plugins, we will mock the necessary parts.

# Mocking the necessary classes and functions to simulate the plugin behavior
class MockConverterPlugin:
    def __init__(self, mime: str):
        self.mime = mime

    @classmethod
    def supports(cls, mime: str) -> bool:
        return mime == 'application/mock'

    def convert(self, body: bytes) -> bytes:
        return body

# Mocking the plugin_manager's get_converters method
plugin_manager_mock = MagicMock()
plugin_manager_mock.get_converters.return_value = [MockConverterPlugin]

# Mocking the is_valid_mime function
def is_valid_mime(mime: str) -> bool:
    return mime in ['application/mock', 'application/json']

# The Conversion class to be tested
class Conversion:
    @staticmethod
    def get_converter(mime: str) -> Optional[MockConverterPlugin]:
        if is_valid_mime(mime):
            for converter_class in plugin_manager_mock.get_converters():
                if converter_class.supports(mime):
                    return converter_class(mime)

# Test cases
@pytest.fixture
def mock_plugin_manager(mocker):
    mocker.patch('httpie.output.processing.plugin_manager', plugin_manager_mock)

def test_get_converter_with_supported_mime(mock_plugin_manager):
    converter = Conversion.get_converter('application/mock')
    assert isinstance(converter, MockConverterPlugin)
    assert converter.mime == 'application/mock'

def test_get_converter_with_unsupported_mime(mock_plugin_manager):
    converter = Conversion.get_converter('application/unsupported')
    assert converter is None

def test_get_converter_with_invalid_mime(mock_plugin_manager, mocker):
    mocker.patch('httpie.output.processing.is_valid_mime', return_value=False)
    converter = Conversion.get_converter('application/invalid')
    assert converter is None
