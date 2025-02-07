# file: lib/ansible/module_utils/facts/hardware/sunos.py:168-204
# asked: {"lines": [168, 169, 173, 174, 176, 177, 178, 181, 182, 186, 193, 194, 195, 196, 197, 199, 200, 201, 202, 204], "branches": [[181, 182], [181, 204], [200, 201], [200, 204]]}
# gained: {"lines": [168, 169, 173, 174, 176, 177, 178, 181, 182, 186, 193, 194, 195, 196, 197, 199, 200, 201, 202, 204], "branches": [[181, 182], [181, 204], [200, 201], [200, 204]]}

import pytest
import re
from unittest.mock import Mock, patch
from ansible.module_utils.facts.hardware.sunos import SunOSHardware

@pytest.fixture
def mock_module():
    return Mock()

@pytest.fixture
def sunos_hardware(mock_module):
    return SunOSHardware(module=mock_module)

def test_get_dmi_facts_no_prtdiag(sunos_hardware, mock_module):
    mock_module.run_command.side_effect = [
        (0, 'i86pc', ''),  # uname -i
        (1, '', 'prtdiag not found')  # prtdiag
    ]
    mock_module.get_bin_path.return_value = '/usr/platform/i86pc/sbin/prtdiag'

    dmi_facts = sunos_hardware.get_dmi_facts()

    assert dmi_facts == {}
    mock_module.run_command.assert_any_call('/usr/bin/uname -i')
    mock_module.run_command.assert_any_call('/usr/platform/i86pc/sbin/prtdiag')

def test_get_dmi_facts_with_output(sunos_hardware, mock_module):
    mock_module.run_command.side_effect = [
        (0, 'i86pc', ''),  # uname -i
        (0, 'System Configuration: Oracle Corporation  Sun Fire X4170 M2', '')  # prtdiag
    ]
    mock_module.get_bin_path.return_value = '/usr/platform/i86pc/sbin/prtdiag'

    dmi_facts = sunos_hardware.get_dmi_facts()

    assert dmi_facts == {
        'system_vendor': 'Oracle Corporation',
        'product_name': 'Sun Fire X4170 M2'
    }
    mock_module.run_command.assert_any_call('/usr/bin/uname -i')
    mock_module.run_command.assert_any_call('/usr/platform/i86pc/sbin/prtdiag')

def test_get_dmi_facts_with_unknown_vendor(sunos_hardware, mock_module):
    mock_module.run_command.side_effect = [
        (0, 'i86pc', ''),  # uname -i
        (0, 'System Configuration: Unknown Vendor  Unknown Product', '')  # prtdiag
    ]
    mock_module.get_bin_path.return_value = '/usr/platform/i86pc/sbin/prtdiag'

    dmi_facts = sunos_hardware.get_dmi_facts()

    assert dmi_facts == {}
    mock_module.run_command.assert_any_call('/usr/bin/uname -i')
    mock_module.run_command.assert_any_call('/usr/platform/i86pc/sbin/prtdiag')
