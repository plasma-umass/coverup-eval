# file lib/ansible/module_utils/common/network.py:64-83
# lines [64, 66, 67, 68, 69, 70, 71, 72, 74, 75, 77, 78, 79, 81, 82, 83]
# branches ['67->68', '67->69', '78->79', '78->81', '81->82', '81->83']

import pytest
from unittest.mock import patch

# Assuming the functions `is_masklen`, `to_netmask`, and `to_masklen` are defined in the same module
from ansible.module_utils.common.network import to_subnet

@pytest.fixture
def mock_is_masklen(mocker):
    return mocker.patch('ansible.module_utils.common.network.is_masklen')

@pytest.fixture
def mock_to_netmask(mocker):
    return mocker.patch('ansible.module_utils.common.network.to_netmask')

@pytest.fixture
def mock_to_masklen(mocker):
    return mocker.patch('ansible.module_utils.common.network.to_masklen')

def test_to_subnet_valid_masklen(mock_is_masklen, mock_to_netmask):
    mock_is_masklen.return_value = True
    mock_to_netmask.return_value = '255.255.255.0'
    
    result = to_subnet('192.168.1.1', '24')
    assert result == '192.168.1.0/24'

def test_to_subnet_invalid_masklen(mock_is_masklen, mock_to_netmask, mock_to_masklen):
    mock_is_masklen.return_value = False
    mock_to_netmask.side_effect = ValueError
    mock_to_masklen.return_value = 24
    
    result = to_subnet('192.168.1.1', '255.255.255.0')
    assert result == '192.168.1.0/24'

def test_to_subnet_dotted_notation(mock_is_masklen, mock_to_netmask):
    mock_is_masklen.return_value = True
    mock_to_netmask.return_value = '255.255.255.0'
    
    result = to_subnet('192.168.1.1', '24', dotted_notation=True)
    assert result == '192.168.1.0 255.255.255.0'
