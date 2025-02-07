# file: lib/ansible/cli/doc.py:614-642
# asked: {"lines": [614, 616, 619, 620, 623, 624, 625, 626, 627, 628, 629, 630, 631, 632, 634, 636, 638, 640, 642], "branches": [[619, 620], [619, 623], [624, 625], [624, 642], [636, 638], [636, 640]]}
# gained: {"lines": [614, 616, 619, 620, 623, 624, 625, 626, 627, 628, 629, 630, 631, 632, 634, 636, 638, 640, 642], "branches": [[619, 620], [619, 623], [624, 625], [624, 642], [636, 638], [636, 640]]}

import pytest
from unittest.mock import patch, MagicMock
from ansible.cli.doc import DocCLI
from ansible.errors import AnsibleError, AnsibleOptionsError
from ansible import context

@pytest.fixture
def mock_context_args():
    context.CLIARGS = {'args': ['test_plugin'], 'verbosity': 0}
    yield
    context.CLIARGS = {}

def test_get_plugins_docs_no_args(mock_context_args):
    context.CLIARGS['args'] = []
    with pytest.raises(AnsibleOptionsError, match="Incorrect options passed"):
        DocCLI(['test'])._get_plugins_docs('module', MagicMock())

def test_get_plugins_docs_plugin_not_found(mock_context_args):
    loader = MagicMock()
    loader.find_plugin_with_context.return_value.resolved = False
    with patch('ansible.cli.doc.display') as mock_display:
        result = DocCLI(['test'])._get_plugins_docs('module', loader)
        assert result == {}
        mock_display.warning.assert_called_once_with('module test_plugin not found in:\n\n')

def test_get_plugins_docs_plugin_doc_exception(mock_context_args):
    loader = MagicMock()
    loader.find_plugin_with_context.side_effect = Exception("Test Exception")
    with patch('ansible.cli.doc.display') as mock_display:
        with pytest.raises(AnsibleError, match="module test_plugin missing documentation"):
            DocCLI(['test'])._get_plugins_docs('module', loader)
        mock_display.vvv.assert_called_once()

def test_get_plugins_docs_no_doc(mock_context_args):
    loader = MagicMock()
    loader.find_plugin_with_context.return_value.resolved = True
    with patch('ansible.cli.doc.DocCLI._get_plugin_doc', return_value=(None, None, None, None)):
        result = DocCLI(['test'])._get_plugins_docs('module', loader)
        assert result == {}

def test_get_plugins_docs_success(mock_context_args):
    loader = MagicMock()
    loader.find_plugin_with_context.return_value.resolved = True
    with patch('ansible.cli.doc.DocCLI._get_plugin_doc', return_value=({'doc': 'test'}, 'examples', 'return', 'metadata')):
        with patch('ansible.cli.doc.DocCLI._combine_plugin_doc', return_value={'combined': 'doc'}):
            result = DocCLI(['test'])._get_plugins_docs('module', loader)
            assert result == {'test_plugin': {'combined': 'doc'}}
