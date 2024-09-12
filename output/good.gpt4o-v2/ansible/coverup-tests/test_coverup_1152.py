# file: lib/ansible/playbook/play.py:350-365
# asked: {"lines": [351, 353, 354, 355, 356, 357, 358, 359, 360, 361, 362, 364, 365], "branches": [[356, 0], [356, 357], [359, 360], [359, 364]]}
# gained: {"lines": [351, 353, 354, 355, 356, 357, 358, 359, 360, 361, 362, 364, 365], "branches": [[356, 357], [359, 360], [359, 364]]}

import pytest
from ansible.playbook.play import Play
from ansible.playbook.role import Role

@pytest.fixture
def play_instance():
    return Play()

def test_deserialize_with_roles(play_instance, mocker):
    mocker.patch.object(Role, 'deserialize', return_value=None)
    data = {
        'included_path': '/some/path',
        'action_groups': {'group1': 'action1'},
        'group_actions': {'group2': 'action2'},
        'roles': [
            {'name': 'role1'},
            {'name': 'role2'}
        ]
    }

    play_instance.deserialize(data)

    assert play_instance._included_path == '/some/path'
    assert play_instance._action_groups == {'group1': 'action1'}
    assert play_instance._group_actions == {'group2': 'action2'}
    assert hasattr(play_instance, 'roles')
    assert len(play_instance.roles) == 2
    assert isinstance(play_instance.roles[0], Role)
    assert isinstance(play_instance.roles[1], Role)
    assert 'roles' not in data
