# file lib/ansible/playbook/play.py:104-119
# lines [104, 106, 107, 108, 110, 112, 113, 114, 115, 116, 118, 119]
# branches ['106->exit', '106->107', '107->108', '107->110', '110->112', '110->118', '112->exit', '112->113', '113->114', '113->115', '115->112', '115->116', '118->exit', '118->119']

import pytest
from ansible.errors import AnsibleParserError
from ansible.playbook.play import Play
from ansible.module_utils.six import text_type, binary_type

# Mock class to avoid issues with the rest of the Play class
class MockPlay(Play):
    def __init__(self, *args, **kwargs):
        self._ds = {'hosts': None}

@pytest.mark.parametrize("hosts_value", [
    None,
    [None],
    [123],
    123
])
def test_play_validate_hosts_errors(hosts_value):
    play = MockPlay()
    with pytest.raises(AnsibleParserError):
        play._validate_hosts('hosts', 'hosts', hosts_value)

def test_play_validate_hosts_success(mocker):
    play = MockPlay()
    mock_string = mocker.MagicMock(spec=text_type)
    mock_string.__str__.return_value = 'mocked_host'
    play._validate_hosts('hosts', 'hosts', [mock_string])
    play._validate_hosts('hosts', 'hosts', 'mocked_host')
    assert True  # If no exception is raised, the test passes
