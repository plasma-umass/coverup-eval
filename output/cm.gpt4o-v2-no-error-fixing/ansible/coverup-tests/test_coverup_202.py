# file: lib/ansible/utils/collection_loader/_collection_finder.py:825-842
# asked: {"lines": [825, 826, 832, 834, 836, 837, 839, 840, 842], "branches": [[836, 837], [836, 839], [839, 840], [839, 842]]}
# gained: {"lines": [825, 826, 832, 834, 836, 837, 839, 840, 842], "branches": [[836, 837], [836, 839], [839, 840], [839, 842]]}

import pytest
from ansible.utils.collection_loader._collection_finder import AnsibleCollectionRef
from ansible.module_utils.common.text.converters import to_native, to_text

def test_legacy_plugin_dir_to_plugin_type_action_plugins():
    result = AnsibleCollectionRef.legacy_plugin_dir_to_plugin_type('action_plugins')
    assert result == 'action'

def test_legacy_plugin_dir_to_plugin_type_library():
    result = AnsibleCollectionRef.legacy_plugin_dir_to_plugin_type('library')
    assert result == 'modules'

def test_legacy_plugin_dir_to_plugin_type_invalid():
    with pytest.raises(ValueError, match="invalid_plugins cannot be mapped to a valid collection ref type"):
        AnsibleCollectionRef.legacy_plugin_dir_to_plugin_type('invalid_plugins')

def test_legacy_plugin_dir_to_plugin_type_valid_types():
    valid_types = ['action_plugins', 'become_plugins', 'cache_plugins', 'callback_plugins', 'cliconf_plugins', 
                   'connection_plugins', 'doc_fragments', 'filter_plugins', 'httpapi_plugins', 'inventory_plugins', 
                   'lookup_plugins', 'module_utils', 'netconf_plugins', 'role', 'shell_plugins', 'strategy_plugins', 
                   'terminal_plugins', 'test_plugins', 'vars_plugins', 'playbook']
    for plugin_dir in valid_types:
        plugin_type = plugin_dir.replace('_plugins', '')
        if plugin_type == 'library':
            plugin_type = 'modules'
        result = AnsibleCollectionRef.legacy_plugin_dir_to_plugin_type(plugin_dir)
        assert result == plugin_type
