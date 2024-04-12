# file lib/ansible/playbook/block.py:89-93
# lines [91, 92, 93]
# branches []

import pytest
from ansible.playbook.block import Block

# Assuming the existence of a mock_loader and mock_variable_manager for the test environment
# If they do not exist, they should be created accordingly

@pytest.fixture
def mock_loader(mocker):
    return mocker.MagicMock()

@pytest.fixture
def mock_variable_manager(mocker):
    return mocker.MagicMock()

def test_block_load_with_non_block_data(mock_loader, mock_variable_manager):
    # Non-block data that should trigger the implicit block creation
    non_block_data = {'name': 'test task', 'debug': 'var=result'}

    # Call the load method with non-block data
    result = Block.load(non_block_data, loader=mock_loader, variable_manager=mock_variable_manager)

    # Assertions to ensure that the result is a Block instance
    # Since the 'implicit' attribute is not part of the Block class, we check for the '_implicit' attribute
    assert isinstance(result, Block)
    assert getattr(result, '_implicit', None) is True

    # Clean up if necessary (not shown as no persistent changes are made in this test)
