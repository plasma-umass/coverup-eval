# file thefuck/entrypoints/fix_command.py:13-26
# lines [13, 14, 15, 16, 17, 19, 20, 21, 22, 23, 24, 25, 26]
# branches ['14->15', '14->16', '16->17', '16->19', '22->23', '22->26', '24->22', '24->25']

import os
from unittest.mock import patch
import pytest
from thefuck.entrypoints.fix_command import _get_raw_command
from thefuck import const
from thefuck.utils import get_alias, get_all_executables
from difflib import SequenceMatcher

class KnownArgs:
    def __init__(self, force_command=None, command=None):
        self.force_command = force_command
        self.command = command

@pytest.fixture
def environ():
    old_environ = dict(os.environ)
    yield
    os.environ.clear()
    os.environ.update(old_environ)

def test_get_raw_command_with_force_command(environ):
    args = KnownArgs(force_command='forced_command')
    assert _get_raw_command(args) == 'forced_command'

def test_get_raw_command_without_tf_history(environ):
    args = KnownArgs(command='normal_command')
    with patch.dict(os.environ, {'TF_HISTORY': ''}):
        assert _get_raw_command(args) == 'normal_command'

def test_get_raw_command_with_tf_history_and_diff_less_than_diff_with_alias(environ):
    args = KnownArgs(command='normal_command')
    with patch.dict(os.environ, {'TF_HISTORY': 'alias_command\nother_command'}), \
         patch('thefuck.utils.get_alias', return_value='alias'), \
         patch('thefuck.utils.get_all_executables', return_value=['ls', 'cd', 'echo']), \
         patch('thefuck.const.DIFF_WITH_ALIAS', new=0.5):
        assert _get_raw_command(args) == ['other_command']

def test_get_raw_command_with_tf_history_and_command_in_executables(environ):
    args = KnownArgs(command='normal_command')
    with patch.dict(os.environ, {'TF_HISTORY': 'ls\ncd\necho'}), \
         patch('thefuck.utils.get_alias', return_value='not_in_executables'), \
         patch('thefuck.utils.get_all_executables', return_value=['ls', 'cd', 'echo']):
        assert _get_raw_command(args) == ['echo']

def test_get_raw_command_with_tf_history_and_no_match(environ):
    args = KnownArgs(command='normal_command')
    with patch.dict(os.environ, {'TF_HISTORY': 'unrelated_command\nother_unrelated_command'}), \
         patch('thefuck.utils.get_alias', return_value='alias'), \
         patch('thefuck.utils.get_all_executables', return_value=['ls', 'cd', 'echo']), \
         patch('thefuck.const.DIFF_WITH_ALIAS', new=0.99):
        assert _get_raw_command(args) == ['other_unrelated_command']
