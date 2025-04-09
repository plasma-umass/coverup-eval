# file lib/ansible/module_utils/facts/hardware/sunos.py:168-204
# lines []
# branches ['181->204', '200->204']

import re
import pytest
from unittest.mock import MagicMock

# Assuming the SunOSHardware class is defined in a module named sunos
from ansible.module_utils.facts.hardware import sunos

@pytest.fixture
def mock_module(mocker):
    mock_module = mocker.MagicMock()
    mock_module.run_command = MagicMock()
    mock_module.get_bin_path = MagicMock()
    return mock_module

def test_get_dmi_facts_with_output(mock_module):
    hardware = sunos.SunOSHardware(module=mock_module)
    
    # Mock uname command
    mock_module.run_command.side_effect = [
        (0, "some-platform", ""),
        (1, "System Configuration: Oracle Corporation sun4v SPARC T4-1", "")
    ]
    
    # Mock prtdiag path
    mock_module.get_bin_path.return_value = "/usr/platform/some-platform/sbin/prtdiag"
    
    dmi_facts = hardware.get_dmi_facts()
    
    assert dmi_facts['system_vendor'] == "Oracle Corporation"
    assert dmi_facts['product_name'] == "SPARC T4-1"
    mock_module.run_command.assert_called_with("/usr/platform/some-platform/sbin/prtdiag")

def test_get_dmi_facts_without_output(mock_module):
    hardware = sunos.SunOSHardware(module=mock_module)
    
    # Mock uname command
    mock_module.run_command.side_effect = [
        (0, "some-platform", ""),
        (1, "", "")  # No output for prtdiag command
    ]
    
    # Mock prtdiag path
    mock_module.get_bin_path.return_value = "/usr/platform/some-platform/sbin/prtdiag"
    
    dmi_facts = hardware.get_dmi_facts()
    
    assert 'system_vendor' not in dmi_facts
    assert 'product_name' not in dmi_facts
    mock_module.run_command.assert_called_with("/usr/platform/some-platform/sbin/prtdiag")
