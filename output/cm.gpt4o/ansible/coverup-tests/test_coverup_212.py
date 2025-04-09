# file lib/ansible/playbook/play.py:350-365
# lines [350, 351, 353, 354, 355, 356, 357, 358, 359, 360, 361, 362, 364, 365]
# branches ['356->exit', '356->357', '359->360', '359->364']

import pytest
from unittest.mock import MagicMock

# Assuming the Play class and its dependencies are imported from ansible.playbook.play
from ansible.playbook.play import Play

class TestPlay:
    def test_deserialize(self, mocker):
        # Mocking the Role class and its deserialize method
        Role = mocker.patch('ansible.playbook.play.Role')
        role_instance = Role.return_value
        role_instance.deserialize = MagicMock()

        # Creating a Play instance
        play = Play()

        # Data to be deserialized
        data = {
            'included_path': '/some/path',
            'action_groups': {'group1': 'action1'},
            'group_actions': {'action2': 'group2'},
            'roles': [{'name': 'role1'}, {'name': 'role2'}]
        }

        # Calling the deserialize method
        play.deserialize(data)

        # Assertions to verify the deserialization
        assert play._included_path == '/some/path'
        assert play._action_groups == {'group1': 'action1'}
        assert play._group_actions == {'action2': 'group2'}
        assert len(play.roles) == 2
        role_instance.deserialize.assert_any_call({'name': 'role1'})
        role_instance.deserialize.assert_any_call({'name': 'role2'})

        # Ensure 'roles' key is removed from data
        assert 'roles' not in data
