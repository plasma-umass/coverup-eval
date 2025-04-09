# file lib/ansible/module_utils/facts/hardware/sunos.py:168-204
# lines [169, 173, 174, 176, 177, 178, 181, 182, 186, 193, 194, 195, 196, 197, 199, 200, 201, 202, 204]
# branches ['181->182', '181->204', '200->201', '200->204']

import pytest
from unittest.mock import Mock, patch
from ansible.module_utils.facts.hardware.sunos import SunOSHardware

@pytest.fixture
def mock_module():
    module = Mock()
    module.run_command = Mock()
    module.get_bin_path = Mock()
    return module

def test_get_dmi_facts(mock_module):
    hardware = SunOSHardware(module=mock_module)

    # Mock the responses for run_command and get_bin_path
    mock_module.run_command.side_effect = [
        (0, 'i86pc', ''),  # Response for '/usr/bin/uname -i'
        (0, 'System Configuration: Oracle Corporation  Sun Fire X4170 M2', '')  # Response for prtdiag_path
    ]
    mock_module.get_bin_path.return_value = '/usr/platform/i86pc/sbin/prtdiag'

    dmi_facts = hardware.get_dmi_facts()

    # Assertions to verify the expected dmi_facts
    assert dmi_facts['system_vendor'] == 'Oracle Corporation'
    assert dmi_facts['product_name'] == 'Sun Fire X4170 M2'

    # Verify that the run_command and get_bin_path were called with expected arguments
    mock_module.run_command.assert_any_call('/usr/bin/uname -i')
    mock_module.get_bin_path.assert_called_once_with("prtdiag", opt_dirs=['/usr/platform/i86pc/sbin'])
    mock_module.run_command.assert_any_call('/usr/platform/i86pc/sbin/prtdiag')
