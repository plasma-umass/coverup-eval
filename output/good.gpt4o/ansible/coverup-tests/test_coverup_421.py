# file lib/ansible/playbook/block.py:105-117
# lines [105, 111, 112, 113, 115, 117]
# branches ['111->112', '111->117', '112->113', '112->115']

import pytest
from unittest.mock import MagicMock
from ansible.playbook.block import Block

class TestBlock:
    @pytest.fixture
    def block_instance(self, mocker):
        mocker.patch('ansible.playbook.block.Base.preprocess_data', return_value=None)
        mocker.patch('ansible.playbook.block.Block.is_block', return_value=False)
        return Block()

    def test_preprocess_data_with_list(self, block_instance, mocker):
        ds = [{'name': 'task1'}, {'name': 'task2'}]
        mock_super = mocker.patch('ansible.playbook.block.Base.preprocess_data', return_value=None)
        
        block_instance.preprocess_data(ds)
        
        mock_super.assert_called_once_with(dict(block=ds))

    def test_preprocess_data_with_non_list(self, block_instance, mocker):
        ds = {'name': 'task1'}
        mock_super = mocker.patch('ansible.playbook.block.Base.preprocess_data', return_value=None)
        
        block_instance.preprocess_data(ds)
        
        mock_super.assert_called_once_with(dict(block=[ds]))

    def test_preprocess_data_with_block(self, block_instance, mocker):
        ds = {'block': [{'name': 'task1'}, {'name': 'task2'}]}
        mocker.patch('ansible.playbook.block.Block.is_block', return_value=True)
        mock_super = mocker.patch('ansible.playbook.block.Base.preprocess_data', return_value=None)
        
        block_instance.preprocess_data(ds)
        
        mock_super.assert_called_once_with(ds)
