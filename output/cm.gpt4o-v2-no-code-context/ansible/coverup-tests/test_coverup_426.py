# file: lib/ansible/module_utils/facts/hardware/hpux.py:41-52
# asked: {"lines": [41, 42, 44, 45, 46, 48, 49, 50, 52], "branches": []}
# gained: {"lines": [41, 42, 44, 45, 46, 48, 49, 50, 52], "branches": []}

import pytest
from unittest.mock import patch, Mock

# Assuming the HPUXHardware class and its methods are imported from the module
from ansible.module_utils.facts.hardware.hpux import HPUXHardware

@pytest.fixture
def hpux_hardware():
    module_mock = Mock()
    return HPUXHardware(module=module_mock)

def test_populate_with_collected_facts(hpux_hardware, mocker):
    mocker.patch.object(hpux_hardware, 'get_cpu_facts', return_value={'cpu': 'facts'})
    mocker.patch.object(hpux_hardware, 'get_memory_facts', return_value={'memory': 'facts'})
    mocker.patch.object(hpux_hardware, 'get_hw_facts', return_value={'hw': 'facts'})

    collected_facts = {'some': 'facts'}
    result = hpux_hardware.populate(collected_facts=collected_facts)

    assert result == {'cpu': 'facts', 'memory': 'facts', 'hw': 'facts'}

def test_populate_without_collected_facts(hpux_hardware, mocker):
    mocker.patch.object(hpux_hardware, 'get_cpu_facts', return_value={'cpu': 'facts'})
    mocker.patch.object(hpux_hardware, 'get_memory_facts', return_value={'memory': 'facts'})
    mocker.patch.object(hpux_hardware, 'get_hw_facts', return_value={'hw': 'facts'})

    result = hpux_hardware.populate()

    assert result == {'cpu': 'facts', 'memory': 'facts', 'hw': 'facts'}
