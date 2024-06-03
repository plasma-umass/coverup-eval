# file lib/ansible/cli/doc.py:585-612
# lines [595]
# branches ['589->592', '594->595', '605->612', '609->607']

import pytest
from unittest.mock import MagicMock, patch

@pytest.fixture
def mock_context(mocker):
    context = mocker.patch('ansible.cli.doc.context')
    context.CLIARGS = {
        'args': [''],
        'list_dir': False,
        'list_files': False,
        'dump': True
    }
    return context

@pytest.fixture
def mock_loader(mocker):
    loader = mocker.MagicMock()
    loader._get_paths_with_context.return_value = [MagicMock(path='path1', internal=True)]
    return loader

@pytest.fixture
def doc_cli_instance(mocker, mock_context):
    from ansible.cli.doc import DocCLI
    instance = DocCLI(['ansible-doc'])
    instance.plugin_list = {}
    return instance

def test_list_plugins_full_coverage(doc_cli_instance, mock_loader, mock_context):
    from ansible.cli.doc import DocCLI

    # Mock the methods called within _list_plugins
    with patch.object(DocCLI, 'find_plugins', return_value={'plugin1': 'data1'}), \
         patch.object(DocCLI, 'get_all_plugins_of_type', return_value=['plugin1']), \
         patch.object(DocCLI, 'get_plugin_metadata', return_value={'name': 'plugin1', 'data': 'metadata'}), \
         patch('ansible.cli.doc.add_collection_plugins'):

        results = doc_cli_instance._list_plugins('plugin_type', mock_loader)

        # Assertions to verify the correct execution of the code
        assert 'plugin1' in results
        assert results['plugin1'] == {'name': 'plugin1', 'data': 'metadata'}
        mock_loader._get_paths_with_context.assert_called_once()
        DocCLI.find_plugins.assert_called_once_with('path1', True, 'plugin_type')
        DocCLI.get_all_plugins_of_type.assert_called_once_with('plugin_type')
        DocCLI.get_plugin_metadata.assert_called_once_with('plugin_type', 'plugin1')
