# file lib/ansible/cli/doc.py:847-865
# lines [847, 848, 850, 852, 854, 856, 858, 859, 861, 862, 864, 865]
# branches ['850->852', '850->856', '858->859', '858->861', '861->862', '861->864']

import pytest
from ansible.cli.doc import DocCLI

def test_format_snippet_inventory_plugin_no_yaml_config():
    plugin = 'test_inventory_plugin'
    plugin_type = 'inventory'
    doc = {
        'options': {
            'plugin': True
        }
    }
    
    with pytest.raises(ValueError) as excinfo:
        DocCLI.format_snippet(plugin, plugin_type, doc)
    
    assert 'The test_inventory_plugin inventory plugin does not take YAML type config source' in str(excinfo.value)

def test_format_snippet_lookup_plugin(mocker):
    plugin = 'test_lookup_plugin'
    plugin_type = 'lookup'
    doc = {
        'options': {
            'some_option': 'some_value'
        }
    }
    
    mocker.patch('ansible.cli.doc._do_lookup_snippet', return_value=['lookup_snippet'])
    
    result = DocCLI.format_snippet(plugin, plugin_type, doc)
    
    assert result == 'lookup_snippet\n'

def test_format_snippet_with_options(mocker):
    plugin = 'test_plugin'
    plugin_type = 'other'
    doc = {
        'options': {
            'some_option': 'some_value'
        }
    }
    
    mocker.patch('ansible.cli.doc._do_yaml_snippet', return_value=['yaml_snippet'])
    
    result = DocCLI.format_snippet(plugin, plugin_type, doc)
    
    assert result == 'yaml_snippet\n'
