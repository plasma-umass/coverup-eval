# file: lib/ansible/cli/doc.py:834-845
# asked: {"lines": [837, 839, 840, 842, 845], "branches": [[837, 839], [837, 845], [839, 840], [839, 842]]}
# gained: {"lines": [837, 839, 840, 842, 845], "branches": [[837, 839], [837, 845], [839, 840], [839, 842]]}

import pytest
from ansible.cli.doc import DocCLI
from ansible.plugins.loader import action_loader

@pytest.fixture
def mock_action_loader(monkeypatch):
    class MockActionLoader:
        def __contains__(self, item):
            return item == "test_plugin_with_action"
    
    monkeypatch.setattr(action_loader.__class__, "__contains__", MockActionLoader().__contains__)

def test_combine_plugin_doc_with_action(mock_action_loader):
    plugin = "test_plugin_with_action"
    plugin_type = "module"
    doc = {}
    plainexamples = "example"
    returndocs = "return"
    metadata = "metadata"
    
    result = DocCLI._combine_plugin_doc(plugin, plugin_type, doc, plainexamples, returndocs, metadata)
    
    assert result["doc"]["has_action"] == True
    assert result["examples"] == plainexamples
    assert result["return"] == returndocs
    assert result["metadata"] == metadata

def test_combine_plugin_doc_without_action(mock_action_loader):
    plugin = "test_plugin_without_action"
    plugin_type = "module"
    doc = {}
    plainexamples = "example"
    returndocs = "return"
    metadata = "metadata"
    
    result = DocCLI._combine_plugin_doc(plugin, plugin_type, doc, plainexamples, returndocs, metadata)
    
    assert result["doc"]["has_action"] == False
    assert result["examples"] == plainexamples
    assert result["return"] == returndocs
    assert result["metadata"] == metadata

def test_combine_plugin_doc_non_module(mock_action_loader):
    plugin = "test_plugin"
    plugin_type = "non_module"
    doc = {}
    plainexamples = "example"
    returndocs = "return"
    metadata = "metadata"
    
    result = DocCLI._combine_plugin_doc(plugin, plugin_type, doc, plainexamples, returndocs, metadata)
    
    assert "has_action" not in result["doc"]
    assert result["examples"] == plainexamples
    assert result["return"] == returndocs
    assert result["metadata"] == metadata
