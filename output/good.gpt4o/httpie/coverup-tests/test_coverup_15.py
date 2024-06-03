# file httpie/plugins/base.py:115-148
# lines [115, 116, 120, 122, 129, 130, 131, 133, 139, 141, 148]
# branches []

import pytest
from httpie.plugins.base import FormatterPlugin

def test_formatter_plugin_initialization():
    format_options = {'option1': 'value1'}
    plugin = FormatterPlugin(format_options=format_options)
    
    assert plugin.enabled is True
    assert plugin.kwargs['format_options'] == format_options
    assert plugin.format_options == format_options

def test_formatter_plugin_format_headers():
    plugin = FormatterPlugin(format_options={})
    headers = "Content-Type: application/json"
    formatted_headers = plugin.format_headers(headers)
    
    assert formatted_headers == headers

def test_formatter_plugin_format_body():
    plugin = FormatterPlugin(format_options={})
    content = '{"key": "value"}'
    mime = 'application/json'
    formatted_body = plugin.format_body(content, mime)
    
    assert formatted_body == content

@pytest.fixture(autouse=True)
def cleanup(mocker):
    yield
    mocker.stopall()
