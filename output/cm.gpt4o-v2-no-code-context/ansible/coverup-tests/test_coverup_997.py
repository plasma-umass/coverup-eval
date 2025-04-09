# file: lib/ansible/cli/doc.py:834-845
# asked: {"lines": [837, 839, 840, 842, 845], "branches": [[837, 839], [837, 845], [839, 840], [839, 842]]}
# gained: {"lines": [837, 839, 840, 842, 845], "branches": [[837, 839], [837, 845], [839, 840], [839, 842]]}

import pytest
from unittest.mock import patch, MagicMock

# Assuming the DocCLI class is imported from ansible.cli.doc
from ansible.cli.doc import DocCLI

@pytest.fixture
def mock_action_loader(monkeypatch):
    action_loader = MagicMock()
    monkeypatch.setattr('ansible.cli.doc.action_loader', action_loader)
    return action_loader

def test_combine_plugin_doc_with_module_and_action(mock_action_loader):
    mock_action_loader.__contains__.side_effect = lambda x: x == 'test_plugin'
    
    plugin = 'test_plugin'
    plugin_type = 'module'
    doc = {}
    plainexamples = 'example'
    returndocs = 'return'
    metadata = 'metadata'
    
    result = DocCLI._combine_plugin_doc(plugin, plugin_type, doc, plainexamples, returndocs, metadata)
    
    assert result['doc']['has_action'] is True
    assert result['examples'] == plainexamples
    assert result['return'] == returndocs
    assert result['metadata'] == metadata

def test_combine_plugin_doc_with_module_and_no_action(mock_action_loader):
    mock_action_loader.__contains__.side_effect = lambda x: False
    
    plugin = 'test_plugin'
    plugin_type = 'module'
    doc = {}
    plainexamples = 'example'
    returndocs = 'return'
    metadata = 'metadata'
    
    result = DocCLI._combine_plugin_doc(plugin, plugin_type, doc, plainexamples, returndocs, metadata)
    
    assert result['doc']['has_action'] is False
    assert result['examples'] == plainexamples
    assert result['return'] == returndocs
    assert result['metadata'] == metadata

def test_combine_plugin_doc_with_non_module(mock_action_loader):
    plugin = 'test_plugin'
    plugin_type = 'other'
    doc = {}
    plainexamples = 'example'
    returndocs = 'return'
    metadata = 'metadata'
    
    result = DocCLI._combine_plugin_doc(plugin, plugin_type, doc, plainexamples, returndocs, metadata)
    
    assert 'has_action' not in result['doc']
    assert result['examples'] == plainexamples
    assert result['return'] == returndocs
    assert result['metadata'] == metadata
