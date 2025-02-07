# file: lib/ansible/cli/doc.py:813-832
# asked: {"lines": [819, 820, 822, 823, 824, 827, 828, 830, 831, 832], "branches": [[817, 819], [827, 828], [827, 830]]}
# gained: {"lines": [819, 820, 822, 823, 824, 827, 828, 830, 831, 832], "branches": [[817, 819], [827, 828], [827, 830]]}

import pytest
from unittest.mock import MagicMock, patch
from ansible.cli.doc import DocCLI, PluginNotFound
from ansible.plugins.loader import fragment_loader
from ansible.utils.plugin_docs import get_docstring
from ansible import context

@pytest.fixture
def mock_loader():
    return MagicMock()

@pytest.fixture
def mock_result():
    mock = MagicMock()
    mock.resolved = True
    mock.plugin_resolved_path = 'fake_path'
    mock.plugin_resolved_collection = 'fake_collection'
    return mock

@pytest.fixture(autouse=True)
def mock_context(mocker):
    mocker.patch('ansible.context.CLIARGS', {'verbosity': 0})

def test_get_plugin_doc_success(mock_loader, mock_result):
    mock_loader.find_plugin_with_context.return_value = mock_result
    with patch('ansible.cli.doc.get_docstring', return_value=({}, None, None, None)) as mock_get_docstring:
        doc, plainexamples, returndocs, metadata = DocCLI._get_plugin_doc('fake_plugin', 'module', mock_loader, ['fake_path'])
        assert doc['filename'] == 'fake_path'
        assert doc['collection'] == 'fake_collection'
        mock_get_docstring.assert_called_once_with('fake_path', fragment_loader, verbose=False, collection_name='fake_collection', is_module=True)

def test_get_plugin_doc_not_found(mock_loader):
    result = MagicMock()
    result.resolved = False
    mock_loader.find_plugin_with_context.return_value = result
    with pytest.raises(PluginNotFound):
        DocCLI._get_plugin_doc('fake_plugin', 'module', mock_loader, ['fake_path'])

def test_get_plugin_doc_no_documentation(mock_loader, mock_result):
    mock_loader.find_plugin_with_context.return_value = mock_result
    with patch('ansible.cli.doc.get_docstring', return_value=(None, None, None, None)):
        with pytest.raises(ValueError, match='fake_plugin did not contain a DOCUMENTATION attribute'):
            DocCLI._get_plugin_doc('fake_plugin', 'module', mock_loader, ['fake_path'])
