# file lib/ansible/module_utils/facts/hardware/sunos.py:168-204
# lines [168, 169, 173, 174, 176, 177, 178, 181, 182, 186, 193, 194, 195, 196, 197, 199, 200, 201, 202, 204]
# branches ['181->182', '181->204', '200->201', '200->204']

import re
import pytest
from unittest.mock import MagicMock

# Assuming the SunOSHardware class is part of a module named sunos
from ansible.module_utils.facts.hardware import sunos

@pytest.fixture
def mock_module(mocker):
    mock = MagicMock()
    mock.run_command = MagicMock(side_effect=[
        (0, 'sun4v', ''),  # uname -i command
        (1, 'System Configuration: Oracle Corporation sun4v SPARC T4-1', '')  # prtdiag command
    ])
    mock.get_bin_path = MagicMock(return_value='/usr/platform/sun4v/sbin/prtdiag')
    return mock

def test_get_dmi_facts_with_prtdiag_output(mock_module):
    hardware = sunos.SunOSHardware(module=mock_module)
    dmi_facts = hardware.get_dmi_facts()

    assert dmi_facts['system_vendor'] == 'Oracle Corporation'
    assert dmi_facts['product_name'] == 'SPARC T4-1'

    # Verify that run_command was called with the expected commands
    mock_module.run_command.assert_any_call('/usr/bin/uname -i')
    mock_module.run_command.assert_any_call('/usr/platform/sun4v/sbin/prtdiag')

    # Verify that get_bin_path was called with the expected arguments
    mock_module.get_bin_path.assert_called_once_with("prtdiag", opt_dirs=['/usr/platform/sun4v/sbin'])
