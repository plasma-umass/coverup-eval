# file lib/ansible/playbook/block.py:105-117
# lines [111, 112, 113, 115, 117]
# branches ['111->112', '111->117', '112->113', '112->115']

import pytest
from ansible.playbook.block import Block

@pytest.fixture
def mock_super_preprocess_data(mocker):
    return mocker.patch('ansible.playbook.block.Base.preprocess_data', return_value='mocked_super')

@pytest.mark.parametrize("ds, expected_call", [
    ([{'task': 'dummy'}], {'block': [{'task': 'dummy'}]}),
    ({'task': 'dummy'}, {'block': [{'task': 'dummy'}]}),
])
def test_preprocess_data_non_block(mock_super_preprocess_data, ds, expected_call):
    block = Block()

    result = block.preprocess_data(ds)

    mock_super_preprocess_data.assert_called_once_with(expected_call)
    assert result == 'mocked_super'
