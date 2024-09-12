# file: lib/ansible/plugins/action/pause.py:75-85
# asked: {"lines": [75, 76, 77, 79, 83, 85], "branches": [[76, 77], [76, 79], [79, 83], [79, 85]]}
# gained: {"lines": [75, 76, 77, 79, 83, 85], "branches": [[76, 77], [76, 79], [79, 83], [79, 85]]}

import pytest
from unittest.mock import patch

# Assuming the function is_interactive is defined in the module ansible.plugins.action.pause
from ansible.plugins.action.pause import is_interactive

def test_is_interactive_with_none_fd():
    assert not is_interactive(None)

def test_is_interactive_with_non_tty_fd():
    with patch('ansible.plugins.action.pause.isatty', return_value=False):
        assert not is_interactive(1)

def test_is_interactive_with_tty_fd_and_foreground_process():
    with patch('ansible.plugins.action.pause.isatty', return_value=True), \
         patch('ansible.plugins.action.pause.getpgrp', return_value=1000), \
         patch('ansible.plugins.action.pause.tcgetpgrp', return_value=1000):
        assert is_interactive(1)

def test_is_interactive_with_tty_fd_and_background_process():
    with patch('ansible.plugins.action.pause.isatty', return_value=True), \
         patch('ansible.plugins.action.pause.getpgrp', return_value=1000), \
         patch('ansible.plugins.action.pause.tcgetpgrp', return_value=2000):
        assert not is_interactive(1)
