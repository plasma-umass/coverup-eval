# file lib/ansible/plugins/shell/powershell.py:81-88
# lines [83, 88]
# branches []

import pytest
import ntpath
from ansible.plugins.shell.powershell import ShellModule

@pytest.fixture
def shell_module():
    return ShellModule()

def test_join_path_with_unquoted_paths(shell_module, mocker):
    mocker.patch.object(shell_module, '_unquote', side_effect=lambda x: x)
    
    # Test with paths that will trigger the lines 83-88
    path1 = "C:\\folder1\\"
    path2 = "\\folder2\\"
    path3 = "folder3\\file.txt"
    
    result = shell_module.join_path(path1, path2, path3)
    
    expected = ntpath.join(ntpath.normpath(path1), ntpath.normpath(path2).strip('\\'), ntpath.normpath(path3).strip('\\'))
    
    assert result == expected
