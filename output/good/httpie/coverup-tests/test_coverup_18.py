# file httpie/plugins/base.py:94-112
# lines [94, 95, 104, 105, 107, 108, 110, 111, 112]
# branches []

import pytest
from httpie.plugins.base import ConverterPlugin

class DummyConverterPlugin(ConverterPlugin):
    @classmethod
    def supports(cls, mime):
        return mime == 'application/dummy'

def test_converter_plugin_supports(mocker):
    mime_type = 'application/dummy'
    assert DummyConverterPlugin.supports(mime_type) is True

    mime_type = 'application/other'
    assert DummyConverterPlugin.supports(mime_type) is False

def test_converter_plugin_convert_not_implemented():
    plugin = DummyConverterPlugin('application/dummy')
    with pytest.raises(NotImplementedError):
        plugin.convert(b'some content')

def test_converter_plugin_init():
    mime_type = 'application/dummy'
    plugin = DummyConverterPlugin(mime_type)
    assert plugin.mime == mime_type
