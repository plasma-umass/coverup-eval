# file: lib/ansible/playbook/play.py:350-365
# asked: {"lines": [351, 353, 354, 355, 356, 357, 358, 359, 360, 361, 362, 364, 365], "branches": [[356, 0], [356, 357], [359, 360], [359, 364]]}
# gained: {"lines": [351, 353, 354, 355, 356, 357, 358, 359, 360, 361, 362, 364, 365], "branches": [[356, 0], [356, 357], [359, 360], [359, 364]]}

import pytest
from unittest.mock import MagicMock

# Assuming the Play class and its dependencies are imported from ansible.playbook.play
from ansible.playbook.play import Play
from ansible.playbook.role import Role

@pytest.fixture
def play_instance():
    return Play()

def test_deserialize_with_roles(play_instance, mocker):
    # Mocking the Role class and its deserialize method
    mock_role_class = mocker.patch('ansible.playbook.play.Role', autospec=True)
    mock_role_instance = mock_role_class.return_value
    mock_role_instance.deserialize = MagicMock()

    data = {
        'included_path': '/some/path',
        'action_groups': {'group1': 'action1'},
        'group_actions': {'action2': 'group2'},
        'roles': [{'name': 'role1'}, {'name': 'role2'}]
    }

    play_instance.deserialize(data)

    # Assertions to verify the postconditions
    assert play_instance._included_path == '/some/path'
    assert play_instance._action_groups == {'group1': 'action1'}
    assert play_instance._group_actions == {'action2': 'group2'}
    assert hasattr(play_instance, 'roles')
    assert len(play_instance.roles) == 2
    mock_role_instance.deserialize.assert_any_call({'name': 'role1'})
    mock_role_instance.deserialize.assert_any_call({'name': 'role2'})
    assert 'roles' not in data

def test_deserialize_without_roles(play_instance):
    data = {
        'included_path': '/some/path',
        'action_groups': {'group1': 'action1'},
        'group_actions': {'action2': 'group2'}
    }

    play_instance.deserialize(data)

    # Assertions to verify the postconditions
    assert play_instance._included_path == '/some/path'
    assert play_instance._action_groups == {'group1': 'action1'}
    assert play_instance._group_actions == {'action2': 'group2'}
    assert play_instance.roles == []
