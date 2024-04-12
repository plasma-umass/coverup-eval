# file lib/ansible/module_utils/facts/network/generic_bsd.py:281-288
# lines [281, 282, 283, 284, 285, 286, 288]
# branches ['284->285', '284->288']

import pytest
from unittest.mock import MagicMock
from ansible.module_utils.facts.network.generic_bsd import GenericBsdIfconfigNetwork

@pytest.fixture
def generic_bsd_ifconfig_network():
    module_mock = MagicMock()
    return GenericBsdIfconfigNetwork(module=module_mock)

def test_get_options_with_valid_option_string(generic_bsd_ifconfig_network):
    option_string = "options=<OPT1,OPT2,OPT3>"
    expected_options = ["OPT1", "OPT2", "OPT3"]
    options = generic_bsd_ifconfig_network.get_options(option_string)
    assert options == expected_options

def test_get_options_with_no_options(generic_bsd_ifconfig_network):
    option_string = "options=<>"
    expected_options = []
    options = generic_bsd_ifconfig_network.get_options(option_string)
    assert options == expected_options

def test_get_options_with_invalid_option_string(generic_bsd_ifconfig_network):
    option_string = "options=<>"
    expected_options = []
    options = generic_bsd_ifconfig_network.get_options(option_string)
    assert options == expected_options

def test_get_options_with_no_closing_bracket(generic_bsd_ifconfig_network):
    option_string = "options=<OPT1,OPT2,OPT3"
    expected_options = []
    options = generic_bsd_ifconfig_network.get_options(option_string)
    assert options == expected_options

def test_get_options_with_no_opening_bracket(generic_bsd_ifconfig_network):
    option_string = "options=OPT1,OPT2,OPT3>"
    expected_options = []
    options = generic_bsd_ifconfig_network.get_options(option_string)
    assert options == expected_options

def test_get_options_with_empty_string(generic_bsd_ifconfig_network):
    option_string = ""
    expected_options = []
    options = generic_bsd_ifconfig_network.get_options(option_string)
    assert options == expected_options
