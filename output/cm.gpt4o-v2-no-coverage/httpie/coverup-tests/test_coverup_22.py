# file: httpie/plugins/base.py:115-148
# asked: {"lines": [115, 116, 120, 122, 129, 130, 131, 133, 139, 141, 148], "branches": []}
# gained: {"lines": [115, 116, 120, 122, 129, 130, 131, 133, 139, 141, 148], "branches": []}

import pytest
from httpie.plugins.base import FormatterPlugin

class MockEnvironment:
    pass

@pytest.fixture
def mock_env():
    return MockEnvironment()

def test_formatter_plugin_init(mock_env):
    kwargs = {'format_options': {'option1': 'value1'}}
    plugin = FormatterPlugin(env=mock_env, **kwargs)
    assert plugin.enabled is True
    assert plugin.kwargs['format_options'] == kwargs['format_options']
    assert plugin.format_options == kwargs['format_options']

def test_formatter_plugin_format_headers():
    plugin = FormatterPlugin(format_options={})
    headers = "Content-Type: application/json"
    assert plugin.format_headers(headers) == headers

def test_formatter_plugin_format_body():
    plugin = FormatterPlugin(format_options={})
    content = '{"key": "value"}'
    mime = "application/json"
    assert plugin.format_body(content, mime) == content
