# file lib/ansible/plugins/shell/powershell.py:99-102
# lines [99, 101, 102]
# branches []

import pytest
from ansible.plugins.shell.powershell import ShellModule

@pytest.fixture
def shell_module():
    return ShellModule()

def test_path_has_trailing_slash(shell_module):
    # Test with trailing forward slash
    path_with_forward_slash = 'C:/path/to/dir/'
    assert shell_module.path_has_trailing_slash(path_with_forward_slash) is True

    # Test with trailing backslash
    path_with_backslash = 'C:\\path\\to\\dir\\'
    assert shell_module.path_has_trailing_slash(path_with_backslash) is True

    # Test without trailing slash
    path_without_trailing_slash = 'C:/path/to/dir'
    assert shell_module.path_has_trailing_slash(path_without_trailing_slash) is False

    # Test with quoted path and trailing slash
    quoted_path_with_trailing_slash = '"C:/path/to/dir/"'
    assert shell_module.path_has_trailing_slash(quoted_path_with_trailing_slash) is True

    # Test with quoted path without trailing slash
    quoted_path_without_trailing_slash = '"C:/path/to/dir"'
    assert shell_module.path_has_trailing_slash(quoted_path_without_trailing_slash) is False
