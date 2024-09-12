# file: lib/ansible/playbook/role/definition.py:114-135
# asked: {"lines": [121, 122, 124, 125, 126, 130, 131, 132, 133, 135], "branches": [[121, 122], [121, 124], [125, 126], [125, 130], [130, 131], [130, 135]]}
# gained: {"lines": [121, 122, 124, 125, 126, 130, 131, 132, 133, 135], "branches": [[121, 122], [121, 124], [125, 126], [125, 130], [130, 131], [130, 135]]}

import pytest
from ansible.errors import AnsibleError
from ansible.playbook.role.definition import RoleDefinition
from ansible.template import Templar
from unittest.mock import Mock

class TestRoleDefinition:
    @pytest.fixture
    def role_definition(self):
        return RoleDefinition()

    def test_load_role_name_with_string(self, role_definition):
        result = role_definition._load_role_name('simple_role')
        assert result == 'simple_role'

    def test_load_role_name_with_role_field(self, role_definition):
        ds = {'role': 'role_name'}
        result = role_definition._load_role_name(ds)
        assert result == 'role_name'

    def test_load_role_name_with_name_field(self, role_definition):
        ds = {'name': 'name_value'}
        result = role_definition._load_role_name(ds)
        assert result == 'name_value'

    def test_load_role_name_with_invalid_role_name(self, role_definition):
        ds = {'role': 123}
        with pytest.raises(AnsibleError, match='role definitions must contain a role name'):
            role_definition._load_role_name(ds)

    def test_load_role_name_with_missing_role_name(self, role_definition):
        ds = {}
        with pytest.raises(AnsibleError, match='role definitions must contain a role name'):
            role_definition._load_role_name(ds)

    def test_load_role_name_with_variable_manager(self, monkeypatch, role_definition):
        ds = {'role': 'role_name'}
        mock_variable_manager = Mock()
        mock_variable_manager.get_vars.return_value = {'var1': 'value1'}
        mock_templar = Mock()
        mock_templar.template.return_value = 'templated_role_name'

        monkeypatch.setattr(role_definition, '_variable_manager', mock_variable_manager)
        monkeypatch.setattr(role_definition, '_play', Mock())
        monkeypatch.setattr(role_definition, '_loader', Mock())
        monkeypatch.setattr('ansible.playbook.role.definition.Templar', lambda loader, variables: mock_templar)

        result = role_definition._load_role_name(ds)
        assert result == 'templated_role_name'
        mock_variable_manager.get_vars.assert_called_once_with(play=role_definition._play)
        mock_templar.template.assert_called_once_with('role_name')
