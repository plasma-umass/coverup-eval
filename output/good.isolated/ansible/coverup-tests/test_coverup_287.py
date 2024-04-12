# file lib/ansible/playbook/play.py:243-262
# lines [243, 252, 254, 255, 258, 259, 260, 262]
# branches ['254->255', '254->262', '255->258', '255->262', '258->259', '258->260']

import pytest
from ansible.playbook.play import Play
from ansible.playbook.role import Role

# Mock Role class to simulate the behavior of roles and dependencies
class MockRole(Role):
    def __init__(self, from_include=False, tasks=None):
        self.from_include = from_include
        self.tasks = tasks or []

    def compile(self, play):
        return self.tasks

@pytest.fixture
def mock_role(mocker):
    mocker.patch('ansible.playbook.role.Role', MockRole)

def test_play_compile_roles_excludes_from_include_roles(mock_role):
    # Create a play with two roles, one that should be included and one that should not
    play = Play()
    included_role = MockRole(from_include=False, tasks=['task1', 'task2'])
    excluded_role = MockRole(from_include=True, tasks=['task3', 'task4'])
    play.roles = [included_role, excluded_role]

    # Compile roles and assert that only the included role's tasks are in the block list
    block_list = play._compile_roles()
    assert block_list == ['task1', 'task2']

    # Also assert that the excluded role's tasks are not in the block list
    assert 'task3' not in block_list
    assert 'task4' not in block_list
