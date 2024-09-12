# file: lib/ansible/module_utils/facts/network/generic_bsd.py:281-288
# asked: {"lines": [281, 282, 283, 284, 285, 286, 288], "branches": [[284, 285], [284, 288]]}
# gained: {"lines": [281, 282, 283, 284, 285, 286, 288], "branches": [[284, 285], [284, 288]]}

import pytest
from ansible.module_utils.facts.network.generic_bsd import GenericBsdIfconfigNetwork

@pytest.fixture
def network_instance():
    return GenericBsdIfconfigNetwork(module=None)

def test_get_options_with_valid_string(network_instance):
    option_string = "options=<opt1,opt2,opt3>"
    expected_result = ['opt1', 'opt2', 'opt3']
    result = network_instance.get_options(option_string)
    assert result == expected_result

def test_get_options_with_no_options(network_instance):
    option_string = "options=<>"
    expected_result = []
    result = network_instance.get_options(option_string)
    assert result == expected_result

def test_get_options_with_invalid_string(network_instance):
    option_string = "options=opt1,opt2,opt3"
    expected_result = []
    result = network_instance.get_options(option_string)
    assert result == expected_result

def test_get_options_with_partial_options(network_instance):
    option_string = "options=<opt1>"
    expected_result = ['opt1']
    result = network_instance.get_options(option_string)
    assert result == expected_result
