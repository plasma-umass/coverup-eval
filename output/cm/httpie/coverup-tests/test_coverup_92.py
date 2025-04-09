# file httpie/output/processing.py:26-53
# lines [36, 37, 38, 39, 40, 41, 42, 45, 46, 47, 50, 51, 52, 53]
# branches ['38->exit', '38->39', '39->38', '39->40', '41->39', '41->42', '45->46', '45->47', '50->51', '50->53', '51->52', '51->53']

import pytest
from httpie.output.processing import Formatting
from httpie.plugins import FormatterPlugin
from httpie.context import Environment

class MockFormatterPlugin(FormatterPlugin):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.enabled = True

    def format_headers(self, headers):
        return 'Formatted Headers'

    def format_body(self, content, mime):
        return 'Formatted Body'

@pytest.fixture
def mock_plugin_manager(mocker):
    mock_manager = mocker.patch('httpie.output.processing.plugin_manager')
    mock_manager.get_formatters_grouped.return_value = {
        'mock_group': [MockFormatterPlugin]
    }
    return mock_manager

@pytest.fixture
def mock_is_valid_mime(mocker):
    mocker.patch('httpie.output.processing.is_valid_mime', return_value=True)

def test_formatting_with_mocked_plugins(mock_plugin_manager, mock_is_valid_mime):
    env = Environment()
    formatting = Formatting(groups=['mock_group'], env=env, format_options={})
    assert len(formatting.enabled_plugins) == 1

    headers = 'Original Headers'
    formatted_headers = formatting.format_headers(headers)
    assert formatted_headers == 'Formatted Headers'

    content = 'Original Content'
    mime = 'text/plain'
    formatted_body = formatting.format_body(content, mime)
    assert formatted_body == 'Formatted Body'
