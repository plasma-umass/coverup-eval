# file: lib/ansible/module_utils/facts/network/generic_bsd.py:281-288
# asked: {"lines": [281, 282, 283, 284, 285, 286, 288], "branches": [[284, 285], [284, 288]]}
# gained: {"lines": [281, 282, 283, 284, 285, 286, 288], "branches": [[284, 285], [284, 288]]}

import pytest
from ansible.module_utils.facts.network.generic_bsd import GenericBsdIfconfigNetwork
from ansible.module_utils.basic import AnsibleModule

class TestGenericBsdIfconfigNetwork:
    @pytest.fixture
    def network_instance(self, mocker):
        mock_module = mocker.Mock(spec=AnsibleModule)
        return GenericBsdIfconfigNetwork(mock_module)

    def test_get_options_with_valid_option_string(self, network_instance):
        option_string = "some text <option1,option2,option3> some more text"
        expected_result = ['option1', 'option2', 'option3']
        result = network_instance.get_options(option_string)
        assert result == expected_result

    def test_get_options_with_no_options(self, network_instance):
        option_string = "some text <> some more text"
        expected_result = []
        result = network_instance.get_options(option_string)
        assert result == expected_result

    def test_get_options_with_no_brackets(self, network_instance):
        option_string = "some text with no brackets"
        expected_result = []
        result = network_instance.get_options(option_string)
        assert result == expected_result

    def test_get_options_with_only_start_bracket(self, network_instance):
        option_string = "some text < with only start bracket"
        expected_result = []
        result = network_instance.get_options(option_string)
        assert result == expected_result

    def test_get_options_with_only_end_bracket(self, network_instance):
        option_string = "some text with only end bracket>"
        expected_result = []
        result = network_instance.get_options(option_string)
        assert result == expected_result

    def test_get_options_with_brackets_but_no_content(self, network_instance):
        option_string = "some text <> some more text"
        expected_result = []
        result = network_instance.get_options(option_string)
        assert result == expected_result
