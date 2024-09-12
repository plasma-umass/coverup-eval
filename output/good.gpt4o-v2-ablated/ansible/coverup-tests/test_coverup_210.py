# file: lib/ansible/plugins/shell/powershell.py:113-118
# asked: {"lines": [113, 114, 115, 116, 118], "branches": [[115, 116], [115, 118]]}
# gained: {"lines": [113, 114, 115, 116, 118], "branches": [[115, 116], [115, 118]]}

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

@pytest.fixture
def shell_module():
    return ShellModule()

def test_remove_non_recursive(shell_module, mocker):
    mocker.patch.object(ShellModule, '_escape', side_effect=MockShellBase()._escape)
    mocker.patch.object(ShellModule, '_unquote', side_effect=MockShellBase()._unquote)
    mocker.patch.object(ShellModule, '_encode_script', side_effect=MockShellBase()._encode_script)

    path = '"C:\\path\\to\\file"'
    result = shell_module.remove(path, recurse=False)
    expected_script = b"Remove-Item 'C:\\path\\to\\file' -Force;"
    assert result == expected_script

def test_remove_recursive(shell_module, mocker):
    mocker.patch.object(ShellModule, '_escape', side_effect=MockShellBase()._escape)
    mocker.patch.object(ShellModule, '_unquote', side_effect=MockShellBase()._unquote)
    mocker.patch.object(ShellModule, '_encode_script', side_effect=MockShellBase()._encode_script)

    path = '"C:\\path\\to\\directory"'
    result = shell_module.remove(path, recurse=True)
    expected_script = b"Remove-Item 'C:\\path\\to\\directory' -Force -Recurse;"
    assert result == expected_script
