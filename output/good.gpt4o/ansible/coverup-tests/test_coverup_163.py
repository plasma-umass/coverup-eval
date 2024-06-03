# file lib/ansible/module_utils/facts/network/hurd.py:64-82
# lines [64, 65, 67, 68, 69, 71, 73, 74, 75, 76, 77, 79, 80, 82]
# branches ['68->69', '68->71', '73->74', '73->79', '75->73', '75->76', '79->80', '79->82']

import os
import pytest
from unittest.mock import patch, MagicMock

# Assuming the HurdPfinetNetwork class is imported from the module
from ansible.module_utils.facts.network.hurd import HurdPfinetNetwork

@pytest.fixture
def mock_module():
    return MagicMock()

@pytest.fixture
def hurd_pfinet_network(mock_module):
    return HurdPfinetNetwork(module=mock_module)

def test_populate_no_fsysopts_path(hurd_pfinet_network, mock_module):
    mock_module.get_bin_path.return_value = None
    result = hurd_pfinet_network.populate()
    assert result == {}

def test_populate_no_socket_path(hurd_pfinet_network, mock_module):
    mock_module.get_bin_path.return_value = '/usr/bin/fsysopts'
    with patch('os.path.exists', return_value=False):
        result = hurd_pfinet_network.populate()
        assert result == {}

def test_populate_with_socket_path(hurd_pfinet_network, mock_module):
    mock_module.get_bin_path.return_value = '/usr/bin/fsysopts'
    with patch('os.path.exists', side_effect=lambda x: x.endswith('inet')):
        with patch.object(HurdPfinetNetwork, 'assign_network_facts', return_value={'key': 'value'}) as mock_assign:
            result = hurd_pfinet_network.populate()
            assert result == {'key': 'value'}
            mock_assign.assert_called_once_with({}, '/usr/bin/fsysopts', os.path.join(hurd_pfinet_network._socket_dir, 'inet'))
