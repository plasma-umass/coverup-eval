# file lib/ansible/playbook/block.py:105-117
# lines [111, 112, 113, 115, 117]
# branches ['111->112', '111->117', '112->113', '112->115']

import pytest
from ansible.playbook.block import Block

@pytest.fixture
def mock_super_preprocess_data(mocker):
    return mocker.patch('ansible.playbook.block.Base.preprocess_data', return_value='mocked_super')

@pytest.mark.parametrize("input_ds, expected_call_arg", [
    ([{'task': 'dummy_task'}], {'block': [{'task': 'dummy_task'}]}),
    ({'task': 'dummy_task'}, {'block': [{'task': 'dummy_task'}]}),
])
def test_block_preprocess_data_non_block(mock_super_preprocess_data, input_ds, expected_call_arg):
    block = Block()

    result = block.preprocess_data(input_ds)

    mock_super_preprocess_data.assert_called_once_with(expected_call_arg)
    assert result == 'mocked_super'

@pytest.fixture
def mock_is_block(mocker):
    return mocker.patch('ansible.playbook.block.Block.is_block', return_value=False)

def test_block_preprocess_data_block(mock_super_preprocess_data, mock_is_block):
    ds = {'block': [{'task': 'dummy_task'}]}
    mock_is_block.return_value = True

    result = Block().preprocess_data(ds)

    mock_super_preprocess_data.assert_called_once_with(ds)
    assert result == 'mocked_super'
