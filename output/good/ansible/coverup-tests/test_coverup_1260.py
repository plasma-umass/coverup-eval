# file lib/ansible/plugins/become/su.py:146-161
# lines [147, 151, 153, 154, 156, 157, 158, 159, 161]
# branches ['153->154', '153->156']

import pytest
from ansible.plugins.become import su
from shlex import quote as shlex_quote
from unittest.mock import MagicMock

# Mocking the BecomeBase class to avoid side effects
class MockedBecomeBase:
    def build_become_command(self, cmd, shell):
        pass

# Replacing the original BecomeBase with the mocked one
su.BecomeBase = MockedBecomeBase

@pytest.fixture
def become_module():
    return su.BecomeModule()

@pytest.fixture
def mock_options(mocker):
    mocker.patch.object(su.BecomeModule, 'get_option', side_effect=lambda x: {'become_exe': 'su', 'become_flags': '-s', 'become_user': 'test_user'}.get(x))
    mocker.patch.object(su.BecomeModule, '_build_success_command', return_value='BECOME-SUCCESS-COMMAND')

def test_build_become_command_with_cmd(become_module, mock_options):
    cmd = 'echo hello'
    shell = MagicMock()
    result = become_module.build_become_command(cmd, shell)
    expected = "su -s test_user -c %s" % shlex_quote('BECOME-SUCCESS-COMMAND')
    assert result == expected

def test_build_become_command_without_cmd(become_module, mock_options):
    cmd = ''
    shell = MagicMock()
    result = become_module.build_become_command(cmd, shell)
    assert result == ''
