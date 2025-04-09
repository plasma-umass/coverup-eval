# file lib/ansible/cli/arguments/option_helpers.py:367-370
# lines [369, 370]
# branches []

import pytest
from argparse import ArgumentParser
from ansible.cli.arguments.option_helpers import add_tasknoplay_options
import ansible.constants as C

def test_add_tasknoplay_options_task_timeout():
    parser = ArgumentParser()
    add_tasknoplay_options(parser)
    args = parser.parse_args(['--task-timeout', '30'])
    assert args.task_timeout == 30

def test_add_tasknoplay_options_task_timeout_default():
    parser = ArgumentParser()
    add_tasknoplay_options(parser)
    args = parser.parse_args([])
    assert args.task_timeout == C.TASK_TIMEOUT
