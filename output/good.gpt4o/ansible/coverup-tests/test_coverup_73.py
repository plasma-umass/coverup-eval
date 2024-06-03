# file lib/ansible/cli/doc.py:585-612
# lines [585, 587, 588, 589, 590, 592, 593, 594, 595, 597, 600, 601, 602, 603, 605, 606, 607, 608, 609, 610, 612]
# branches ['589->590', '589->592', '592->593', '592->597', '594->595', '594->597', '600->601', '600->602', '602->603', '602->605', '605->606', '605->612', '607->608', '607->612', '609->607', '609->610']

import pytest
from unittest.mock import MagicMock, patch
from ansible.cli.doc import DocCLI
from ansible.plugins.loader import PluginLoader
from ansible import context

@pytest.fixture
def mock_context(mocker):
    context.CLIARGS = {
        'args': [],
        'list_dir': False,
        'list_files': False,
        'dump': False
    }
    yield
    context.CLIARGS = {}

@pytest.fixture
def doc_cli(mocker):
    mock_args = mocker.MagicMock()
    return DocCLI(mock_args)

def test_list_plugins_with_coll_filter(mock_context, doc_cli, mocker):
    mock_loader = mocker.create_autospec(PluginLoader)
    mock_loader._get_paths_with_context.return_value = []

    context.CLIARGS['args'] = ['some_filter']
    context.CLIARGS['list_dir'] = True

    with patch.object(DocCLI, 'find_plugins', return_value={}), \
         patch('ansible.cli.doc.add_collection_plugins', return_value=None), \
         patch.object(DocCLI, '_get_plugin_list_descriptions', return_value={'plugin1': 'description1'}):
        results = doc_cli._list_plugins('plugin_type', mock_loader)
        assert results == {'plugin1': 'description1'}

def test_list_plugins_without_coll_filter(mock_context, doc_cli, mocker):
    mock_loader = mocker.create_autospec(PluginLoader)
    mock_loader._get_paths_with_context.return_value = []

    context.CLIARGS['args'] = ['']
    context.CLIARGS['list_files'] = True

    with patch.object(DocCLI, 'find_plugins', return_value={}), \
         patch('ansible.cli.doc.add_collection_plugins', return_value=None), \
         patch.object(DocCLI, '_get_plugin_list_filenames', return_value={'plugin1': 'filename1'}):
        results = doc_cli._list_plugins('plugin_type', mock_loader)
        assert results == {'plugin1': 'filename1'}

def test_list_plugins_with_dump(mock_context, doc_cli, mocker):
    mock_loader = mocker.create_autospec(PluginLoader)
    mock_loader._get_paths_with_context.return_value = []

    context.CLIARGS['args'] = ['']
    context.CLIARGS['dump'] = True

    with patch.object(DocCLI, 'find_plugins', return_value={}), \
         patch('ansible.cli.doc.add_collection_plugins', return_value=None), \
         patch.object(DocCLI, 'get_all_plugins_of_type', return_value=['plugin1']), \
         patch.object(DocCLI, 'get_plugin_metadata', return_value={'name': 'plugin1', 'description': 'A plugin'}):
        results = doc_cli._list_plugins('plugin_type', mock_loader)
        assert results == {'plugin1': {'name': 'plugin1', 'description': 'A plugin'}}
