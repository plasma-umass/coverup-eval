# file lib/ansible/playbook/role/include.py:36-60
# lines [47, 48, 59, 60]
# branches ['56->59']

import pytest
from ansible.errors import AnsibleParserError, AnsibleError
from ansible.playbook.role.include import RoleInclude
from ansible.parsing.yaml.objects import AnsibleBaseYAMLObject
from ansible.module_utils.six import string_types
from ansible.module_utils._text import to_native

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
def test_role_include_init_and_load(mocker):
    play = MockPlay()
    role_basedir = "fake_role_basedir"
    variable_manager = MockVariableManager()
    loader = MockLoader()
    collection_list = ["fake_collection"]

    # Test __init__ execution
    role_include = RoleInclude(play=play, role_basedir=role_basedir, variable_manager=variable_manager, loader=loader, collection_list=collection_list)
    assert role_include._play == play
    assert role_include._role_basedir == role_basedir
    assert role_include._variable_manager == variable_manager
    assert role_include._loader == loader
    assert role_include._collection_list == collection_list

    # Test load execution with string type data containing a comma
    with pytest.raises(AnsibleError):
        RoleInclude.load(data="invalid,role", play=play, current_role_path=role_basedir, variable_manager=variable_manager, loader=loader, collection_list=collection_list)

    # Test load execution with invalid type data
    with pytest.raises(AnsibleParserError):
        RoleInclude.load(data=12345, play=play, current_role_path=role_basedir, variable_manager=variable_manager, loader=loader, collection_list=collection_list)

    # Test load execution with AnsibleBaseYAMLObject
    data = MockAnsibleBaseYAMLObject()
    mocker.patch.object(RoleInclude, 'load_data', return_value="loaded_data")
    result = RoleInclude.load(data=data, play=play, current_role_path=role_basedir, variable_manager=variable_manager, loader=loader, collection_list=collection_list)
    assert result == "loaded_data"
