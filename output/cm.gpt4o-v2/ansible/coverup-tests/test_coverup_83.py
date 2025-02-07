# file: lib/ansible/playbook/conditional.py:78-114
# asked: {"lines": [78, 87, 88, 89, 91, 92, 93, 96, 97, 98, 99, 101, 104, 105, 107, 108, 109, 111, 112, 114], "branches": [[88, 89], [88, 91], [93, 96], [93, 114], [96, 97], [96, 98], [98, 99], [98, 101], [104, 105], [104, 107], [108, 93], [108, 109]]}
# gained: {"lines": [78, 87, 88, 91, 92, 93, 96, 97, 98, 99, 101, 104, 105, 107, 108, 109, 111, 112, 114], "branches": [[88, 91], [93, 96], [93, 114], [96, 97], [96, 98], [98, 99], [98, 101], [104, 105], [108, 93], [108, 109]]}

import pytest
from unittest.mock import MagicMock, patch
from ansible.errors import AnsibleError
from ansible.module_utils._text import to_native
from ansible.playbook.conditional import Conditional

class TestConditional:

    @patch('ansible.playbook.conditional.display')
    def test_evaluate_conditional_all_true(self, mock_display):
        templar = MagicMock()
        all_vars = {}
        loader = MagicMock()
        cond = Conditional(loader=loader)
        cond.when = [True, True, True]
        result = cond.evaluate_conditional(templar, all_vars)
        assert result is True
        assert mock_display.debug.call_count == 3

    @patch('ansible.playbook.conditional.display')
    def test_evaluate_conditional_one_false(self, mock_display):
        templar = MagicMock()
        all_vars = {}
        loader = MagicMock()
        cond = Conditional(loader=loader)
        cond.when = [True, False, True]
        result = cond.evaluate_conditional(templar, all_vars)
        assert result is False
        assert mock_display.debug.call_count == 2

    @patch('ansible.playbook.conditional.display')
    def test_evaluate_conditional_exception(self, mock_display):
        templar = MagicMock()
        all_vars = {}
        loader = MagicMock()
        cond = Conditional(loader=loader)
        cond.when = [True, "{{ undefined_variable }}"]
        cond._check_conditional = MagicMock(side_effect=Exception("Test exception"))
        with pytest.raises(AnsibleError) as excinfo:
            cond.evaluate_conditional(templar, all_vars)
        assert "The conditional check" in str(excinfo.value)
        assert mock_display.debug.call_count == 1

    @patch('ansible.playbook.conditional.display')
    def test_evaluate_conditional_none_and_empty(self, mock_display):
        templar = MagicMock()
        all_vars = {}
        loader = MagicMock()
        cond = Conditional(loader=loader)
        cond.when = [None, '', True]
        result = cond.evaluate_conditional(templar, all_vars)
        assert result is True
        assert mock_display.debug.call_count == 3

    @patch('ansible.playbook.conditional.display')
    def test_evaluate_conditional_mixed(self, mock_display):
        templar = MagicMock()
        all_vars = {}
        loader = MagicMock()
        cond = Conditional(loader=loader)
        cond.when = [None, '', True, False]
        result = cond.evaluate_conditional(templar, all_vars)
        assert result is False
        assert mock_display.debug.call_count == 4
