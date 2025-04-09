# file: lib/ansible/cli/doc.py:847-865
# asked: {"lines": [847, 848, 850, 852, 854, 856, 858, 859, 861, 862, 864, 865], "branches": [[850, 852], [850, 856], [858, 859], [858, 861], [861, 862], [861, 864]]}
# gained: {"lines": [847, 848, 850, 852, 854, 856, 858, 859, 861, 862, 864, 865], "branches": [[850, 852], [850, 856], [858, 859], [858, 861], [861, 862]]}

import pytest
from ansible.cli.doc import DocCLI

def test_format_snippet_inventory_plugin():
    plugin = 'test_plugin'
    plugin_type = 'inventory'
    doc = {'options': {'plugin': True}}
    
    with pytest.raises(ValueError) as excinfo:
        DocCLI.format_snippet(plugin, plugin_type, doc)
    
    assert 'The test_plugin inventory plugin does not take YAML type config source' in str(excinfo.value)

def test_format_snippet_lookup_plugin(monkeypatch):
    plugin = 'test_plugin'
    plugin_type = 'lookup'
    doc = {'some_key': 'some_value'}
    
    def mock_do_lookup_snippet(doc):
        return ['lookup snippet']
    
    monkeypatch.setattr('ansible.cli.doc._do_lookup_snippet', mock_do_lookup_snippet)
    
    result = DocCLI.format_snippet(plugin, plugin_type, doc)
    
    assert result == 'lookup snippet\n'

def test_format_snippet_with_options(monkeypatch):
    plugin = 'test_plugin'
    plugin_type = 'other'
    doc = {'options': {'some_option': 'some_value'}}
    
    def mock_do_yaml_snippet(doc):
        return ['yaml snippet']
    
    monkeypatch.setattr('ansible.cli.doc._do_yaml_snippet', mock_do_yaml_snippet)
    
    result = DocCLI.format_snippet(plugin, plugin_type, doc)
    
    assert result == 'yaml snippet\n'
