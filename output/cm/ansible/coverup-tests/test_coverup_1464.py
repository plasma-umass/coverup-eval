# file lib/ansible/module_utils/facts/network/generic_bsd.py:66-71
# lines []
# branches ['68->67']

import pytest
from unittest.mock import MagicMock
from ansible.module_utils.facts.network.generic_bsd import GenericBsdIfconfigNetwork

@pytest.fixture
def mock_interfaces():
    return {
        'em0': {
            'media': 'Ethernet autoselect (1000baseT <full-duplex>)'
        },
        'em1': {
            'media': 'Ethernet autoselect'
        },
        'lo0': {
            'other_data': 'loopback'
        }
    }

@pytest.fixture
def mock_module():
    mock = MagicMock()
    return mock

def test_detect_type_media_with_ether(mock_interfaces, mock_module):
    network = GenericBsdIfconfigNetwork(mock_module)
    result = network.detect_type_media(mock_interfaces)
    assert result['em0']['type'] == 'ether'
    assert 'type' not in result['lo0']
    # The 'em1' interface should have 'type' set to 'ether' since it contains 'media'
    assert result['em1']['type'] == 'ether'

def test_detect_type_media_without_ether(mock_interfaces, mock_module):
    # Modify the 'em0' interface to not include 'ether' in the media
    mock_interfaces['em0']['media'] = 'Fiber autoselect (1000baseSX <full-duplex>)'
    # Remove 'media' key from 'em1' to simulate an interface without 'media' information
    del mock_interfaces['em1']['media']
    network = GenericBsdIfconfigNetwork(mock_module)
    result = network.detect_type_media(mock_interfaces)
    assert 'type' not in result['em0']
    assert 'type' not in result['lo0']
    # Since 'em1' no longer has 'media', it should not have 'type'
    assert 'type' not in result['em1']
