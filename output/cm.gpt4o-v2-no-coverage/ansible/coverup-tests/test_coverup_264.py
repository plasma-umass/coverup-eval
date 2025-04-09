# file: lib/ansible/playbook/play.py:350-365
# asked: {"lines": [350, 351, 353, 354, 355, 356, 357, 358, 359, 360, 361, 362, 364, 365], "branches": [[356, 0], [356, 357], [359, 360], [359, 364]]}
# gained: {"lines": [350, 351, 353, 354, 355, 356, 357, 358, 359, 360, 361, 362, 364, 365], "branches": [[356, 0], [356, 357], [359, 360], [359, 364]]}

import pytest
from ansible.playbook.play import Play
from ansible.playbook.role import Role

@pytest.fixture
def play_instance():
    return Play()

def test_deserialize_with_roles(play_instance, mocker):
    mock_role_class = mocker.patch('ansible.playbook.play.Role', autospec=True)
    mock_role_instance = mock_role_class.return_value
    mock_role_instance.deserialize = mocker.Mock()

    data = {
        'included_path': '/some/path',
        'action_groups': {'group1': 'action1'},
        'group_actions': {'action2': 'group2'},
        'roles': [{'role_key': 'role_value'}]
    }

    play_instance.deserialize(data)

    assert play_instance._included_path == '/some/path'
    assert play_instance._action_groups == {'group1': 'action1'}
    assert play_instance._group_actions == {'action2': 'group2'}
    assert hasattr(play_instance, 'roles')
    assert len(play_instance.roles) == 1
    mock_role_instance.deserialize.assert_called_once_with({'role_key': 'role_value'})
    assert 'roles' not in data

def test_deserialize_without_roles(play_instance):
    data = {
        'included_path': '/some/path',
        'action_groups': {'group1': 'action1'},
        'group_actions': {'action2': 'group2'}
    }

    play_instance.deserialize(data)

    assert play_instance._included_path == '/some/path'
    assert play_instance._action_groups == {'group1': 'action1'}
    assert play_instance._group_actions == {'action2': 'group2'}
    assert play_instance.roles == []
