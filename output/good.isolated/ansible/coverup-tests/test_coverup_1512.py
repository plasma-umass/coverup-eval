# file lib/ansible/playbook/block.py:179-222
# lines [180, 181, 182, 183, 184, 185, 186, 188, 191, 192, 193, 195, 197, 198, 199, 201, 202, 203, 205, 206, 208, 209, 210, 212, 213, 214, 215, 217, 218, 219, 221, 222]
# branches ['182->183', '182->199', '184->185', '184->197', '186->188', '186->191', '192->193', '192->195', '205->206', '205->208', '209->210', '209->212', '212->213', '212->217', '218->219', '218->221']

import pytest
from ansible.playbook.block import Block

class MockTask:
    def __init__(self, parent=None):
        self._parent = parent

    def copy(self, exclude_parent=False):
        new_task = MockTask()
        if not exclude_parent:
            new_task._parent = self._parent
        return new_task

@pytest.fixture
def mock_block(mocker):
    block = Block()
    block._play = mocker.MagicMock()
    block._use_handlers = mocker.MagicMock()
    block._dep_chain = mocker.MagicMock()
    block._parent = mocker.MagicMock()
    block._role = mocker.MagicMock()
    block.block = [MockTask(parent=block)]
    block.rescue = [MockTask(parent=block)]
    block.always = [MockTask(parent=block)]
    return block

def test_block_copy(mock_block):
    # Copy the block without excluding parent or tasks
    new_block = mock_block.copy(exclude_parent=False, exclude_tasks=False)

    # Assertions to ensure the copy has the correct attributes
    assert new_block._play == mock_block._play
    assert new_block._use_handlers == mock_block._use_handlers
    assert new_block._dep_chain == mock_block._dep_chain[:]
    assert new_block._parent is not None
    assert new_block._role == mock_block._role

    # Assertions to ensure tasks are copied correctly
    assert len(new_block.block) == len(mock_block.block)
    assert new_block.block[0]._parent == new_block
    assert len(new_block.rescue) == len(mock_block.rescue)
    assert new_block.rescue[0]._parent == new_block
    assert len(new_block.always) == len(mock_block.always)
    assert new_block.always[0]._parent == new_block

    # Assertions to ensure the parent of tasks is set correctly
    assert new_block.block[0]._parent == new_block
    assert new_block.rescue[0]._parent == new_block
    assert new_block.always[0]._parent == new_block

    # Validate the new block
    new_block.validate()
