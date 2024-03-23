# file lib/ansible/playbook/role/metadata.py:51-61
# lines [57, 58, 60, 61]
# branches ['57->58', '57->60']

import pytest
from ansible.errors import AnsibleParserError
from ansible.playbook.role.metadata import RoleMetadata
from unittest.mock import MagicMock

# Assuming the existence of a RoleMetadata class with the provided load method

def test_role_metadata_load_with_non_dict_data():
    owner_mock = MagicMock()
    owner_mock.get_name.return_value = "test_role"
    
    with pytest.raises(AnsibleParserError) as excinfo:
        RoleMetadata.load(data="not_a_dict", owner=owner_mock)
    
    assert "the 'meta/main.yml' for role test_role is not a dictionary" in str(excinfo.value)
    owner_mock.get_name.assert_called_once()
