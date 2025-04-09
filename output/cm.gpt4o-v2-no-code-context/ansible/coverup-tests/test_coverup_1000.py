# file: lib/ansible/plugins/action/pause.py:75-85
# asked: {"lines": [76, 77, 79, 83, 85], "branches": [[76, 77], [76, 79], [79, 83], [79, 85]]}
# gained: {"lines": [76, 77, 79, 83, 85], "branches": [[76, 77], [76, 79], [79, 83], [79, 85]]}

import pytest
from unittest.mock import patch

# Assuming the function is_interactive is imported from the module
from ansible.plugins.action.pause import is_interactive

def test_is_interactive_fd_none():
    assert is_interactive() is False

@patch('ansible.plugins.action.pause.isatty', return_value=True)
@patch('ansible.plugins.action.pause.getpgrp', return_value=1000)
@patch('ansible.plugins.action.pause.tcgetpgrp', return_value=1000)
def test_is_interactive_isatty_true(mock_tcgetpgrp, mock_getpgrp, mock_isatty):
    assert is_interactive(1) is True

@patch('ansible.plugins.action.pause.isatty', return_value=True)
@patch('ansible.plugins.action.pause.getpgrp', return_value=1000)
@patch('ansible.plugins.action.pause.tcgetpgrp', return_value=2000)
def test_is_interactive_isatty_true_different_pgrp(mock_tcgetpgrp, mock_getpgrp, mock_isatty):
    assert is_interactive(1) is False

@patch('ansible.plugins.action.pause.isatty', return_value=False)
def test_is_interactive_isatty_false(mock_isatty):
    assert is_interactive(1) is False
