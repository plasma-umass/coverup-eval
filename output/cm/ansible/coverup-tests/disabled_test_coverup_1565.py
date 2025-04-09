# file lib/ansible/playbook/play.py:280-310
# lines [290, 291, 292, 293, 294, 297, 298, 300, 302, 303, 304, 305, 306, 307, 308, 310]
# branches ['297->298', '297->300']

import pytest
from ansible.playbook.play import Play
from ansible.playbook.block import Block
from ansible.playbook.role import Role
from ansible.playbook.task import Task
from ansible.vars.manager import VariableManager
from ansible.parsing.dataloader import DataLoader

@pytest.fixture
def mock_play(mocker):
    play = Play()
    play._variable_manager = mocker.MagicMock(spec=VariableManager)
    play._loader = mocker.MagicMock(spec=DataLoader)
    play.pre_tasks = [Task()]
    play.tasks = [Task()]
    play.post_tasks = [Task()]
    play._compile_roles = mocker.MagicMock(return_value=[Role()])
    return play

def test_compile_includes_flush_blocks(mock_play):
    block_list = mock_play.compile()

    # Verify that flush blocks are included at the correct positions
    assert isinstance(block_list[0], Task)  # pre_tasks
    assert isinstance(block_list[1], Block)  # flush_block
    assert isinstance(block_list[2], Role)  # roles
    assert isinstance(block_list[3], Task)  # tasks
    assert isinstance(block_list[4], Block)  # flush_block
    assert isinstance(block_list[5], Task)  # post_tasks
    assert isinstance(block_list[6], Block)  # flush_block

    # Verify that the flush blocks contain the flush_handlers meta task
    for block in block_list[1::3]:  # Only check the flush_blocks
        assert block.block[0].action == 'meta'
        assert block.block[0].args.get('_raw_params') == 'flush_handlers'
        assert block.block[0].implicit is True

    # Verify that the mock method _compile_roles was called
    mock_play._compile_roles.assert_called_once()
