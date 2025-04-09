# file: lib/ansible/module_utils/facts/hardware/sunos.py:168-204
# asked: {"lines": [168, 169, 173, 174, 176, 177, 178, 181, 182, 186, 193, 194, 195, 196, 197, 199, 200, 201, 202, 204], "branches": [[181, 182], [181, 204], [200, 201], [200, 204]]}
# gained: {"lines": [168, 169, 173, 174, 176, 177, 178, 181, 182, 186, 193, 194, 195, 196, 197, 199, 200, 201, 202, 204], "branches": [[181, 182], [181, 204], [200, 201], [200, 204]]}

import pytest
import re
from unittest.mock import Mock, patch
from ansible.module_utils.facts.hardware.sunos import SunOSHardware

@pytest.fixture
def module():
    return Mock()

@pytest.fixture
def sunos_hardware(module):
    return SunOSHardware(module)

def test_get_dmi_facts_no_prtdiag(monkeypatch, sunos_hardware):
    def mock_run_command(cmd):
        if cmd == '/usr/bin/uname -i':
            return 0, 'i86pc', ''
        elif 'prtdiag' in cmd:
            return 1, '', 'prtdiag: not found'
        return 1, '', 'command not found'

    monkeypatch.setattr(sunos_hardware.module, 'run_command', mock_run_command)
    monkeypatch.setattr(sunos_hardware.module, 'get_bin_path', lambda x, opt_dirs=None: '/usr/platform/i86pc/sbin/prtdiag')

    dmi_facts = sunos_hardware.get_dmi_facts()
    assert dmi_facts == {}

def test_get_dmi_facts_with_prtdiag_output(monkeypatch, sunos_hardware):
    prtdiag_output = "System Configuration: Oracle Corporation  Sun Fire X4170 M2\n"

    def mock_run_command(cmd):
        if cmd == '/usr/bin/uname -i':
            return 0, 'i86pc', ''
        elif 'prtdiag' in cmd:
            return 0, prtdiag_output, ''
        return 1, '', 'command not found'

    monkeypatch.setattr(sunos_hardware.module, 'run_command', mock_run_command)
    monkeypatch.setattr(sunos_hardware.module, 'get_bin_path', lambda x, opt_dirs=None: '/usr/platform/i86pc/sbin/prtdiag')

    dmi_facts = sunos_hardware.get_dmi_facts()
    assert dmi_facts == {
        'system_vendor': 'Oracle Corporation',
        'product_name': 'Sun Fire X4170 M2'
    }

def test_get_dmi_facts_with_prtdiag_no_match(monkeypatch, sunos_hardware):
    prtdiag_output = "System Configuration: Unknown Vendor Unknown Product\n"

    def mock_run_command(cmd):
        if cmd == '/usr/bin/uname -i':
            return 0, 'i86pc', ''
        elif 'prtdiag' in cmd:
            return 0, prtdiag_output, ''
        return 1, '', 'command not found'

    monkeypatch.setattr(sunos_hardware.module, 'run_command', mock_run_command)
    monkeypatch.setattr(sunos_hardware.module, 'get_bin_path', lambda x, opt_dirs=None: '/usr/platform/i86pc/sbin/prtdiag')

    dmi_facts = sunos_hardware.get_dmi_facts()
    assert dmi_facts == {}
