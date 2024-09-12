# file: httpie/plugins/base.py:94-112
# asked: {"lines": [94, 95, 104, 105, 107, 108, 110, 111, 112], "branches": []}
# gained: {"lines": [94, 95, 104, 105, 107, 108, 110, 111, 112], "branches": []}

import pytest
from httpie.plugins.base import ConverterPlugin

class TestConverterPlugin:
    
    def test_init(self):
        mime = 'application/json'
        plugin = ConverterPlugin(mime)
        assert plugin.mime == mime

    def test_convert_not_implemented(self):
        plugin = ConverterPlugin('application/json')
        with pytest.raises(NotImplementedError):
            plugin.convert(b'some content')

    def test_supports_not_implemented(self):
        with pytest.raises(NotImplementedError):
            ConverterPlugin.supports('application/json')
