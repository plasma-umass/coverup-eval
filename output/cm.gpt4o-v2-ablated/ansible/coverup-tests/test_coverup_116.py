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

    @pytest.mark.parametrize("legacy_plugin_dir_name, expected_plugin_type", [
        ('action_plugins', 'action'),
        ('library', 'modules'),
        ('role_plugins', 'role'),
    ])
    def test_legacy_plugin_dir_to_plugin_type_valid(self, legacy_plugin_dir_name, expected_plugin_type):
        result = AnsibleCollectionRef.legacy_plugin_dir_to_plugin_type(legacy_plugin_dir_name)
        assert result == expected_plugin_type

    @pytest.mark.parametrize("invalid_legacy_plugin_dir_name", [
        'invalid_plugins',
        'unknown_plugins',
        'random_dir',
    ])
    def test_legacy_plugin_dir_to_plugin_type_invalid(self, invalid_legacy_plugin_dir_name):
        with pytest.raises(ValueError) as excinfo:
            AnsibleCollectionRef.legacy_plugin_dir_to_plugin_type(invalid_legacy_plugin_dir_name)
        assert str(excinfo.value) == '{0} cannot be mapped to a valid collection ref type'.format(to_native(invalid_legacy_plugin_dir_name))
