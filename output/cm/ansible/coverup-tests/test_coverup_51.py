# file lib/ansible/module_utils/facts/system/caps.py:25-55
# lines [25, 26, 27, 28, 30, 31, 32, 33, 35, 37, 39, 40, 41, 42, 43, 44, 45, 46, 47, 49, 50, 52, 53, 55]
# branches ['32->33', '32->35', '37->39', '37->55', '42->43', '42->52', '43->44', '43->45', '45->42', '45->46', '46->47', '46->49']

import pytest
from ansible.module_utils.facts.system.caps import SystemCapabilitiesFactCollector

def test_system_capabilities_fact_collector(mocker):
    module_mock = mocker.MagicMock()
    module_mock.get_bin_path.return_value = '/usr/bin/capsh'
    module_mock.run_command.return_value = (0, "Current: =ep\n", "")

    fact_collector = SystemCapabilitiesFactCollector()
    facts = fact_collector.collect(module=module_mock)

    assert facts['system_capabilities_enforced'] == 'False'
    assert facts['system_capabilities'] == []

    module_mock.run_command.return_value = (0, "Current: = cap_sys_admin,cap_net_admin\n", "")
    facts = fact_collector.collect(module=module_mock)

    assert facts['system_capabilities_enforced'] == 'True'
    assert facts['system_capabilities'] == ['cap_sys_admin', 'cap_net_admin']

    module_mock.get_bin_path.return_value = None
    facts = fact_collector.collect(module=module_mock)

    assert facts == {}
