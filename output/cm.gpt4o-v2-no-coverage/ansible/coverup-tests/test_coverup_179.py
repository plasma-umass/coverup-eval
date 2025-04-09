# file: lib/ansible/module_utils/facts/network/hurd.py:64-82
# asked: {"lines": [64, 65, 67, 68, 69, 71, 73, 74, 75, 76, 77, 79, 80, 82], "branches": [[68, 69], [68, 71], [73, 74], [73, 79], [75, 73], [75, 76], [79, 80], [79, 82]]}
# gained: {"lines": [64, 65, 67, 68, 69, 71, 73, 74, 75, 76, 77, 79, 80, 82], "branches": [[68, 69], [68, 71], [73, 74], [73, 79], [75, 73], [75, 76], [79, 80], [79, 82]]}

import os
import pytest
from unittest.mock import MagicMock, patch
from ansible.module_utils.facts.network.hurd import HurdPfinetNetwork

@pytest.fixture
def hurd_pfinet_network():
    module = MagicMock()
    network = HurdPfinetNetwork(module)
    return network

def test_populate_no_fsysopts_path(hurd_pfinet_network):
    hurd_pfinet_network.module.get_bin_path.return_value = None
    result = hurd_pfinet_network.populate()
    assert result == {}

@patch('os.path.exists')
def test_populate_no_socket_path(mock_exists, hurd_pfinet_network):
    hurd_pfinet_network.module.get_bin_path.return_value = '/bin/fsysopts'
    mock_exists.return_value = False
    result = hurd_pfinet_network.populate()
    assert result == {}

@patch('os.path.exists')
def test_populate_with_socket_path(mock_exists, hurd_pfinet_network):
    hurd_pfinet_network.module.get_bin_path.return_value = '/bin/fsysopts'
    mock_exists.side_effect = lambda path: path.endswith('inet')
    with patch.object(hurd_pfinet_network, 'assign_network_facts', return_value={'key': 'value'}) as mock_assign:
        result = hurd_pfinet_network.populate()
        assert result == {'key': 'value'}
        mock_assign.assert_called_once_with({}, '/bin/fsysopts', '/servers/socket/inet')
