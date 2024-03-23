# file httpie/output/processing.py:26-53
# lines []
# branches ['41->39', '50->53']

import pytest
from httpie.output.processing import Formatting
from httpie.plugins import FormatterPlugin
from httpie.context import Environment

class DummyFormatter(FormatterPlugin):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.enabled = kwargs.get('force_enable', False)

    def format_headers(self, headers):
        return headers

    def format_body(self, content, mime):
        return content

@pytest.fixture
def mock_plugin_manager(mocker):
    mock_manager = mocker.patch('httpie.output.processing.plugin_manager')
    mock_manager.get_formatters_grouped.return_value = {
        'test_group': [DummyFormatter],
        'empty_group': []
    }
    return mock_manager

def test_formatting_with_disabled_plugin(mock_plugin_manager):
    env = Environment()
    formatting = Formatting(groups=['test_group'], env=env, format_options={})
    assert len(formatting.enabled_plugins) == 0

def test_formatting_with_enabled_plugin(mock_plugin_manager):
    env = Environment()
    formatting = Formatting(groups=['test_group'], env=env, force_enable=True, format_options={})
    assert len(formatting.enabled_plugins) == 1

def test_formatting_with_invalid_mime(mock_plugin_manager):
    env = Environment()
    formatting = Formatting(groups=['test_group'], env=env, force_enable=True, format_options={})
    content = formatting.format_body('content', 'invalid/mime')
    assert content == 'content'

def test_formatting_with_empty_group(mock_plugin_manager):
    env = Environment()
    formatting = Formatting(groups=['empty_group'], env=env, format_options={})
    assert len(formatting.enabled_plugins) == 0
