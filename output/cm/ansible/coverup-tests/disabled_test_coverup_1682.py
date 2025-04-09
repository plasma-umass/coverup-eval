# file lib/ansible/playbook/role/metadata.py:51-61
# lines [60, 61]
# branches ['57->60']

import pytest
from ansible.errors import AnsibleParserError
from ansible.playbook.role.metadata import RoleMetadata
from unittest.mock import MagicMock

# Assuming the existence of a RoleMetadata class with the provided method snippet

class TestRoleMetadata:

    def test_load_with_dict(self, mocker):
        # Mock the owner and its get_name method
        mock_owner = MagicMock()
        mock_owner.get_name.return_value = "test_role"

        # Mock the load_data method to just return the instance for simplicity
        mocker.patch.object(RoleMetadata, 'load_data', return_value=RoleMetadata(owner=mock_owner))

        # Call the static load method with a dictionary
        data = {}
        result = RoleMetadata.load(data, owner=mock_owner)

        # Assert that the result is an instance of RoleMetadata
        assert isinstance(result, RoleMetadata)

    def test_load_with_non_dict_raises_error(self, mocker):
        # Mock the owner and its get_name method
        mock_owner = MagicMock()
        mock_owner.get_name.return_value = "test_role"

        # Call the static load method with a non-dictionary, expecting an exception
        with pytest.raises(AnsibleParserError) as excinfo:
            RoleMetadata.load("not_a_dict", owner=mock_owner)

        # Assert that the exception message is as expected
        assert "the 'meta/main.yml' for role test_role is not a dictionary" in str(excinfo.value)
