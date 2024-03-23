# file lib/ansible/utils/collection_loader/_collection_finder.py:825-842
# lines [832, 834, 836, 837, 839, 840, 842]
# branches ['836->837', '836->839', '839->840', '839->842']

import pytest
from ansible.utils.collection_loader import _collection_finder

def test_legacy_plugin_dir_to_plugin_type_valid(mocker):
    mocker.patch.object(_collection_finder.AnsibleCollectionRef, 'VALID_REF_TYPES', ['modules', 'action'])
    assert _collection_finder.AnsibleCollectionRef.legacy_plugin_dir_to_plugin_type('library') == 'modules'
    assert _collection_finder.AnsibleCollectionRef.legacy_plugin_dir_to_plugin_type('action_plugins') == 'action'

def test_legacy_plugin_dir_to_plugin_type_invalid(mocker):
    mocker.patch.object(_collection_finder.AnsibleCollectionRef, 'VALID_REF_TYPES', ['modules', 'action'])
    with pytest.raises(ValueError) as excinfo:
        _collection_finder.AnsibleCollectionRef.legacy_plugin_dir_to_plugin_type('invalid_plugins')
    assert 'invalid_plugins cannot be mapped to a valid collection ref type' in str(excinfo.value)
