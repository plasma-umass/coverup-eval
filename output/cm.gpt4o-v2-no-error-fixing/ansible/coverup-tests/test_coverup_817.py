# file: lib/ansible/plugins/shell/powershell.py:81-88
# asked: {"lines": [83, 88], "branches": []}
# gained: {"lines": [83, 88], "branches": []}

import pytest
import ntpath
from ansible.plugins.shell.powershell import ShellModule

class MockShellBase:
    def _unquote(self, value):
        return value.strip('"').strip("'")

class TestShellModule:
    @pytest.fixture
    def shell_module(self):
        return ShellModule()

    def test_join_path(self, shell_module, mocker):
        mocker.patch.object(ShellModule, '_unquote', side_effect=MockShellBase()._unquote)
        
        # Test with no leading backslashes in the second part
        result = shell_module.join_path('C:\\path', 'to\\file')
        assert result == 'C:\\path\\to\\file'
        
        # Test with leading backslashes in the second part
        result = shell_module.join_path('C:\\path', '\\to\\file')
        assert result == 'C:\\path\\to\\file'
        
        # Test with quotes around the parts
        result = shell_module.join_path('"C:\\path"', "'to\\file'")
        assert result == 'C:\\path\\to\\file'
        
        # Test with multiple parts
        result = shell_module.join_path('C:\\path', 'to', 'file')
        assert result == 'C:\\path\\to\\file'
        
        # Test with mixed slashes
        result = shell_module.join_path('C:/path', 'to\\file')
        assert result == 'C:\\path\\to\\file'
