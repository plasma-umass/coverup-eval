# file lib/ansible/utils/collection_loader/_collection_finder.py:825-842
# lines [825, 826, 832, 834, 836, 837, 839, 840, 842]
# branches ['836->837', '836->839', '839->840', '839->842']

import pytest
from ansible.utils.collection_loader._collection_finder import AnsibleCollectionRef
from ansible.module_utils._text import to_text, to_native

def test_legacy_plugin_dir_to_plugin_type_valid():
    # Test with a valid plugin directory name
    plugin_dir_name = 'action_plugins'
    expected_plugin_type = 'action'
    assert AnsibleCollectionRef.legacy_plugin_dir_to_plugin_type(plugin_dir_name) == expected_plugin_type

def test_legacy_plugin_dir_to_plugin_type_library():
    # Test with the 'library' plugin directory name
    plugin_dir_name = 'library'
    expected_plugin_type = 'modules'
    assert AnsibleCollectionRef.legacy_plugin_dir_to_plugin_type(plugin_dir_name) == expected_plugin_type

def test_legacy_plugin_dir_to_plugin_type_invalid():
    # Test with an invalid plugin directory name
    plugin_dir_name = 'invalid_plugins'
    with pytest.raises(ValueError) as excinfo:
        AnsibleCollectionRef.legacy_plugin_dir_to_plugin_type(plugin_dir_name)
    assert str(excinfo.value) == to_native(plugin_dir_name) + ' cannot be mapped to a valid collection ref type'
