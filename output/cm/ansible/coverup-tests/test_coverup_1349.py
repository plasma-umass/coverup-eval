# file lib/ansible/module_utils/facts/system/caps.py:25-55
# lines [33, 44]
# branches ['32->33', '43->44', '45->42']

import pytest
from ansible.module_utils.facts.system.caps import SystemCapabilitiesFactCollector

def test_system_capabilities_fact_collector(mocker):
    module_mock = mocker.MagicMock()
    module_mock.get_bin_path.side_effect = ['/usr/bin/capsh', '/usr/bin/capsh', '/usr/bin/capsh', None]
    module_mock.run_command.side_effect = [
        (0, 'Current:=ep\n', ''),
        (0, 'Current: = cap_sys_admin,cap_net_admin\n', ''),
        (0, '\nCurrent: = cap_sys_admin,cap_net_admin\n', ''),
    ]

    collector = SystemCapabilitiesFactCollector()

    # Test when capsh output is 'Current:=ep'
    facts = collector.collect(module=module_mock)
    assert facts['system_capabilities_enforced'] == 'False'
    assert facts['system_capabilities'] == []

    # Test when capsh output includes capabilities
    facts = collector.collect(module=module_mock)
    assert facts['system_capabilities_enforced'] == 'True'
    assert facts['system_capabilities'] == ['cap_sys_admin', 'cap_net_admin']

    # Test when capsh output includes capabilities with a leading newline
    facts = collector.collect(module=module_mock)
    assert facts['system_capabilities_enforced'] == 'True'
    assert facts['system_capabilities'] == ['cap_sys_admin', 'cap_net_admin']

    # Test when capsh is not found
    facts = collector.collect(module=module_mock)
    assert facts == {}
