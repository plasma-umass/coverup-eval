# file: lib/ansible/plugins/shell/powershell.py:81-88
# asked: {"lines": [81, 83, 88], "branches": []}
# gained: {"lines": [81, 83, 88], "branches": []}

import pytest
import ntpath
from ansible.plugins.shell.powershell import ShellModule

@pytest.fixture
def shell_module():
    return ShellModule()

def test_join_path_single_component(shell_module):
    result = shell_module.join_path('C:\\path\\to\\dir')
    assert result == 'C:\\path\\to\\dir'

def test_join_path_multiple_components(shell_module):
    result = shell_module.join_path('C:\\path', 'to', 'dir')
    assert result == 'C:\\path\\to\\dir'

def test_join_path_with_leading_slash(shell_module):
    result = shell_module.join_path('C:\\path', '\\to', 'dir')
    assert result == 'C:\\path\\to\\dir'

def test_join_path_with_double_slash(shell_module):
    result = shell_module.join_path('C:\\path\\\\to', 'dir')
    assert result == 'C:\\path\\to\\dir'

def test_join_path_with_quoted_component(shell_module):
    result = shell_module.join_path('C:\\path', '"to"', 'dir')
    assert result == 'C:\\path\\to\\dir'
