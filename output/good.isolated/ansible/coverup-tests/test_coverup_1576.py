# file lib/ansible/playbook/play.py:264-278
# lines [270, 272, 273, 274, 275, 276, 278]
# branches ['272->273', '272->278', '273->274', '273->278', '274->275', '274->276']

import pytest
from ansible.playbook.play import Play
from ansible.playbook.role import Role

# Mock Role class to simulate the behavior of roles with handlers
class MockRole:
    def __init__(self, from_include=False, handler_blocks=None):
        self.from_include = from_include
        self.handler_blocks = handler_blocks or []

    def get_handler_blocks(self, play=None):
        return self.handler_blocks

@pytest.fixture
def mock_role(mocker):
    return mocker.patch('ansible.playbook.play.Role', side_effect=MockRole)

def test_compile_roles_handlers_includes_handlers_from_roles(mock_role):
    # Create a Play object with mock roles
    play = Play()
    play.roles = [
        MockRole(from_include=False, handler_blocks=['handler1', 'handler2']),
        MockRole(from_include=True),  # This role should be skipped
        MockRole(from_include=False, handler_blocks=['handler3']),
    ]

    # Call the method under test
    handlers = play.compile_roles_handlers()

    # Assert that the correct handlers are included
    assert handlers == ['handler1', 'handler2', 'handler3']

    # Assert that roles with from_include=True are skipped
    assert 'handler_from_skipped_role' not in handlers
