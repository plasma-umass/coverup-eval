# file: lib/ansible/utils/collection_loader/_collection_finder.py:825-842
# asked: {"lines": [825, 826, 832, 834, 836, 837, 839, 840, 842], "branches": [[836, 837], [836, 839], [839, 840], [839, 842]]}
# gained: {"lines": [825, 826, 832, 834, 836, 837, 839, 840, 842], "branches": [[836, 837], [836, 839], [839, 840], [839, 842]]}

import pytest
from ansible.utils.collection_loader._collection_finder import AnsibleCollectionRef

def test_legacy_plugin_dir_to_plugin_type_valid_action_plugins():
    result = AnsibleCollectionRef.legacy_plugin_dir_to_plugin_type('action_plugins')
    assert result == 'action'

def test_legacy_plugin_dir_to_plugin_type_valid_library():
    result = AnsibleCollectionRef.legacy_plugin_dir_to_plugin_type('library')
    assert result == 'modules'

def test_legacy_plugin_dir_to_plugin_type_invalid_plugin():
    with pytest.raises(ValueError, match="invalid_plugins cannot be mapped to a valid collection ref type"):
        AnsibleCollectionRef.legacy_plugin_dir_to_plugin_type('invalid_plugins')
