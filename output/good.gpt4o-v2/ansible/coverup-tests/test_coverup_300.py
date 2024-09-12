# file: lib/ansible/utils/collection_loader/_collection_finder.py:825-842
# asked: {"lines": [825, 826, 832, 834, 836, 837, 839, 840, 842], "branches": [[836, 837], [836, 839], [839, 840], [839, 842]]}
# gained: {"lines": [825, 826, 832, 834, 836, 837, 839, 840, 842], "branches": [[836, 837], [836, 839], [839, 840], [839, 842]]}

import pytest
from ansible.utils.collection_loader._collection_finder import AnsibleCollectionRef
from ansible.module_utils.common.text.converters import to_native, to_text

def test_legacy_plugin_dir_to_plugin_type_valid():
    assert AnsibleCollectionRef.legacy_plugin_dir_to_plugin_type('action_plugins') == 'action'
    assert AnsibleCollectionRef.legacy_plugin_dir_to_plugin_type('library') == 'modules'
    assert AnsibleCollectionRef.legacy_plugin_dir_to_plugin_type('module_utils') == 'module_utils'

def test_legacy_plugin_dir_to_plugin_type_invalid():
    with pytest.raises(ValueError, match="invalid_plugins cannot be mapped to a valid collection ref type"):
        AnsibleCollectionRef.legacy_plugin_dir_to_plugin_type('invalid_plugins')

def test_legacy_plugin_dir_to_plugin_type_conversion():
    assert AnsibleCollectionRef.legacy_plugin_dir_to_plugin_type('action_plugins') == 'action'
    assert AnsibleCollectionRef.legacy_plugin_dir_to_plugin_type('library') == 'modules'
    assert AnsibleCollectionRef.legacy_plugin_dir_to_plugin_type('module_utils') == 'module_utils'
