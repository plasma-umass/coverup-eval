# file lib/ansible/module_utils/facts/network/aix.py:32-51
# lines []
# branches ['37->51', '43->41', '47->41']

import pytest
from ansible.module_utils.facts.network.aix import AIXNetwork

@pytest.fixture
def mock_module(mocker):
    mock_module = mocker.MagicMock()
    mock_module.get_bin_path.return_value = '/usr/bin/netstat'
    return mock_module

def test_get_default_interfaces_ipv4_ipv6(mocker, mock_module):
    mocker.patch('ansible.module_utils.facts.network.aix.GenericBsdIfconfigNetwork')
    aix_network = AIXNetwork(mock_module)

    # Mock the run_command method to return sample netstat output
    sample_output = (
        "Routing tables\n"
        "Destination        Gateway           Flags   Refs     Use  If   Exp  Groups\n"
        "Route Tree for Protocol Family 2 (Internet):\n"
        "default            192.168.1.1       UG        2    123456  en0\n"
        "default            2001:0db8::1      UG        1     65432  en1\n"
    )
    mock_module.run_command.return_value = (0, sample_output, '')

    ipv4, ipv6 = aix_network.get_default_interfaces('/usr/bin/netstat')

    # Assertions to check if the correct default gateway and interface are set for IPv4 and IPv6
    assert ipv4['gateway'] == '192.168.1.1'
    assert ipv4['interface'] == 'en0'
    assert ipv6['gateway'] == '2001:0db8::1'
    assert ipv6['interface'] == 'en1'

    # Cleanup is not necessary as we are using mocks and not affecting the real system state
