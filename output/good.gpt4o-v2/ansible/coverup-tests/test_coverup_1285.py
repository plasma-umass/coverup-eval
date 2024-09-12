# file: lib/ansible/cli/doc.py:847-865
# asked: {"lines": [], "branches": [[861, 864]]}
# gained: {"lines": [], "branches": [[861, 864]]}

import pytest
from ansible.cli.doc import DocCLI

def test_format_snippet_yaml():
    doc = {
        'options': {
            'option1': {
                'description': 'This is a description',
                'required': True
            }
        },
        'short_description': 'A short description',
        'module': 'test_module'
    }
    plugin = 'test_plugin'
    plugin_type = 'test_type'
    
    result = DocCLI.format_snippet(plugin, plugin_type, doc)
    
    assert result.startswith('- name: A short description')
    assert 'option1:' in result
    assert '(required) This is a description' in result
    assert result.endswith('\n')

def test_format_snippet_inventory():
    doc = {
        'options': {
            'plugin': 'some_plugin'
        }
    }
    plugin = 'test_plugin'
    plugin_type = 'inventory'
    
    with pytest.raises(ValueError, match='The test_plugin inventory plugin does not take YAML type config source'):
        DocCLI.format_snippet(plugin, plugin_type, doc)

def test_format_snippet_no_options():
    doc = {
        'short_description': 'A short description',
        'module': 'test_module'
    }
    plugin = 'test_plugin'
    plugin_type = 'test_type'
    
    result = DocCLI.format_snippet(plugin, plugin_type, doc)
    
    assert result == ''
