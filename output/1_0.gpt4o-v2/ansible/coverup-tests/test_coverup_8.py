# file: lib/ansible/plugins/become/runas.py:64-70
# asked: {"lines": [64, 66, 68, 70], "branches": []}
# gained: {"lines": [64, 66, 68, 70], "branches": []}

import pytest
from ansible.plugins.become.runas import BecomeModule

@pytest.fixture
def become_module():
    return BecomeModule()

def test_become_module_name(become_module):
    assert become_module.name == 'runas'

def test_build_become_command(become_module):
    cmd = "echo Hello"
    shell = "/bin/bash"
    result = become_module.build_become_command(cmd, shell)
    assert result == cmd
