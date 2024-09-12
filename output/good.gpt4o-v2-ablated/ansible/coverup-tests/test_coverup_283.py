# file: lib/ansible/cli/arguments/option_helpers.py:367-370
# asked: {"lines": [367, 369, 370], "branches": []}
# gained: {"lines": [367, 369, 370], "branches": []}

import pytest
from argparse import ArgumentParser, Namespace
from ansible.cli.arguments.option_helpers import add_tasknoplay_options
import ansible.constants as C

@pytest.fixture
def parser():
    return ArgumentParser()

def test_add_tasknoplay_options_default(parser):
    add_tasknoplay_options(parser)
    args = parser.parse_args([])
    assert args.task_timeout == C.TASK_TIMEOUT

def test_add_tasknoplay_options_custom(parser):
    add_tasknoplay_options(parser)
    custom_timeout = 120
    args = parser.parse_args(['--task-timeout', str(custom_timeout)])
    assert args.task_timeout == custom_timeout
