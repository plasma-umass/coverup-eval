# file lib/ansible/module_utils/facts/hardware/aix.py:113-131
# lines [113, 114, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131]
# branches ['120->121', '120->131', '122->123', '122->131', '123->124', '123->131', '125->126', '125->127', '127->128', '127->129', '129->123', '129->130']

import pytest
from unittest.mock import Mock

# Assuming the AIXHardware class is imported from ansible.module_utils.facts.hardware.aix
from ansible.module_utils.facts.hardware.aix import AIXHardware

class MockModule:
    def run_command(self, command):
        if command == "/usr/sbin/lsattr -El sys0 -a fwversion":
            return (0, "fwversion IBM,FW860.50 (SV860_215)", "")
        elif command == "lsconf":
            return (0, "Machine Serial Number: 1234567\nLPAR Info: LPAR123\nSystem Model: IBM,1234", "")
        return (1, "", "Command not found")

    def get_bin_path(self, command):
        if command == "lsconf":
            return "lsconf"
        return None

@pytest.fixture
def mock_module():
    return MockModule()

@pytest.fixture
def aix_hardware(mock_module):
    return AIXHardware(module=mock_module)

def test_get_dmi_facts(aix_hardware):
    dmi_facts = aix_hardware.get_dmi_facts()
    
    assert dmi_facts['firmware_version'] == 'FW860.50'
    assert dmi_facts['product_serial'] == '1234567'
    assert dmi_facts['lpar_info'] == 'LPAR123'
    assert dmi_facts['product_name'] == 'IBM,1234'
