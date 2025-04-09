# file lib/ansible/module_utils/facts/network/aix.py:32-51
# lines [32, 33, 35, 37, 38, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 51]
# branches ['37->38', '37->51', '41->42', '41->51', '43->41', '43->44', '44->45', '44->47', '47->41', '47->48']

import pytest
from unittest.mock import Mock, patch

# Import the AIXNetwork class from the appropriate module
from ansible.module_utils.facts.network.aix import AIXNetwork

class TestAIXNetwork:
    @patch('ansible.module_utils.facts.network.aix.GenericBsdIfconfigNetwork')
    def test_get_default_interfaces(self, MockGenericBsdIfconfigNetwork):
        # Mocking the module and its methods
        mock_module = Mock()
        mock_module.get_bin_path.return_value = '/usr/bin/netstat'
        mock_module.run_command.return_value = (0, 'default 192.168.1.1 UG 0 0 en0\n', '')

        # Creating an instance of AIXNetwork with the mocked module
        network = AIXNetwork(mock_module)

        # Calling the method to test
        v4, v6 = network.get_default_interfaces('/some/path')

        # Assertions to verify the expected output
        assert v4 == {'gateway': '192.168.1.1', 'interface': 'en0'}
        assert v6 == {}

        # Clean up
        mock_module.get_bin_path.assert_called_once_with('netstat')
        mock_module.run_command.assert_called_once_with(['/usr/bin/netstat', '-nr'])

    @patch('ansible.module_utils.facts.network.aix.GenericBsdIfconfigNetwork')
    def test_get_default_interfaces_no_netstat(self, MockGenericBsdIfconfigNetwork):
        # Mocking the module and its methods
        mock_module = Mock()
        mock_module.get_bin_path.return_value = None

        # Creating an instance of AIXNetwork with the mocked module
        network = AIXNetwork(mock_module)

        # Calling the method to test
        v4, v6 = network.get_default_interfaces('/some/path')

        # Assertions to verify the expected output
        assert v4 == {}
        assert v6 == {}

        # Clean up
        mock_module.get_bin_path.assert_called_once_with('netstat')
        mock_module.run_command.assert_not_called()

    @patch('ansible.module_utils.facts.network.aix.GenericBsdIfconfigNetwork')
    def test_get_default_interfaces_ipv6(self, MockGenericBsdIfconfigNetwork):
        # Mocking the module and its methods
        mock_module = Mock()
        mock_module.get_bin_path.return_value = '/usr/bin/netstat'
        mock_module.run_command.return_value = (0, 'default fe80::1 UG 0 0 en1\n', '')

        # Creating an instance of AIXNetwork with the mocked module
        network = AIXNetwork(mock_module)

        # Calling the method to test
        v4, v6 = network.get_default_interfaces('/some/path')

        # Assertions to verify the expected output
        assert v4 == {}
        assert v6 == {'gateway': 'fe80::1', 'interface': 'en1'}

        # Clean up
        mock_module.get_bin_path.assert_called_once_with('netstat')
        mock_module.run_command.assert_called_once_with(['/usr/bin/netstat', '-nr'])
