# file httpie/plugins/base.py:115-148
# lines [115, 116, 120, 122, 129, 130, 131, 133, 139, 141, 148]
# branches []

import pytest
from httpie.plugins.base import FormatterPlugin

class DummyEnvironment:
    colors = 256

@pytest.fixture
def formatter_plugin_kwargs():
    return {
        'format_options': {
            'option1': 'value1',
            'option2': 'value2'
        }
    }

@pytest.fixture
def formatter_plugin(formatter_plugin_kwargs):
    return FormatterPlugin(**formatter_plugin_kwargs)

def test_formatter_plugin_init(formatter_plugin, formatter_plugin_kwargs):
    assert formatter_plugin.enabled is True
    assert formatter_plugin.kwargs == formatter_plugin_kwargs
    assert formatter_plugin.format_options == formatter_plugin_kwargs['format_options']

def test_formatter_plugin_format_headers(formatter_plugin):
    headers = "Header1: Value1\nHeader2: Value2"
    formatted_headers = formatter_plugin.format_headers(headers)
    assert formatted_headers == headers

def test_formatter_plugin_format_body(formatter_plugin):
    content = "This is the body content."
    mime = "text/plain"
    formatted_content = formatter_plugin.format_body(content, mime)
    assert formatted_content == content
