# file: lib/ansible/cli/arguments/option_helpers.py:367-370
# asked: {"lines": [367, 369, 370], "branches": []}
# gained: {"lines": [367, 369, 370], "branches": []}

import pytest
from argparse import ArgumentParser
from ansible.cli.arguments.option_helpers import add_tasknoplay_options
from ansible import constants as C

def test_add_tasknoplay_options():
    parser = ArgumentParser()
    add_tasknoplay_options(parser)
    args = parser.parse_args(['--task-timeout', '30'])
    assert args.task_timeout == 30

    args = parser.parse_args([])
    assert args.task_timeout == C.TASK_TIMEOUT
