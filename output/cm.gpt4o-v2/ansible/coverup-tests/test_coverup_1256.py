# file: lib/ansible/playbook/conditional.py:78-114
# asked: {"lines": [89], "branches": [[88, 89], [104, 107]]}
# gained: {"lines": [89], "branches": [[88, 89]]}

import pytest
from unittest.mock import MagicMock, patch
from ansible.errors import AnsibleError
from ansible.module_utils._text import to_native
from ansible.playbook.conditional import Conditional

class TestConditional:

    @patch('ansible.playbook.conditional.display')
    def test_evaluate_conditional_with_ds(self, mock_display):
        loader = MagicMock()
        conditional = Conditional(loader=loader)
        conditional._ds = 'datastructure'
        conditional.when = [True, False]
        templar = MagicMock()
        all_vars = {}

        with patch.object(conditional, '_check_conditional', return_value=False):
            result = conditional.evaluate_conditional(templar, all_vars)
            assert result is False
            mock_display.debug.assert_called_with('Evaluated conditional (False): False')

    @patch('ansible.playbook.conditional.display')
    def test_evaluate_conditional_without_ds(self, mock_display):
        loader = MagicMock()
        conditional = Conditional(loader=loader)
        conditional.when = [True, False]
        templar = MagicMock()
        all_vars = {}

        with patch.object(conditional, '_check_conditional', return_value=False):
            result = conditional.evaluate_conditional(templar, all_vars)
            assert result is False
            mock_display.debug.assert_called_with('Evaluated conditional (False): False')

    @patch('ansible.playbook.conditional.display')
    def test_evaluate_conditional_exception(self, mock_display):
        loader = MagicMock()
        conditional = Conditional(loader=loader)
        conditional._ds = 'datastructure'
        conditional.when = ['invalid']
        templar = MagicMock()
        all_vars = {}

        with patch.object(conditional, '_check_conditional', side_effect=Exception('error')):
            with pytest.raises(AnsibleError) as excinfo:
                conditional.evaluate_conditional(templar, all_vars)
            assert "The conditional check 'invalid' failed. The error was: error" in str(excinfo.value)
            assert excinfo.value.obj == 'datastructure'
