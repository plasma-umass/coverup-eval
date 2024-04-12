# file lib/ansible/module_utils/facts/network/aix.py:32-51
# lines [32, 33, 35, 37, 38, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 51]
# branches ['37->38', '37->51', '41->42', '41->51', '43->41', '43->44', '44->45', '44->47', '47->41', '47->48']

import pytest
from ansible.module_utils.facts.network.aix import AIXNetwork

class MockModule:
    def get_bin_path(self, bin_name):
        return '/usr/bin/' + bin_name

    def run_command(self, command):
        if 'netstat' in command:
            # Adjust the output to match the expected format with 6 elements per line
            return 0, 'default 192.168.1.1 UGSc 12 34 en0\ndefault 2001:0db8::1 UGSc 12 34 en1', ''
        return 1, '', 'An error occurred'

@pytest.fixture
def mock_module(mocker):
    mock = MockModule()
    mocker.patch.object(mock, 'get_bin_path', return_value='/usr/bin/netstat')
    mocker.patch.object(mock, 'run_command', return_value=(0, 'default 192.168.1.1 UGSc 12 34 en0\ndefault 2001:0db8::1 UGSc 12 34 en1', ''))
    return mock

def test_get_default_interfaces(mock_module):
    aix_network = AIXNetwork(module=mock_module)
    v4, v6 = aix_network.get_default_interfaces(route_path='/usr/bin/netstat')

    assert v4['gateway'] == '192.168.1.1'
    assert v4['interface'] == 'en0'
    assert v6['gateway'] == '2001:0db8::1'
    assert v6['interface'] == 'en1'
    mock_module.run_command.assert_called_with(['/usr/bin/netstat', '-nr'])
