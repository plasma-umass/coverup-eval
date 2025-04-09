# file: lib/ansible/playbook/conditional.py:78-114
# asked: {"lines": [78, 87, 88, 89, 91, 92, 93, 96, 97, 98, 99, 101, 104, 105, 107, 108, 109, 111, 112, 114], "branches": [[88, 89], [88, 91], [93, 96], [93, 114], [96, 97], [96, 98], [98, 99], [98, 101], [104, 105], [104, 107], [108, 93], [108, 109]]}
# gained: {"lines": [78, 87, 88, 91, 92, 93, 96, 97, 98, 99, 101, 104, 105, 107, 108, 109, 111, 112, 114], "branches": [[88, 91], [93, 96], [93, 114], [96, 97], [96, 98], [98, 99], [98, 101], [104, 105], [108, 93], [108, 109]]}

import pytest
from unittest.mock import MagicMock, patch
from ansible.errors import AnsibleError
from ansible.playbook.conditional import Conditional

class TestConditional:

    @patch('ansible.playbook.conditional.display')
    def test_evaluate_conditional_all_true(self, mock_display):
        loader = MagicMock()
        conditional = Conditional(loader=loader)
        conditional.when = [True, True, True]
        templar = MagicMock()
        all_vars = MagicMock()

        result = conditional.evaluate_conditional(templar, all_vars)
        assert result is True

    @patch('ansible.playbook.conditional.display')
    def test_evaluate_conditional_one_false(self, mock_display):
        loader = MagicMock()
        conditional = Conditional(loader=loader)
        conditional.when = [True, False, True]
        templar = MagicMock()
        all_vars = MagicMock()

        result = conditional.evaluate_conditional(templar, all_vars)
        assert result is False

    @patch('ansible.playbook.conditional.display')
    def test_evaluate_conditional_empty_string(self, mock_display):
        loader = MagicMock()
        conditional = Conditional(loader=loader)
        conditional.when = [True, '', True]
        templar = MagicMock()
        all_vars = MagicMock()

        result = conditional.evaluate_conditional(templar, all_vars)
        assert result is True

    @patch('ansible.playbook.conditional.display')
    def test_evaluate_conditional_none(self, mock_display):
        loader = MagicMock()
        conditional = Conditional(loader=loader)
        conditional.when = [True, None, True]
        templar = MagicMock()
        all_vars = MagicMock()

        result = conditional.evaluate_conditional(templar, all_vars)
        assert result is True

    @patch('ansible.playbook.conditional.display')
    def test_evaluate_conditional_exception(self, mock_display):
        loader = MagicMock()
        conditional = Conditional(loader=loader)
        conditional.when = [True, 'invalid_conditional', True]
        templar = MagicMock()
        all_vars = MagicMock()

        with patch.object(conditional, '_check_conditional', side_effect=Exception('error')):
            with pytest.raises(AnsibleError, match="The conditional check 'invalid_conditional' failed. The error was: error"):
                conditional.evaluate_conditional(templar, all_vars)
