# file: lib/ansible/plugins/shell/powershell.py:81-88
# asked: {"lines": [81, 83, 88], "branches": []}
# gained: {"lines": [81, 83, 88], "branches": []}

import pytest
import ntpath
from ansible.plugins.shell.powershell import ShellModule

class TestShellModule:
    @pytest.fixture
    def shell_module(self):
        return ShellModule()

    def test_join_path_single_component(self, shell_module):
        result = shell_module.join_path('C:\\path\\to\\file')
        assert result == 'C:\\path\\to\\file'

    def test_join_path_multiple_components(self, shell_module):
        result = shell_module.join_path('C:\\path', 'to', 'file')
        assert result == 'C:\\path\\to\\file'

    def test_join_path_with_leading_slash(self, shell_module):
        result = shell_module.join_path('C:\\path', '\\to', 'file')
        assert result == 'C:\\path\\to\\file'

    def test_join_path_with_double_slash(self, shell_module):
        result = shell_module.join_path('C:\\path\\\\to', 'file')
        assert result == 'C:\\path\\to\\file'

    def test_join_path_with_quoted_component(self, shell_module):
        result = shell_module.join_path('C:\\path', '"to"', 'file')
        assert result == 'C:\\path\\to\\file'
