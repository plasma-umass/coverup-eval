# file: lib/ansible/utils/context_objects.py:85-92
# asked: {"lines": [85, 86, 87, 92], "branches": []}
# gained: {"lines": [85, 86, 87, 92], "branches": []}

import pytest
from ansible.utils.context_objects import GlobalCLIArgs, CLIArgs

def test_global_cli_args_singleton():
    # Create two instances of GlobalCLIArgs
    instance1 = GlobalCLIArgs({})
    instance2 = GlobalCLIArgs({})

    # Assert that both instances are actually the same instance (singleton behavior)
    assert instance1 is instance2

    # Assert that the instance is an instance of CLIArgs
    assert isinstance(instance1, CLIArgs)
    assert isinstance(instance2, CLIArgs)
