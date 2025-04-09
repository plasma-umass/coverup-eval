# file: httpie/plugins/base.py:115-148
# asked: {"lines": [115, 116, 120, 122, 129, 130, 131, 133, 139, 141, 148], "branches": []}
# gained: {"lines": [115, 116, 120, 122, 129, 130, 131, 133, 139, 141, 148], "branches": []}

import pytest
from httpie.plugins.base import FormatterPlugin

@pytest.fixture
def formatter_plugin():
    return FormatterPlugin(format_options={'option1': 'value1'})

def test_formatter_plugin_initialization(formatter_plugin):
    assert formatter_plugin.enabled is True
    assert formatter_plugin.kwargs == {'format_options': {'option1': 'value1'}}
    assert formatter_plugin.format_options == {'option1': 'value1'}

def test_format_headers(formatter_plugin):
    headers = "Content-Type: application/json"
    formatted_headers = formatter_plugin.format_headers(headers)
    assert formatted_headers == headers

def test_format_body(formatter_plugin):
    content = '{"key": "value"}'
    mime = "application/json"
    formatted_content = formatter_plugin.format_body(content, mime)
    assert formatted_content == content
