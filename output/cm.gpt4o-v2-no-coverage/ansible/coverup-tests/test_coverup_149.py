# file: lib/ansible/module_utils/facts/hardware/sunos.py:168-204
# asked: {"lines": [168, 169, 173, 174, 176, 177, 178, 181, 182, 186, 193, 194, 195, 196, 197, 199, 200, 201, 202, 204], "branches": [[181, 182], [181, 204], [200, 201], [200, 204]]}
# gained: {"lines": [168, 169, 173, 174, 176, 177, 178, 181, 182, 186, 193, 194, 195, 196, 197, 199, 200, 201, 202, 204], "branches": [[181, 182], [181, 204], [200, 201], [200, 204]]}

import pytest
import re
from unittest.mock import Mock, patch
from ansible.module_utils.facts.hardware.sunos import SunOSHardware

@pytest.fixture
def sunos_hardware():
    module = Mock()
    return SunOSHardware(module)

def test_get_dmi_facts_no_output(sunos_hardware):
    sunos_hardware.module.run_command = Mock(return_value=(0, '', ''))
    dmi_facts = sunos_hardware.get_dmi_facts()
    assert dmi_facts == {}

def test_get_dmi_facts_with_output_no_match(sunos_hardware):
    sunos_hardware.module.run_command = Mock(side_effect=[
        (0, 'i86pc', ''),
        (0, 'Some random output\n', '')
    ])
    dmi_facts = sunos_hardware.get_dmi_facts()
    assert dmi_facts == {}

def test_get_dmi_facts_with_output_match(sunos_hardware):
    sunos_hardware.module.run_command = Mock(side_effect=[
        (0, 'i86pc', ''),
        (0, 'System Configuration: Oracle Corporation  Sun Fire X4170 M2\n', '')
    ])
    dmi_facts = sunos_hardware.get_dmi_facts()
    assert dmi_facts == {
        'system_vendor': 'Oracle Corporation',
        'product_name': 'Sun Fire X4170 M2'
    }

def test_get_dmi_facts_prtdiag_not_found(sunos_hardware):
    sunos_hardware.module.run_command = Mock(side_effect=[
        (0, 'i86pc', ''),
        (1, '', 'prtdiag: not found')
    ])
    sunos_hardware.module.get_bin_path = Mock(return_value=None)
    dmi_facts = sunos_hardware.get_dmi_facts()
    assert dmi_facts == {}
