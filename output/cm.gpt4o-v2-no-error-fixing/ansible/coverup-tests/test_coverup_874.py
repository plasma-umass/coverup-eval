# file: lib/ansible/module_utils/facts/network/hurd.py:64-82
# asked: {"lines": [65, 67, 68, 69, 71, 73, 74, 75, 76, 77, 79, 80, 82], "branches": [[68, 69], [68, 71], [73, 74], [73, 79], [75, 73], [75, 76], [79, 80], [79, 82]]}
# gained: {"lines": [65, 67, 68, 69, 71, 73, 74, 75, 76, 77, 79, 80, 82], "branches": [[68, 69], [68, 71], [73, 74], [73, 79], [75, 73], [75, 76], [79, 80], [79, 82]]}

import os
import pytest
from unittest.mock import MagicMock, patch
from ansible.module_utils.facts.network.hurd import HurdPfinetNetwork

@pytest.fixture
def hurd_pfinet_network():
    module = MagicMock()
    network = HurdPfinetNetwork(module)
    network._socket_dir = '/mock/socket/dir'
    return network

def test_populate_no_fsysopts_path(hurd_pfinet_network):
    hurd_pfinet_network.module.get_bin_path.return_value = None
    result = hurd_pfinet_network.populate()
    assert result == {}

def test_populate_no_socket_path(hurd_pfinet_network):
    hurd_pfinet_network.module.get_bin_path.return_value = '/mock/fsysopts'
    with patch('os.path.exists', return_value=False):
        result = hurd_pfinet_network.populate()
        assert result == {}

def test_populate_with_socket_path(hurd_pfinet_network):
    hurd_pfinet_network.module.get_bin_path.return_value = '/mock/fsysopts'
    with patch('os.path.exists', side_effect=lambda x: x == '/mock/socket/dir/inet'):
        with patch.object(hurd_pfinet_network, 'assign_network_facts', return_value={'mock': 'facts'}) as mock_assign:
            result = hurd_pfinet_network.populate()
            assert result == {'mock': 'facts'}
            mock_assign.assert_called_once_with({}, '/mock/fsysopts', '/mock/socket/dir/inet')
