# file lib/ansible/cli/doc.py:762-770
# lines [762, 763, 764, 765, 766, 767, 768, 769, 770]
# branches ['767->768', '767->770']

import pytest
from unittest import mock
from ansible.cli.doc import DocCLI

@pytest.fixture
def mock_plugin_loader(mocker):
    mock_loader = mocker.patch('ansible.cli.doc.plugin_loader')
    mock_loader.some_loader._get_paths_with_context.return_value = [
        mock.Mock(path='path1', internal=False),
        mock.Mock(path='path2', internal=True)
    ]
    return mock_loader

def test_get_all_plugins_of_type(mock_plugin_loader, mocker):
    mocker.patch('ansible.cli.doc.DocCLI.find_plugins', side_effect=lambda path, internal, plugin_type: {f'{plugin_type}_plugin_{path}'})
    
    result = DocCLI.get_all_plugins_of_type('some')
    
    assert result == ['some_plugin_path1', 'some_plugin_path2']
    mock_plugin_loader.some_loader._get_paths_with_context.assert_called_once()
    DocCLI.find_plugins.assert_any_call('path1', False, 'some')
    DocCLI.find_plugins.assert_any_call('path2', True, 'some')
