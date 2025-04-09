# file lib/ansible/module_utils/facts/system/distribution.py:19-27
# lines [20, 21, 22, 23, 24, 25, 26, 27]
# branches ['20->21', '20->22', '25->26', '25->27']

import pytest
from ansible.module_utils.facts.system.distribution import get_uname

class MockModule:
    def run_command(self, command):
        if command == ['uname', '-v']:
            return 0, 'Mocked uname version output', ''
        else:
            return 1, '', 'Mocked error'

@pytest.fixture
def mock_module(mocker):
    mock = MockModule()
    mocker.patch('ansible.module_utils.facts.system.distribution.get_uname', side_effect=mock.run_command)
    return mock

def test_get_uname_with_string_flag(mock_module):
    result = get_uname(mock_module, flags='-v')
    assert result == 'Mocked uname version output'

def test_get_uname_with_non_zero_return_code(mock_module):
    result = get_uname(mock_module, flags='-invalid-flag')
    assert result is None
