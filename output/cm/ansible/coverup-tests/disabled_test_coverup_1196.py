# file lib/ansible/playbook/block.py:224-243
# lines [230, 231, 232, 233, 235, 237, 238, 239, 240, 241, 243]
# branches ['231->232', '231->235', '232->231', '232->233', '237->238', '237->239', '239->240', '239->243']

import pytest
from ansible.playbook.block import Block

@pytest.fixture
def mock_role(mocker):
    mock_role = mocker.MagicMock()
    mock_role.serialize.return_value = {'role_name': 'test_role'}
    return mock_role

@pytest.fixture
def mock_parent(mocker):
    mock_parent = mocker.MagicMock()
    mock_parent.copy.return_value.serialize.return_value = {'parent_name': 'test_parent'}
    mock_parent.__class__.__name__ = 'MockParent'
    return mock_parent

def test_block_serialize_with_role_and_parent(mock_role, mock_parent, mocker):
    block = Block()
    block._valid_attrs = ['test_attr', 'block', 'rescue', 'always']
    block.test_attr = 'value'
    block._role = mock_role
    block._parent = mock_parent
    mocker.patch.object(block, 'get_dep_chain', return_value='dep_chain_value')

    serialized_data = block.serialize()

    assert serialized_data['test_attr'] == 'value'
    assert 'block' not in serialized_data
    assert 'rescue' not in serialized_data
    assert 'always' not in serialized_data
    assert serialized_data['dep_chain'] == 'dep_chain_value'
    assert serialized_data['role'] == {'role_name': 'test_role'}
    assert serialized_data['parent'] == {'parent_name': 'test_parent'}
    assert serialized_data['parent_type'] == 'MockParent'
