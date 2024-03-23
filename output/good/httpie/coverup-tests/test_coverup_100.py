# file httpie/plugins/base.py:94-112
# lines [112]
# branches []

import pytest
from httpie.plugins.base import ConverterPlugin

class DummyConverterPlugin(ConverterPlugin):
    def convert(self, content_bytes):
        return content_bytes

def test_converter_plugin_supports_method(mocker):
    with pytest.raises(NotImplementedError):
        DummyConverterPlugin.supports('application/json')

    # Ensure that the NotImplementedError is raised from the base class
    assert DummyConverterPlugin.supports.__func__ is ConverterPlugin.supports.__func__
