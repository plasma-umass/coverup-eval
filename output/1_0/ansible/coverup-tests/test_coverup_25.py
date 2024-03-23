# file lib/ansible/plugins/shell/sh.py:21-45
# lines [21, 28, 30, 33, 34, 37, 38, 39, 40, 41, 42, 43, 44]
# branches []

import pytest
from ansible.plugins.shell.sh import ShellModule

@pytest.fixture
def shell_module():
    return ShellModule()

def test_shell_module_attributes(shell_module):
    assert shell_module.COMPATIBLE_SHELLS == frozenset(('sh', 'zsh', 'bash', 'dash', 'ksh'))
    assert shell_module.SHELL_FAMILY == 'sh'
    assert shell_module.ECHO == 'echo'
    assert shell_module.COMMAND_SEP == ';'
    assert shell_module._SHELL_EMBEDDED_PY_EOL == '\n'
    assert shell_module._SHELL_REDIRECT_ALLNULL == '> /dev/null 2>&1'
    assert shell_module._SHELL_AND == '&&'
    assert shell_module._SHELL_OR == '||'
    assert shell_module._SHELL_SUB_LEFT == '"`'
    assert shell_module._SHELL_SUB_RIGHT == '`"'
    assert shell_module._SHELL_GROUP_LEFT == '('
    assert shell_module._SHELL_GROUP_RIGHT == ')'
