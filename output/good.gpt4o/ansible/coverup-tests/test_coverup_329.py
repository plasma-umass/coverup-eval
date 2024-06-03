# file lib/ansible/utils/collection_loader/_collection_finder.py:825-842
# lines [825, 826, 832, 834, 836, 837, 839, 840, 842]
# branches ['836->837', '836->839', '839->840', '839->842']

import pytest
from ansible.utils.collection_loader._collection_finder import AnsibleCollectionRef
from ansible.module_utils._text import to_text, to_native

def test_legacy_plugin_dir_to_plugin_type(mocker):
    # Mock the VALID_REF_TYPES to control the test environment
    mocker.patch.object(AnsibleCollectionRef, 'VALID_REF_TYPES', ['action', 'modules', 'role'])

    # Test case for 'action_plugins'
    assert AnsibleCollectionRef.legacy_plugin_dir_to_plugin_type('action_plugins') == 'action'

    # Test case for 'library'
    assert AnsibleCollectionRef.legacy_plugin_dir_to_plugin_type('library') == 'modules'

    # Test case for 'role_plugins'
    assert AnsibleCollectionRef.legacy_plugin_dir_to_plugin_type('role_plugins') == 'role'

    # Test case for invalid plugin type
    with pytest.raises(ValueError, match='invalid_plugins cannot be mapped to a valid collection ref type'):
        AnsibleCollectionRef.legacy_plugin_dir_to_plugin_type('invalid_plugins')
