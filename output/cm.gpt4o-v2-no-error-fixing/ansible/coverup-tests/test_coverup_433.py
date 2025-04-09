# file: lib/ansible/plugins/shell/powershell.py:148-162
# asked: {"lines": [148, 149, 150, 161, 162], "branches": []}
# gained: {"lines": [148, 149, 150, 161, 162], "branches": []}

import pytest
from ansible.plugins.shell.powershell import ShellModule

class MockShellBase:
    def _escape(self, path):
        return path.replace("'", "''")

    def _unquote(self, path):
        if path.startswith('"') and path.endswith('"'):
            return path[1:-1]
        return path

    def _encode_script(self, script):
        return script.encode('utf-8')

class TestShellModule(MockShellBase, ShellModule):
    pass

@pytest.fixture
def shell_module():
    return TestShellModule()

def test_exists_path(shell_module):
    path = '"C:\\path\\to\\file"'
    expected_script = b"""
            If (Test-Path 'C:\\path\\to\\file')
            {
                $res = 0;
            }
            Else
            {
                $res = 1;
            }
            Write-Output '$res';
            Exit $res;
         """
    result = shell_module.exists(path)
    assert result == expected_script

def test_exists_path_with_single_quote(shell_module):
    path = '"C:\\path\\to\\fi\'le"'
    expected_script = b"""
            If (Test-Path 'C:\\path\\to\\fi''le')
            {
                $res = 0;
            }
            Else
            {
                $res = 1;
            }
            Write-Output '$res';
            Exit $res;
         """
    result = shell_module.exists(path)
    assert result == expected_script
