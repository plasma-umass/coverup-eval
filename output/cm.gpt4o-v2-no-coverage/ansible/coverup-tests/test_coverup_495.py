# file: lib/ansible/module_utils/facts/hardware/darwin.py:69-77
# asked: {"lines": [69, 70, 71, 72, 73, 74, 75, 77], "branches": [[72, 73], [72, 74]]}
# gained: {"lines": [69, 70, 71, 72, 73, 74, 75, 77], "branches": [[72, 73], [72, 74]]}

import pytest
from unittest.mock import Mock, patch
from ansible.module_utils.facts.hardware.darwin import DarwinHardware
from ansible.module_utils.facts.hardware.base import Hardware

@pytest.fixture
def mock_module():
    return Mock()

@pytest.fixture
def darwin_hardware(mock_module):
    dh = DarwinHardware(module=mock_module)
    dh.sysctl = {
        'kern.osversion': '20.3.0',
        'kern.osrevision': '199506'
    }
    return dh

def test_get_mac_facts_success(darwin_hardware, mock_module):
    mock_module.run_command.return_value = (0, 'hw.model: MacBookPro16,1', '')
    
    mac_facts = darwin_hardware.get_mac_facts()
    
    assert mac_facts['model'] == 'MacBookPro16,1'
    assert mac_facts['product_name'] == 'MacBookPro16,1'
    assert mac_facts['osversion'] == '20.3.0'
    assert mac_facts['osrevision'] == '199506'

def test_get_mac_facts_failure(darwin_hardware, mock_module):
    mock_module.run_command.return_value = (1, '', 'error')
    
    mac_facts = darwin_hardware.get_mac_facts()
    
    assert 'model' not in mac_facts
    assert 'product_name' not in mac_facts
    assert mac_facts['osversion'] == '20.3.0'
    assert mac_facts['osrevision'] == '199506'
