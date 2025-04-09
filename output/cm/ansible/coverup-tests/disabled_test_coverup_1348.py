# file lib/ansible/playbook/role/include.py:36-60
# lines [47, 48, 59, 60]
# branches ['56->59']

import pytest
from ansible.errors import AnsibleError, AnsibleParserError
from ansible.playbook.role.include import RoleInclude
from ansible.parsing.yaml.objects import AnsibleBaseYAMLObject
from ansible.module_utils.six import string_types

# Mock classes and functions
class MockPlay(object):
    pass

class MockLoader(object):
    pass

class MockVariableManager(object):
    pass

class MockAnsibleBaseYAMLObject(AnsibleBaseYAMLObject):
    pass

# Test function to cover missing lines
def test_role_include_load_with_invalid_data_types(mocker):
    play = MockPlay()
    loader = MockLoader()
    variable_manager = MockVariableManager()
    current_role_path = "fake_path"
    collection_list = []

    # Test with invalid data type
    with pytest.raises(AnsibleParserError):
        RoleInclude.load(data=42, play=play, current_role_path=current_role_path, variable_manager=variable_manager, loader=loader, collection_list=collection_list)

    # Test with string containing a comma (old style role requirement)
    with pytest.raises(AnsibleError):
        RoleInclude.load(data="role1,role2", play=play, current_role_path=current_role_path, variable_manager=variable_manager, loader=loader, collection_list=collection_list)

    # Test with valid AnsibleBaseYAMLObject
    data = MockAnsibleBaseYAMLObject()
    mocker.patch.object(RoleInclude, 'load_data', return_value='loaded_data')
    result = RoleInclude.load(data=data, play=play, current_role_path=current_role_path, variable_manager=variable_manager, loader=loader, collection_list=collection_list)
    assert result == 'loaded_data', "RoleInclude.load did not return expected 'loaded_data'"

# Ensure the test function is not executed at import time
if __name__ == "__main__":
    pytest.main([__file__])
