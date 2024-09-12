# file: lib/ansible/cli/doc.py:834-845
# asked: {"lines": [837, 839, 840, 842, 845], "branches": [[837, 839], [837, 845], [839, 840], [839, 842]]}
# gained: {"lines": [837, 839, 840, 842, 845], "branches": [[837, 839], [837, 845], [839, 840], [839, 842]]}

import pytest
from unittest.mock import patch

# Assuming the necessary imports for CLI, RoleMixin, and action_loader are done elsewhere
from ansible.cli.doc import DocCLI

@pytest.fixture
def mock_action_loader():
    with patch('ansible.cli.doc.action_loader', new_callable=dict) as mock_loader:
        yield mock_loader

def test_combine_plugin_doc_module_with_action(mock_action_loader):
    mock_action_loader['test_plugin'] = True
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

def test_combine_plugin_doc_module_without_action(mock_action_loader):
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

def test_combine_plugin_doc_non_module(mock_action_loader):
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
