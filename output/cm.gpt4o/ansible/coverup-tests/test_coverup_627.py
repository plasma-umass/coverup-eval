# file lib/ansible/modules/iptables.py:581-583
# lines [581, 582, 583]
# branches ['582->exit', '582->583']

import pytest
from unittest.mock import patch

# Assuming the append_wait function is part of a class or module, we need to import it.
# For this example, let's assume it's a standalone function in a module named iptables.

from ansible.modules.iptables import append_wait

def test_append_wait_with_param():
    rule = []
    param = "some_param"
    flag = "--some-flag"
    
    append_wait(rule, param, flag)
    
    assert rule == ["--some-flag", "some_param"]

def test_append_wait_without_param():
    rule = []
    param = None
    flag = "--some-flag"
    
    append_wait(rule, param, flag)
    
    assert rule == []

# Clean up is not necessary in this case as the function does not modify any external state.
