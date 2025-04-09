# file: lib/ansible/cli/doc.py:867-888
# asked: {"lines": [867, 868, 869, 878, 879, 880, 882, 883, 884, 885, 886, 888], "branches": []}
# gained: {"lines": [867, 868, 869, 878, 879, 880, 882, 883, 884, 885, 886, 888], "branches": []}

import pytest
from ansible.cli.doc import DocCLI
from ansible.errors import AnsibleError

def test_format_plugin_doc_success(monkeypatch):
    def mock_get_man_text(doc, collection_name, plugin_type):
        return "Mocked man text"

    monkeypatch.setattr(DocCLI, "get_man_text", mock_get_man_text)

    plugin = "test_plugin"
    plugin_type = "module"
    doc = {
        "collection": "test_collection",
        "description": "Test description"
    }
    plainexamples = "Test examples"
    returndocs = "Test return docs"
    metadata = "Test metadata"

    result = DocCLI.format_plugin_doc(plugin, plugin_type, doc, plainexamples, returndocs, metadata)

    assert result == "Mocked man text"
    assert doc["plainexamples"] == plainexamples
    assert doc["returndocs"] == returndocs
    assert doc["metadata"] == metadata

def test_format_plugin_doc_failure(monkeypatch):
    def mock_get_man_text(doc, collection_name, plugin_type):
        raise Exception("Test exception")

    monkeypatch.setattr(DocCLI, "get_man_text", mock_get_man_text)

    plugin = "test_plugin"
    plugin_type = "module"
    doc = {
        "collection": "test_collection",
        "description": "Test description"
    }
    plainexamples = "Test examples"
    returndocs = "Test return docs"
    metadata = "Test metadata"

    with pytest.raises(AnsibleError) as excinfo:
        DocCLI.format_plugin_doc(plugin, plugin_type, doc, plainexamples, returndocs, metadata)

    assert "Unable to retrieve documentation from 'test_plugin' due to: Test exception" in str(excinfo.value)
