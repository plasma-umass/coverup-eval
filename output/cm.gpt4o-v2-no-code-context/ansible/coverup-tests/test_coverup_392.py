# file: lib/ansible/playbook/block.py:105-117
# asked: {"lines": [105, 111, 112, 113, 115, 117], "branches": [[111, 112], [111, 117], [112, 113], [112, 115]]}
# gained: {"lines": [105, 111, 112, 113, 115, 117], "branches": [[111, 112], [111, 117], [112, 113], [112, 115]]}

import pytest
from unittest.mock import MagicMock

# Assuming the Block class and its dependencies are imported from ansible.playbook.block
from ansible.playbook.block import Block

class TestBlock:
    @pytest.fixture
    def block_instance(self):
        return Block()

    def test_preprocess_data_with_non_block_list(self, block_instance, mocker):
        ds = ['task1', 'task2']
        mock_super = mocker.patch('ansible.playbook.block.Base.preprocess_data', return_value='processed')
        mock_is_block = mocker.patch('ansible.playbook.block.Block.is_block', return_value=False)

        result = block_instance.preprocess_data(ds)

        mock_is_block.assert_called_once_with(ds)
        mock_super.assert_called_once_with(dict(block=ds))
        assert result == 'processed'

    def test_preprocess_data_with_non_block_single_task(self, block_instance, mocker):
        ds = 'task1'
        mock_super = mocker.patch('ansible.playbook.block.Base.preprocess_data', return_value='processed')
        mock_is_block = mocker.patch('ansible.playbook.block.Block.is_block', return_value=False)

        result = block_instance.preprocess_data(ds)

        mock_is_block.assert_called_once_with(ds)
        mock_super.assert_called_once_with(dict(block=[ds]))
        assert result == 'processed'

    def test_preprocess_data_with_block(self, block_instance, mocker):
        ds = {'block': ['task1', 'task2']}
        mock_super = mocker.patch('ansible.playbook.block.Base.preprocess_data', return_value='processed')
        mock_is_block = mocker.patch('ansible.playbook.block.Block.is_block', return_value=True)

        result = block_instance.preprocess_data(ds)

        mock_is_block.assert_called_once_with(ds)
        mock_super.assert_called_once_with(ds)
        assert result == 'processed'
