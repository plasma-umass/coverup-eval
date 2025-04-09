# file: lib/ansible/cli/arguments/option_helpers.py:367-370
# asked: {"lines": [367, 369, 370], "branches": []}
# gained: {"lines": [367, 369, 370], "branches": []}

import pytest
from unittest.mock import Mock

def test_add_tasknoplay_options():
    from ansible.cli.arguments.option_helpers import add_tasknoplay_options
    from ansible import constants as C

    parser = Mock()
    add_tasknoplay_options(parser)

    parser.add_argument.assert_called_once_with(
        '--task-timeout',
        type=int,
        dest='task_timeout',
        action='store',
        default=C.TASK_TIMEOUT,
        help='set task timeout limit in seconds, must be positive integer.'
    )
