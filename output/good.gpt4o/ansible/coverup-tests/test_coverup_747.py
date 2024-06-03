# file lib/ansible/module_utils/facts/hardware/openbsd.py:31-47
# lines [31, 32, 46]
# branches []

import pytest
from ansible.module_utils.facts.hardware.openbsd import OpenBSDHardware
from ansible.module_utils.basic import AnsibleModule

@pytest.fixture
def mock_module(mocker):
    return mocker.Mock(spec=AnsibleModule)

def test_openbsd_hardware_initialization(mock_module):
    hardware = OpenBSDHardware(mock_module)
    assert hardware.platform == 'OpenBSD'
