# file lib/ansible/module_utils/facts/hardware/freebsd.py:191-236
# lines [229, 230, 232, 234]
# branches ['221->234', '223->232']

import pytest
from unittest.mock import Mock, patch

@pytest.fixture
def mock_module():
    module = Mock()
    module.get_bin_path.return_value = '/usr/sbin/dmidecode'
    return module

@pytest.fixture
def freebsd_hardware(mock_module):
    from ansible.module_utils.facts.hardware.freebsd import FreeBSDHardware
    hw = FreeBSDHardware(mock_module)
    return hw

def test_get_dmi_facts_unicode_decode_error(freebsd_hardware, mocker):
    mocker.patch('ansible.module_utils.facts.hardware.freebsd.json.dumps', side_effect=UnicodeDecodeError('utf-8', b"", 0, 1, ''))
    freebsd_hardware.module.run_command.return_value = (0, 'some output', '')

    dmi_facts = freebsd_hardware.get_dmi_facts()

    assert dmi_facts['bios_date'] == 'NA'

def test_get_dmi_facts_non_zero_rc(freebsd_hardware):
    freebsd_hardware.module.run_command.return_value = (1, '', 'error')

    dmi_facts = freebsd_hardware.get_dmi_facts()

    assert dmi_facts['bios_date'] == 'NA'

def test_get_dmi_facts_no_dmidecode(freebsd_hardware):
    freebsd_hardware.module.get_bin_path.return_value = None

    dmi_facts = freebsd_hardware.get_dmi_facts()

    assert dmi_facts['bios_date'] == 'NA'
