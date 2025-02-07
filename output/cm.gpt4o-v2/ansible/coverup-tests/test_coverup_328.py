# file: lib/ansible/cli/doc.py:867-888
# asked: {"lines": [867, 868, 869, 878, 879, 880, 882, 883, 884, 885, 886, 888], "branches": []}
# gained: {"lines": [867, 868, 869, 878, 879, 880, 882, 883, 884, 885, 886, 888], "branches": []}

import pytest
from unittest.mock import patch, MagicMock
from ansible.errors import AnsibleError
from ansible.cli.doc import DocCLI

@pytest.fixture
def mock_display_vvv():
    with patch('ansible.cli.doc.display.vvv') as mock_vvv:
        yield mock_vvv

@pytest.fixture
def mock_get_man_text():
    with patch.object(DocCLI, 'get_man_text', return_value="man text") as mock_method:
        yield mock_method

def test_format_plugin_doc_success(mock_get_man_text):
    plugin = "test_plugin"
    plugin_type = "module"
    doc = {"collection": "test_collection", "description": "test description"}
    plainexamples = "example"
    returndocs = "return docs"
    metadata = "metadata"

    result = DocCLI.format_plugin_doc(plugin, plugin_type, doc, plainexamples, returndocs, metadata)

    assert result == "man text"
    assert doc['plainexamples'] == plainexamples
    assert doc['returndocs'] == returndocs
    assert doc['metadata'] == metadata
    mock_get_man_text.assert_called_once_with(doc, "test_collection", "module")

def test_format_plugin_doc_exception(mock_display_vvv, mock_get_man_text):
    mock_get_man_text.side_effect = Exception("test exception")
    plugin = "test_plugin"
    plugin_type = "module"
    doc = {"collection": "test_collection", "description": "test description"}
    plainexamples = "example"
    returndocs = "return docs"
    metadata = "metadata"

    with pytest.raises(AnsibleError, match="Unable to retrieve documentation from 'test_plugin' due to: test exception"):
        DocCLI.format_plugin_doc(plugin, plugin_type, doc, plainexamples, returndocs, metadata)

    mock_display_vvv.assert_called_once()
    mock_get_man_text.assert_called_once_with(doc, "test_collection", "module")
