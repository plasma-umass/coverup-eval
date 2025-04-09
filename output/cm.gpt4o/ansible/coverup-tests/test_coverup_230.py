# file lib/ansible/cli/doc.py:813-832
# lines [813, 814, 816, 817, 818, 819, 820, 822, 823, 824, 827, 828, 830, 831, 832]
# branches ['817->818', '817->819', '827->828', '827->830']

import pytest
from unittest.mock import MagicMock, patch
from ansible.cli.doc import DocCLI, PluginNotFound

@pytest.fixture
def mock_loader():
    return MagicMock()

@pytest.fixture
def mock_fragment_loader():
    return MagicMock()

@pytest.fixture
def mock_context(mocker):
    context = mocker.patch('ansible.cli.doc.context')
    context.CLIARGS = {'verbosity': 1}
    return context

@pytest.fixture
def mock_get_docstring(mocker):
    return mocker.patch('ansible.cli.doc.get_docstring')

def test_get_plugin_doc_success(mock_loader, mock_fragment_loader, mock_context, mock_get_docstring):
    plugin = 'test_plugin'
    plugin_type = 'module'
    search_paths = ['/path/to/plugins']
    
    mock_result = MagicMock()
    mock_result.resolved = True
    mock_result.plugin_resolved_path = '/path/to/plugin.py'
    mock_result.plugin_resolved_collection = 'test_collection'
    mock_loader.find_plugin_with_context.return_value = mock_result
    
    mock_get_docstring.return_value = ({'DOCUMENTATION': 'test_doc'}, 'plainexamples', 'returndocs', 'metadata')
    
    doc, plainexamples, returndocs, metadata = DocCLI._get_plugin_doc(plugin, plugin_type, mock_loader, search_paths)
    
    assert doc['filename'] == '/path/to/plugin.py'
    assert doc['collection'] == 'test_collection'
    assert plainexamples == 'plainexamples'
    assert returndocs == 'returndocs'
    assert metadata == 'metadata'

def test_get_plugin_doc_plugin_not_found(mock_loader):
    plugin = 'test_plugin'
    plugin_type = 'module'
    search_paths = ['/path/to/plugins']
    
    mock_result = MagicMock()
    mock_result.resolved = False
    mock_loader.find_plugin_with_context.return_value = mock_result
    
    with pytest.raises(PluginNotFound):
        DocCLI._get_plugin_doc(plugin, plugin_type, mock_loader, search_paths)

def test_get_plugin_doc_no_documentation(mock_loader, mock_fragment_loader, mock_context, mock_get_docstring):
    plugin = 'test_plugin'
    plugin_type = 'module'
    search_paths = ['/path/to/plugins']
    
    mock_result = MagicMock()
    mock_result.resolved = True
    mock_result.plugin_resolved_path = '/path/to/plugin.py'
    mock_result.plugin_resolved_collection = 'test_collection'
    mock_loader.find_plugin_with_context.return_value = mock_result
    
    mock_get_docstring.return_value = (None, 'plainexamples', 'returndocs', 'metadata')
    
    with pytest.raises(ValueError):
        DocCLI._get_plugin_doc(plugin, plugin_type, mock_loader, search_paths)
