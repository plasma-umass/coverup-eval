# file: httpie/plugins/base.py:115-148
# asked: {"lines": [115, 116, 120, 122, 129, 130, 131, 133, 139, 141, 148], "branches": []}
# gained: {"lines": [115, 116, 120, 122, 133, 141], "branches": []}

import pytest
from httpie.plugins.base import BasePlugin

class TestFormatterPlugin:
    @pytest.fixture
    def formatter_plugin(self):
        class FormatterPlugin(BasePlugin):
            group_name = 'format'

            def __init__(self, **kwargs):
                self.enabled = True
                self.kwargs = kwargs
                self.format_options = kwargs['format_options']

            def format_headers(self, headers: str) -> str:
                return headers

            def format_body(self, content: str, mime: str) -> str:
                return content

        return FormatterPlugin(format_options={'option1': 'value1'})

    def test_init(self, formatter_plugin):
        assert formatter_plugin.enabled is True
        assert formatter_plugin.kwargs == {'format_options': {'option1': 'value1'}}
        assert formatter_plugin.format_options == {'option1': 'value1'}

    def test_format_headers(self, formatter_plugin):
        headers = "Content-Type: application/json"
        formatted_headers = formatter_plugin.format_headers(headers)
        assert formatted_headers == headers

    def test_format_body(self, formatter_plugin):
        content = '{"key": "value"}'
        mime = "application/json"
        formatted_body = formatter_plugin.format_body(content, mime)
        assert formatted_body == content
