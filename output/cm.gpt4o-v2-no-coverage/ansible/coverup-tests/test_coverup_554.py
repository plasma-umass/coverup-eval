# file: lib/ansible/module_utils/facts/network/generic_bsd.py:281-288
# asked: {"lines": [281, 282, 283, 284, 285, 286, 288], "branches": [[284, 285], [284, 288]]}
# gained: {"lines": [281, 282, 283, 284, 285, 286, 288], "branches": [[284, 285], [284, 288]]}

import pytest
from ansible.module_utils.facts.network.generic_bsd import GenericBsdIfconfigNetwork

class MockModule:
    pass

class TestGenericBsdIfconfigNetwork:
    
    @pytest.fixture
    def network_instance(self):
        return GenericBsdIfconfigNetwork(MockModule())

    def test_get_options_with_valid_string(self, network_instance):
        option_string = "some text <option1,option2,option3> some more text"
        expected_result = ['option1', 'option2', 'option3']
        result = network_instance.get_options(option_string)
        assert result == expected_result

    def test_get_options_with_no_brackets(self, network_instance):
        option_string = "some text option1,option2,option3 some more text"
        expected_result = []
        result = network_instance.get_options(option_string)
        assert result == expected_result

    def test_get_options_with_empty_brackets(self, network_instance):
        option_string = "some text <> some more text"
        expected_result = []
        result = network_instance.get_options(option_string)
        assert result == expected_result

    def test_get_options_with_brackets_but_no_content(self, network_instance):
        option_string = "some text < > some more text"
        expected_result = []
        result = network_instance.get_options(option_string)
        assert result == expected_result

    def test_get_options_with_brackets_and_single_option(self, network_instance):
        option_string = "some text <option1> some more text"
        expected_result = ['option1']
        result = network_instance.get_options(option_string)
        assert result == expected_result
