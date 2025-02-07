# file: httpie/plugins/base.py:115-148
# asked: {"lines": [115, 116, 120, 122, 129, 130, 131, 133, 139, 141, 148], "branches": []}
# gained: {"lines": [115, 116, 120, 122, 129, 130, 131, 133, 139, 141, 148], "branches": []}

import pytest
from httpie.plugins.base import FormatterPlugin

def test_formatter_plugin_init():
    kwargs = {'format_options': 'some_option'}
    plugin = FormatterPlugin(**kwargs)
    assert plugin.enabled is True
    assert plugin.kwargs == kwargs
    assert plugin.format_options == 'some_option'

def test_formatter_plugin_format_headers():
    plugin = FormatterPlugin(format_options='some_option')
    headers = "Content-Type: application/json"
    formatted_headers = plugin.format_headers(headers)
    assert formatted_headers == headers

def test_formatter_plugin_format_body():
    plugin = FormatterPlugin(format_options='some_option')
    content = '{"key": "value"}'
    mime = "application/json"
    formatted_content = plugin.format_body(content, mime)
    assert formatted_content == content
