# file lib/ansible/cli/doc.py:585-612
# lines []
# branches ['589->592', '605->612', '609->607']

import pytest
from unittest.mock import MagicMock, patch
from ansible.cli.doc import DocCLI
from ansible.plugins.loader import PluginLoader

@pytest.fixture
def mock_context(mocker):
    context_mock = mocker.patch('ansible.cli.doc.context')
    context_mock.CLIARGS = {
        'args': [''],
        'list_dir': False,
        'list_files': False,
        'dump': True
    }
    return context_mock

@pytest.fixture
def mock_loader():
    return MagicMock(spec=PluginLoader)

@pytest.fixture
def doc_cli():
    return DocCLI(['ansible-doc'])

def test_list_plugins_with_dump(mock_context, mock_loader, doc_cli):
    mock_loader._get_paths_with_context.return_value = []
    mock_context.CLIARGS['args'] = ['']
    mock_context.CLIARGS['dump'] = True

    with patch.object(DocCLI, 'get_all_plugins_of_type', return_value=['plugin1', 'plugin2']), \
         patch.object(DocCLI, 'get_plugin_metadata', side_effect=[{'name': 'plugin1'}, None]):
        
        results = doc_cli._list_plugins('plugin_type', mock_loader)
        
        assert 'plugin1' in results
        assert results['plugin1'] == {'name': 'plugin1'}
        assert 'plugin2' not in results
