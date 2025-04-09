# file: lib/ansible/utils/collection_loader/_collection_finder.py:825-842
# asked: {"lines": [825, 826, 832, 834, 836, 837, 839, 840, 842], "branches": [[836, 837], [836, 839], [839, 840], [839, 842]]}
# gained: {"lines": [825, 826, 832, 834, 836, 837, 839, 840, 842], "branches": [[836, 837], [836, 839], [839, 840], [839, 842]]}

import pytest
from ansible.utils.collection_loader._collection_finder import AnsibleCollectionRef
from ansible.module_utils._text import to_text, to_native

class TestAnsibleCollectionRef:
    @pytest.fixture(autouse=True)
    def setup(self, monkeypatch):
        # Mock VALID_REF_TYPES to control the test environment
        self.valid_ref_types = {'action', 'modules', 'role'}
        monkeypatch.setattr(AnsibleCollectionRef, 'VALID_REF_TYPES', self.valid_ref_types)

    def test_legacy_plugin_dir_to_plugin_type_action_plugins(self):
        result = AnsibleCollectionRef.legacy_plugin_dir_to_plugin_type('action_plugins')
        assert result == 'action'

    def test_legacy_plugin_dir_to_plugin_type_library(self):
        result = AnsibleCollectionRef.legacy_plugin_dir_to_plugin_type('library')
        assert result == 'modules'

    def test_legacy_plugin_dir_to_plugin_type_invalid(self):
        with pytest.raises(ValueError) as excinfo:
            AnsibleCollectionRef.legacy_plugin_dir_to_plugin_type('invalid_plugins')
        assert 'invalid_plugins cannot be mapped to a valid collection ref type' in str(excinfo.value)

    def test_legacy_plugin_dir_to_plugin_type_valid_custom(self):
        self.valid_ref_types.add('custom')
        result = AnsibleCollectionRef.legacy_plugin_dir_to_plugin_type('custom_plugins')
        assert result == 'custom'
