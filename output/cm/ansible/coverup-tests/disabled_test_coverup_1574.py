# file lib/ansible/playbook/play.py:243-262
# lines [252, 254, 255, 258, 259, 260, 262]
# branches ['254->255', '254->262', '255->258', '255->262', '258->259', '258->260']

import pytest
from ansible.playbook.play import Play
from ansible.playbook.role import Role

# Mock Role class to simulate the behavior of roles with and without `from_include`
class MockRole:
    def __init__(self, from_include=False):
        self.from_include = from_include

    def compile(self, play):
        return ['task1', 'task2']

@pytest.fixture
def mock_role(mocker):
    return mocker.patch('ansible.playbook.role.Role', side_effect=MockRole)

def test_compile_roles_includes_roles_not_from_include(mock_role):
    play = Play()

    # Create mock roles, one that is from an include and one that is not
    included_role = MockRole(from_include=True)
    regular_role = MockRole(from_include=False)

    # Assign these mock roles to the play's roles attribute
    play.roles = [included_role, regular_role]

    # Call the method under test
    block_list = play._compile_roles()

    # Assert that the block_list only contains tasks from the regular role
    assert block_list == ['task1', 'task2']

    # Assert that the included role was skipped
    assert included_role not in block_list
