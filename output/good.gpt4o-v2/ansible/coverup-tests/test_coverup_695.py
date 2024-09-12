# file: lib/ansible/utils/context_objects.py:85-92
# asked: {"lines": [85, 86, 87, 92], "branches": []}
# gained: {"lines": [85, 86, 87, 92], "branches": []}

import pytest
from ansible.utils.context_objects import GlobalCLIArgs

def test_global_cli_args_instantiation():
    # Instantiate GlobalCLIArgs to ensure lines 85-92 are executed
    instance = GlobalCLIArgs({})
    assert isinstance(instance, GlobalCLIArgs)
