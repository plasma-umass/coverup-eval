# file: lib/ansible/playbook/block.py:361-387
# asked: {"lines": [366, 367, 368, 369, 370, 371, 372, 373, 374, 375, 376, 377, 379, 380, 381, 382, 383, 384, 385, 387], "branches": [[368, 369], [368, 377], [369, 370], [369, 373], [371, 368], [371, 372], [373, 368], [373, 376]]}
# gained: {"lines": [366, 367, 368, 369, 370, 371, 372, 373, 374, 375, 376, 377, 379, 380, 381, 382, 383, 384, 385, 387], "branches": [[368, 369], [368, 377], [369, 370], [369, 373], [371, 372], [373, 376]]}

import pytest
from unittest.mock import MagicMock

# Assuming the Block class is defined in ansible.playbook.block
from ansible.playbook.block import Block

class TestBlock:
    @pytest.fixture
    def block(self):
        return Block()

    @pytest.fixture
    def mock_task(self):
        task = MagicMock()
        task.action = 'some_action'
        task.implicit = False
        task.evaluate_tags = MagicMock(return_value=True)
        return task

    @pytest.fixture
    def mock_block(self, mock_task):
        block = Block()
        block.block = [mock_task]
        block.rescue = [mock_task]
        block.always = [mock_task]
        block.copy = MagicMock(return_value=block)
        block.has_tasks = MagicMock(return_value=True)
        return block

    def test_filter_tagged_tasks_with_block(self, block, mock_block, mock_task):
        block._play = MagicMock()
        block._play.only_tags = []
        block._play.skip_tags = []
        
        block.block = [mock_block]
        block.rescue = []
        block.always = []

        result = block.filter_tagged_tasks({})
        assert result.block == [mock_block]
        assert result.rescue == []
        assert result.always == []

    def test_filter_tagged_tasks_with_tasks(self, block, mock_task):
        block._play = MagicMock()
        block._play.only_tags = []
        block._play.skip_tags = []
        
        block.block = [mock_task]
        block.rescue = []
        block.always = []

        result = block.filter_tagged_tasks({})
        assert result.block == [mock_task]
        assert result.rescue == []
        assert result.always == []

    def test_filter_tagged_tasks_with_mixed(self, block, mock_block, mock_task):
        block._play = MagicMock()
        block._play.only_tags = []
        block._play.skip_tags = []
        
        block.block = [mock_block, mock_task]
        block.rescue = [mock_task]
        block.always = [mock_block]

        result = block.filter_tagged_tasks({})
        assert result.block == [mock_block, mock_task]
        assert result.rescue == [mock_task]
        assert result.always == [mock_block]
