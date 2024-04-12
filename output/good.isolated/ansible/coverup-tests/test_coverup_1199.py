# file lib/ansible/cli/doc.py:847-865
# lines [850, 852, 854, 856, 858, 859, 861, 862, 864, 865]
# branches ['850->852', '850->856', '858->859', '858->861', '861->862', '861->864']

import pytest
from ansible.cli.doc import DocCLI

def test_format_snippet_inventory_plugin_raises_value_error(mocker):
    # Mock the _do_lookup_snippet and _do_yaml_snippet functions
    mocker.patch('ansible.cli.doc._do_lookup_snippet')
    mocker.patch('ansible.cli.doc._do_yaml_snippet')

    plugin = 'test_inventory_plugin'
    plugin_type = 'inventory'
    doc = {'options': {'plugin': True}}

    with pytest.raises(ValueError) as excinfo:
        DocCLI.format_snippet(plugin, plugin_type, doc)
    
    assert str(excinfo.value) == ('The test_inventory_plugin inventory plugin does not take YAML type config source'
                                  ' that can be used with the "auto" plugin so a snippet cannot be'
                                  ' created.')
