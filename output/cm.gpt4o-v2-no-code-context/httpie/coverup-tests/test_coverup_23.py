# file: httpie/plugins/base.py:94-112
# asked: {"lines": [94, 95, 104, 105, 107, 108, 110, 111, 112], "branches": []}
# gained: {"lines": [94, 95, 104, 107, 110, 111], "branches": []}

import pytest
from httpie.plugins.base import BasePlugin

class TestConverterPlugin:
    def test_converter_plugin_init(self):
        class ConverterPlugin(BasePlugin):
            def __init__(self, mime):
                self.mime = mime

            def convert(self, content_bytes):
                raise NotImplementedError

            @classmethod
            def supports(cls, mime):
                raise NotImplementedError

        mime_type = 'application/json'
        plugin = ConverterPlugin(mime_type)
        assert plugin.mime == mime_type

    def test_converter_plugin_convert(self):
        class ConverterPlugin(BasePlugin):
            def __init__(self, mime):
                self.mime = mime

            def convert(self, content_bytes):
                raise NotImplementedError

            @classmethod
            def supports(cls, mime):
                raise NotImplementedError

        plugin = ConverterPlugin('application/json')
        with pytest.raises(NotImplementedError):
            plugin.convert(b'some content')

    def test_converter_plugin_supports(self):
        class ConverterPlugin(BasePlugin):
            def __init__(self, mime):
                self.mime = mime

            def convert(self, content_bytes):
                raise NotImplementedError

            @classmethod
            def supports(cls, mime):
                raise NotImplementedError

        with pytest.raises(NotImplementedError):
            ConverterPlugin.supports('application/json')
