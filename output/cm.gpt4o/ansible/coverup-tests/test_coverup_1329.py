# file lib/ansible/playbook/play.py:350-365
# lines []
# branches ['356->exit']

import pytest
from unittest.mock import MagicMock

# Assuming the Play class and its dependencies are imported from ansible.playbook.play
from ansible.playbook.play import Play

class TestPlay:
    def test_deserialize_with_roles(self, mocker):
        # Mocking the Role class and its deserialize method
        Role = mocker.patch('ansible.playbook.play.Role')
        role_instance = Role.return_value
        role_instance.deserialize = MagicMock()

        # Creating a Play instance
        play = Play()

        # Data to be deserialized, including 'roles'
        data = {
            'included_path': '/some/path',
            'action_groups': {'group1': 'action1'},
            'group_actions': {'action2': 'group2'},
            'roles': [{'name': 'role1'}, {'name': 'role2'}]
        }

        # Call the deserialize method
        play.deserialize(data)

        # Assertions to verify the roles were deserialized and set correctly
        assert hasattr(play, 'roles')
        assert len(play.roles) == 2
        role_instance.deserialize.assert_any_call({'name': 'role1'})
        role_instance.deserialize.assert_any_call({'name': 'role2'})

        # Ensure 'roles' key is removed from data
        assert 'roles' not in data

        # Clean up
        delattr(play, 'roles')

    def test_deserialize_without_roles(self):
        # Creating a Play instance
        play = Play()

        # Data to be deserialized, without 'roles'
        data = {
            'included_path': '/some/path',
            'action_groups': {'group1': 'action1'},
            'group_actions': {'action2': 'group2'}
        }

        # Call the deserialize method
        play.deserialize(data)

        # Assertions to verify 'roles' attribute is empty
        assert hasattr(play, 'roles')
        assert play.roles == []
