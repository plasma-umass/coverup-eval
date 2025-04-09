# file lib/ansible/playbook/conditional.py:78-114
# lines [87, 88, 89, 91, 92, 93, 96, 97, 98, 99, 101, 104, 105, 107, 108, 109, 111, 112, 114]
# branches ['88->89', '88->91', '93->96', '93->114', '96->97', '96->98', '98->99', '98->101', '104->105', '104->107', '108->93', '108->109']

import pytest
from unittest.mock import MagicMock, patch
from ansible.errors import AnsibleError
from ansible.playbook.conditional import Conditional

class TestConditional:
    @pytest.fixture
    def conditional_instance(self, mocker):
        loader = mocker.MagicMock()
        instance = Conditional(loader=loader)
        instance.when = []
        return instance

    def test_evaluate_conditional_no_ds(self, conditional_instance, mocker):
        templar = MagicMock()
        all_vars = {}

        # Test when 'when' is empty
        conditional_instance.when = []
        assert conditional_instance.evaluate_conditional(templar, all_vars) is True

        # Test when 'when' has None
        conditional_instance.when = [None]
        assert conditional_instance.evaluate_conditional(templar, all_vars) is True

        # Test when 'when' has an empty string
        conditional_instance.when = ['']
        assert conditional_instance.evaluate_conditional(templar, all_vars) is True

        # Test when 'when' has a boolean True
        conditional_instance.when = [True]
        assert conditional_instance.evaluate_conditional(templar, all_vars) is True

        # Test when 'when' has a boolean False
        conditional_instance.when = [False]
        assert conditional_instance.evaluate_conditional(templar, all_vars) is False

    def test_evaluate_conditional_with_ds(self, conditional_instance, mocker):
        templar = MagicMock()
        all_vars = {}

        # Add _ds attribute to the instance
        conditional_instance._ds = 'datastructure'

        # Test when 'when' has a valid conditional
        conditional_instance.when = ['valid_conditional']
        mocker.patch.object(conditional_instance, '_check_conditional', return_value=True)
        assert conditional_instance.evaluate_conditional(templar, all_vars) is True

        # Test when 'when' has a conditional that raises an exception
        conditional_instance.when = ['invalid_conditional']
        mocker.patch.object(conditional_instance, '_check_conditional', side_effect=Exception('error'))
        with pytest.raises(AnsibleError, match="The conditional check 'invalid_conditional' failed. The error was: error"):
            conditional_instance.evaluate_conditional(templar, all_vars)
