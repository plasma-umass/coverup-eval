# file: lib/ansible/cli/doc.py:867-888
# asked: {"lines": [867, 868, 869, 878, 879, 880, 882, 883, 884, 885, 886, 888], "branches": []}
# gained: {"lines": [867, 868, 869, 878, 879, 880, 882, 883, 884, 885, 886, 888], "branches": []}

import pytest
from unittest.mock import patch, MagicMock
from ansible.errors import AnsibleError
from ansible.cli.doc import DocCLI

@pytest.fixture
def mock_display():
    with patch('ansible.cli.doc.display') as mock_display:
        yield mock_display

@pytest.fixture
def mock_get_man_text():
    with patch.object(DocCLI, 'get_man_text') as mock_get_man_text:
        yield mock_get_man_text

def test_format_plugin_doc_success(mock_display, mock_get_man_text):
    mock_get_man_text.return_value = "Formatted text"
    plugin = "test_plugin"
    plugin_type = "module"
    doc = {
        'collection': 'test_collection',
        'description': 'Test description'
    }
    plainexamples = "Example"
    returndocs = "Return docs"
    metadata = "Metadata"

    result = DocCLI.format_plugin_doc(plugin, plugin_type, doc, plainexamples, returndocs, metadata)

    assert result == "Formatted text"
    assert doc['plainexamples'] == plainexamples
    assert doc['returndocs'] == returndocs
    assert doc['metadata'] == metadata
    mock_get_man_text.assert_called_once_with(doc, 'test_collection', 'module')

def test_format_plugin_doc_exception(mock_display, mock_get_man_text):
    mock_get_man_text.side_effect = Exception("Test exception")
    plugin = "test_plugin"
    plugin_type = "module"
    doc = {
        'collection': 'test_collection',
        'description': 'Test description'
    }
    plainexamples = "Example"
    returndocs = "Return docs"
    metadata = "Metadata"

    with pytest.raises(AnsibleError, match="Unable to retrieve documentation from 'test_plugin' due to: Test exception"):
        DocCLI.format_plugin_doc(plugin, plugin_type, doc, plainexamples, returndocs, metadata)

    mock_get_man_text.assert_called_once_with(doc, 'test_collection', 'module')
    mock_display.vvv.assert_called_once()
