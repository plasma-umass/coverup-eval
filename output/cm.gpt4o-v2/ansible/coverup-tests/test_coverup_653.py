# file: lib/ansible/playbook/block.py:89-93
# asked: {"lines": [89, 90, 91, 92, 93], "branches": []}
# gained: {"lines": [89, 90, 91, 92, 93], "branches": []}

import pytest
from ansible.playbook.block import Block
from ansible.parsing.dataloader import DataLoader
from ansible.vars.manager import VariableManager

@pytest.fixture
def block_data():
    return {
        'block': [
            {'name': 'test task', 'action': 'debug', 'args': {'msg': 'Hello World'}}
        ]
    }

def test_block_load(block_data, mocker):
    mocker.patch('ansible.playbook.block.Block.is_block', return_value=True)
    mocker.patch('ansible.playbook.block.Block.load_data', return_value='loaded_data')

    result = Block.load(block_data, variable_manager=VariableManager(), loader=DataLoader())

    assert result == 'loaded_data'
    Block.is_block.assert_called_once_with(block_data)
    Block.load_data.assert_called_once_with(block_data, variable_manager=mocker.ANY, loader=mocker.ANY)
