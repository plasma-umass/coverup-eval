# file lib/ansible/module_utils/facts/hardware/sunos.py:206-265
# lines [206, 222, 223, 225, 226, 227, 228, 229, 230, 231, 232, 233, 234, 235, 236, 239, 241, 242, 244, 245, 246, 247, 249, 250, 251, 252, 253, 254, 256, 257, 259, 261, 262, 263, 265]
# branches ['241->242', '241->244', '246->247', '246->249', '250->251', '250->265', '252->253', '252->261', '256->257', '256->259']

import pytest
from ansible.module_utils.facts.hardware.sunos import SunOSHardware

@pytest.fixture
def mock_module(mocker):
    mock_module = mocker.MagicMock()
    mock_module.run_command = mocker.MagicMock(return_value=(0, 
        'sderr:0:sd0,err:Hard Errors\t0\n'
        'sderr:0:sd0,err:Illegal Request\t6\n'
        'sderr:0:sd0,err:Media Error\t0\n'
        'sderr:0:sd0,err:Predictive Failure Analysis\t0\n'
        'sderr:0:sd0,err:Product\tVBOX HARDDISK\n'
        'sderr:0:sd0,err:Revision\t1.0\n'
        'sderr:0:sd0,err:Serial No\tVB0ad2ec4d-074a\n'
        'sderr:0:sd0,err:Size\t53687091200\n'
        'sderr:0:sd0,err:Soft Errors\t0\n'
        'sderr:0:sd0,err:Transport Errors\t0\n'
        'sderr:0:sd0,err:Vendor\tATA', ''))
    return mock_module

def test_get_device_facts(mock_module):
    hardware = SunOSHardware(module=mock_module)
    device_facts = hardware.get_device_facts()

    assert 'devices' in device_facts
    assert 'sd0' in device_facts['devices']
    assert device_facts['devices']['sd0']['product'] == 'VBOX HARDDISK'
    assert device_facts['devices']['sd0']['revision'] == '1.0'
    assert device_facts['devices']['sd0']['serial'] == 'VB0ad2ec4d-074a'
    assert device_facts['devices']['sd0']['size'] == '50.00 GB'
    assert device_facts['devices']['sd0']['vendor'] == 'ATA'
    assert device_facts['devices']['sd0']['hard_errors'] == '0'
    assert device_facts['devices']['sd0']['soft_errors'] == '0'
    assert device_facts['devices']['sd0']['transport_errors'] == '0'
    assert device_facts['devices']['sd0']['media_errors'] == '0'
    assert device_facts['devices']['sd0']['predictive_failure_analysis'] == '0'
    assert device_facts['devices']['sd0']['illegal_request'] == '6'
