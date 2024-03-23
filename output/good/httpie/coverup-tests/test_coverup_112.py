# file httpie/output/processing.py:16-23
# lines []
# branches ['20->exit', '21->exit', '22->21']

import pytest
from httpie.output.processing import Conversion
from httpie.plugins.base import ConverterPlugin
from unittest.mock import MagicMock


class MockConverter(ConverterPlugin):
    supported_mimes = {'application/mock'}

    def __init__(self, mime: str):
        self.mime = mime

    @classmethod
    def supports(cls, mime: str) -> bool:
        return mime in cls.supported_mimes

    def convert(self, body: bytes) -> bytes:
        return body


@pytest.fixture
def mock_plugin_manager(mocker):
    mocker.patch('httpie.plugins.registry.plugin_manager.get_converters', return_value=[MockConverter])
    yield


@pytest.fixture
def mock_is_valid_mime(mocker):
    mocker.patch('httpie.output.processing.is_valid_mime', side_effect=[False, True, True])
    yield


def test_get_converter_executes_missing_branches(mock_plugin_manager, mock_is_valid_mime):
    # Test the branch where is_valid_mime returns False
    invalid_mime_type = 'application/invalid'
    converter = Conversion.get_converter(invalid_mime_type)
    assert converter is None

    # Test the branch where is_valid_mime returns True but no converter supports the mime
    unsupported_mime_type = 'application/unsupported'
    converter = Conversion.get_converter(unsupported_mime_type)
    assert converter is None

    # Test the branch where is_valid_mime returns True and a converter supports the mime
    supported_mime_type = 'application/mock'
    converter = Conversion.get_converter(supported_mime_type)
    assert isinstance(converter, MockConverter)
    assert converter.mime == supported_mime_type
