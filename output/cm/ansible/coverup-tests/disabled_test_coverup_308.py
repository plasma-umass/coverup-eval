# file lib/ansible/playbook/play.py:264-278
# lines [264, 270, 272, 273, 274, 275, 276, 278]
# branches ['272->273', '272->278', '273->274', '273->278', '274->275', '274->276']

import pytest
from ansible.playbook.play import Play
from ansible.playbook.role import Role
from unittest.mock import Mock

# Mock Role class to simulate the behavior of roles with and without 'from_include'
class MockRole:
    def __init__(self, from_include=False):
        self.from_include = from_include

    def get_handler_blocks(self, play=None):
        return [Mock()]

@pytest.fixture
def mock_role(mocker):
    mocker.patch('ansible.playbook.role.Role', side_effect=MockRole)

def test_compile_roles_handlers_excludes_from_include_roles(mock_role):
    play = Play()
    play.roles = [MockRole(from_include=True), MockRole(from_include=False)]

    block_list = play.compile_roles_handlers()

    assert len(block_list) == 1  # Only one role should contribute to the block_list
    assert isinstance(block_list[0], Mock)  # The block should be a mock instance

def test_compile_roles_handlers_includes_normal_roles(mock_role):
    play = Play()
    play.roles = [MockRole(from_include=False), MockRole(from_include=False)]

    block_list = play.compile_roles_handlers()

    assert len(block_list) == 2  # Both roles should contribute to the block_list
    for block in block_list:
        assert isinstance(block, Mock)  # Each block should be a mock instance
