# file lib/ansible/playbook/block.py:105-117
# lines [105, 111, 112, 113, 115, 117]
# branches ['111->112', '111->117', '112->113', '112->115']

import pytest
from ansible.playbook.block import Block
from unittest.mock import MagicMock

@pytest.fixture
def mock_super_preprocess_data(mocker):
    return mocker.patch('ansible.playbook.block.Base.preprocess_data', return_value='mocked_super')

def test_block_preprocess_data_with_list(mock_super_preprocess_data):
    block = Block()
    ds = [{'task': 'dummy task'}]
    result = block.preprocess_data(ds)
    assert result == 'mocked_super'
    mock_super_preprocess_data.assert_called_once_with(dict(block=ds))

def test_block_preprocess_data_with_dict(mock_super_preprocess_data):
    block = Block()
    ds = {'task': 'dummy task'}
    result = block.preprocess_data(ds)
    assert result == 'mocked_super'
    mock_super_preprocess_data.assert_called_once_with(dict(block=[ds]))

def test_block_preprocess_data_with_block(mock_super_preprocess_data):
    block = Block()
    ds = {'block': [{'task': 'dummy task'}]}
    result = block.preprocess_data(ds)
    assert result == 'mocked_super'
    mock_super_preprocess_data.assert_called_once_with(ds)
