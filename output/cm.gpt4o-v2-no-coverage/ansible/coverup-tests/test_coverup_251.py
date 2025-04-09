# file: lib/ansible/cli/doc.py:847-865
# asked: {"lines": [847, 848, 850, 852, 854, 856, 858, 859, 861, 862, 864, 865], "branches": [[850, 852], [850, 856], [858, 859], [858, 861], [861, 862], [861, 864]]}
# gained: {"lines": [847, 848, 850, 852, 854, 856, 858, 859, 861, 862, 864, 865], "branches": [[850, 852], [850, 856], [858, 859], [858, 861], [861, 862], [861, 864]]}

import pytest
from ansible.cli.doc import DocCLI

def test_format_snippet_inventory_plugin():
    with pytest.raises(ValueError, match="The test_plugin inventory plugin does not take YAML type config source that can be used with the \"auto\" plugin so a snippet cannot be created."):
        DocCLI.format_snippet('test_plugin', 'inventory', {'options': {'plugin': True}})

def test_format_snippet_lookup_plugin(mocker):
    mocker.patch('ansible.cli.doc._do_lookup_snippet', return_value=['lookup snippet'])
    result = DocCLI.format_snippet('test_plugin', 'lookup', {'options': {}})
    assert result == 'lookup snippet\n'

def test_format_snippet_with_options(mocker):
    mocker.patch('ansible.cli.doc._do_yaml_snippet', return_value=['yaml snippet'])
    result = DocCLI.format_snippet('test_plugin', 'other', {'options': {}})
    assert result == 'yaml snippet\n'

def test_format_snippet_no_options():
    result = DocCLI.format_snippet('test_plugin', 'other', {})
    assert result == ''
