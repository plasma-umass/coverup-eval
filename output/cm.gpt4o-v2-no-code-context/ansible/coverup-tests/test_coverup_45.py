# file: lib/ansible/module_utils/facts/network/linux.py:64-97
# asked: {"lines": [64, 65, 70, 71, 72, 74, 76, 77, 78, 79, 80, 81, 82, 83, 86, 87, 89, 90, 91, 92, 93, 94, 95, 96, 97], "branches": [[76, 77], [76, 97], [77, 79], [77, 80], [80, 81], [80, 82], [83, 86], [83, 87], [89, 76], [89, 90], [90, 76], [90, 91], [91, 92], [91, 93], [93, 94], [93, 95], [95, 90], [95, 96]]}
# gained: {"lines": [64, 65, 70, 71, 72, 74, 76, 77, 78, 79, 80, 82, 83, 86, 87, 89, 90, 91, 92, 93, 94, 95, 96, 97], "branches": [[76, 77], [76, 97], [77, 79], [77, 80], [80, 82], [83, 86], [83, 87], [89, 76], [89, 90], [90, 76], [90, 91], [91, 92], [91, 93], [93, 94], [93, 95], [95, 90], [95, 96]]}

import pytest
from unittest.mock import patch, MagicMock
from ansible.module_utils.facts.network.linux import LinuxNetwork

class TestLinuxNetwork:
    @pytest.fixture
    def linux_network(self, mock_module):
        return LinuxNetwork(mock_module)

    @pytest.fixture
    def mock_module(self):
        return MagicMock()

    @pytest.fixture
    def mock_socket(self, monkeypatch):
        mock_socket = MagicMock()
        monkeypatch.setattr("socket.has_ipv6", True)
        return mock_socket

    def test_get_default_interfaces_v4(self, linux_network, mock_module):
        linux_network.module = mock_module
        mock_module.run_command.return_value = (0, "8.8.8.8 via 192.168.1.1 dev eth0 src 192.168.1.2", "")

        v4, v6 = linux_network.get_default_interfaces("/sbin/ip")

        assert v4 == {'interface': 'eth0', 'address': '192.168.1.2', 'gateway': '192.168.1.1'}
        assert v6 == {}

    def test_get_default_interfaces_v6(self, linux_network, mock_module, mock_socket):
        linux_network.module = mock_module
        mock_module.run_command.side_effect = [
            (0, "8.8.8.8 via 192.168.1.1 dev eth0 src 192.168.1.2", ""),
            (0, "2404:6800:400a:800::1012 dev eth1 src 2404:6800:400a:800::1013", "")
        ]

        v4, v6 = linux_network.get_default_interfaces("/sbin/ip")

        assert v4 == {'interface': 'eth0', 'address': '192.168.1.2', 'gateway': '192.168.1.1'}
        assert v6 == {'interface': 'eth1', 'address': '2404:6800:400a:800::1013'}

    def test_get_default_interfaces_no_output(self, linux_network, mock_module):
        linux_network.module = mock_module
        mock_module.run_command.return_value = (0, "", "")

        v4, v6 = linux_network.get_default_interfaces("/sbin/ip")

        assert v4 == {}
        assert v6 == {}

    def test_get_default_interfaces_invalid_output(self, linux_network, mock_module):
        linux_network.module = mock_module
        mock_module.run_command.return_value = (0, "invalid output", "")

        v4, v6 = linux_network.get_default_interfaces("/sbin/ip")

        assert v4 == {}
        assert v6 == {}

    def test_get_default_interfaces_redhat_v6_skip(self, linux_network, mock_module):
        linux_network.module = mock_module
        collected_facts = {
            'ansible_os_family': 'RedHat',
            'ansible_distribution_version': '4.8'
        }
        mock_module.run_command.return_value = (0, "8.8.8.8 via 192.168.1.1 dev eth0 src 192.168.1.2", "")

        v4, v6 = linux_network.get_default_interfaces("/sbin/ip", collected_facts)

        assert v4 == {'interface': 'eth0', 'address': '192.168.1.2', 'gateway': '192.168.1.1'}
        assert v6 == {}
