# file: lib/ansible/module_utils/facts/system/distribution.py:19-27
# asked: {"lines": [19, 20, 21, 22, 23, 24, 25, 26, 27], "branches": [[20, 21], [20, 22], [25, 26], [25, 27]]}
# gained: {"lines": [19, 20, 21, 22, 23, 24, 25, 26, 27], "branches": [[20, 21], [20, 22], [25, 26], [25, 27]]}

import pytest

class MockModule:
    def run_command(self, command):
        if command == ['uname', '-v']:
            return (0, 'Mocked uname output', '')
        return (1, '', 'Error')

@pytest.fixture
def mock_module():
    return MockModule()

def test_get_uname_with_default_flag(mock_module):
    from ansible.module_utils.facts.system.distribution import get_uname
    result = get_uname(mock_module)
    assert result == 'Mocked uname output'

def test_get_uname_with_custom_flag(mock_module):
    from ansible.module_utils.facts.system.distribution import get_uname
    result = get_uname(mock_module, '-a')
    assert result is None

def test_get_uname_with_list_flag(mock_module):
    from ansible.module_utils.facts.system.distribution import get_uname
    result = get_uname(mock_module, ['-v'])
    assert result == 'Mocked uname output'
