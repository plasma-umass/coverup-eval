# file lib/ansible/playbook/block.py:392-396
# lines [393, 394, 396]
# branches ['393->394', '393->396']

import pytest
from ansible.playbook.block import Block

# Assuming the Block class is part of a larger module and has dependencies that need to be mocked
# We will use pytest-mock to create the necessary mocks

@pytest.fixture
def mock_parent(mocker):
    mock = mocker.Mock()
    mock.get_include_params.return_value = {'mocked': 'params'}
    return mock

def test_get_include_params_with_parent(mocker, mock_parent):
    block = Block()
    mocker.patch.object(block, '_parent', mock_parent)

    # Test that get_include_params returns the parent's get_include_params
    assert block.get_include_params() == {'mocked': 'params'}
    mock_parent.get_include_params.assert_called_once()

def test_get_include_params_without_parent(mocker):
    block = Block()
    mocker.patch.object(block, '_parent', None)

    # Test that get_include_params returns an empty dict when there is no parent
    assert block.get_include_params() == {}
