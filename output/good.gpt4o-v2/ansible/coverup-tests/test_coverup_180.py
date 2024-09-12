# file: lib/ansible/cli/doc.py:847-865
# asked: {"lines": [847, 848, 850, 852, 854, 856, 858, 859, 861, 862, 864, 865], "branches": [[850, 852], [850, 856], [858, 859], [858, 861], [861, 862], [861, 864]]}
# gained: {"lines": [847, 848, 850, 852, 854, 856, 858, 859, 861, 862, 864, 865], "branches": [[850, 852], [850, 856], [858, 859], [858, 861], [861, 862]]}

import pytest
from ansible.cli.doc import DocCLI

def test_format_snippet_inventory_plugin():
    with pytest.raises(ValueError, match="The inventory_plugin inventory plugin does not take YAML type config source that can be used with the \"auto\" plugin so a snippet cannot be created."):
        DocCLI.format_snippet('inventory_plugin', 'inventory', {'options': {'plugin': 'some_plugin'}})

def test_format_snippet_lookup_plugin(monkeypatch):
    def mock_do_lookup_snippet(doc):
        return ["lookup_snippet"]
    
    monkeypatch.setattr('ansible.cli.doc._do_lookup_snippet', mock_do_lookup_snippet)
    result = DocCLI.format_snippet('lookup_plugin', 'lookup', {'options': {}})
    assert result == "lookup_snippet\n"

def test_format_snippet_with_options(monkeypatch):
    def mock_do_yaml_snippet(doc):
        return ["yaml_snippet"]
    
    monkeypatch.setattr('ansible.cli.doc._do_yaml_snippet', mock_do_yaml_snippet)
    result = DocCLI.format_snippet('some_plugin', 'some_type', {'options': {}})
    assert result == "yaml_snippet\n"
