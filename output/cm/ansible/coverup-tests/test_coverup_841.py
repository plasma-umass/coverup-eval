# file lib/ansible/playbook/block.py:65-66
# lines [65, 66]
# branches []

import pytest
from ansible.playbook.block import Block

# Assuming the Block class has the necessary __init__ method and other dependencies
# If not, we would need to mock or create those dependencies.

@pytest.fixture
def block_instance(mocker):
    mocker.patch('ansible.playbook.block.Base.__init__', return_value=None)
    mocker.patch('ansible.playbook.block.Conditional.__init__', return_value=None)
    mocker.patch('ansible.playbook.block.CollectionSearch.__init__', return_value=None)
    mocker.patch('ansible.playbook.block.Taggable.__init__', return_value=None)
    block = Block()
    block._uuid = '1234-5678'
    block._parent = 'parent_block'
    return block

def test_block_repr(block_instance):
    expected_repr = "BLOCK(uuid=1234-5678)(id={})(parent=parent_block)".format(id(block_instance))
    assert repr(block_instance) == expected_repr
