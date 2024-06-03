# file lib/ansible/playbook/block.py:392-396
# lines [392, 393, 394, 396]
# branches ['393->394', '393->396']

import pytest
from unittest.mock import Mock

# Assuming the necessary imports for Block and its parent classes
from ansible.playbook.block import Block

@pytest.fixture
def mock_parent():
    return Mock()

def test_get_include_params_with_parent(mock_parent):
    block = Block()
    block._parent = mock_parent
    mock_parent.get_include_params.return_value = {'key': 'value'}
    
    result = block.get_include_params()
    
    mock_parent.get_include_params.assert_called_once()
    assert result == {'key': 'value'}

def test_get_include_params_without_parent():
    block = Block()
    block._parent = None
    
    result = block.get_include_params()
    
    assert result == {}
