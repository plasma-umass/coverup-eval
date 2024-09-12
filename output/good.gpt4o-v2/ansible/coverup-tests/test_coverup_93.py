# file: lib/ansible/playbook/play.py:104-119
# asked: {"lines": [104, 106, 107, 108, 110, 112, 113, 114, 115, 116, 118, 119], "branches": [[106, 0], [106, 107], [107, 108], [107, 110], [110, 112], [110, 118], [112, 0], [112, 113], [113, 114], [113, 115], [115, 112], [115, 116], [118, 0], [118, 119]]}
# gained: {"lines": [104, 106, 107, 108, 110, 112, 113, 114, 115, 116, 118, 119], "branches": [[106, 107], [107, 108], [107, 110], [110, 112], [110, 118], [112, 0], [112, 113], [113, 114], [113, 115], [115, 112], [115, 116], [118, 0], [118, 119]]}

import pytest
from ansible.playbook.play import Play
from ansible.errors import AnsibleParserError
from ansible.module_utils.common.collections import is_sequence
from ansible.module_utils.six import binary_type, text_type

class MockPlay(Play):
    def __init__(self, ds):
        super().__init__()
        self._ds = ds

def test_validate_hosts_empty_list():
    play = MockPlay({'hosts': True})
    with pytest.raises(AnsibleParserError, match="Hosts list cannot be empty. Please check your playbook"):
        play._validate_hosts('attribute', 'name', [])

def test_validate_hosts_none_in_list():
    play = MockPlay({'hosts': True})
    with pytest.raises(AnsibleParserError, match="Hosts list cannot contain values of 'None'. Please check your playbook"):
        play._validate_hosts('attribute', 'name', [None])

def test_validate_hosts_invalid_type_in_list():
    play = MockPlay({'hosts': True})
    with pytest.raises(AnsibleParserError, match="Hosts list contains an invalid host value: '123'"):
        play._validate_hosts('attribute', 'name', [123])

def test_validate_hosts_invalid_type():
    play = MockPlay({'hosts': True})
    with pytest.raises(AnsibleParserError, match="Hosts list must be a sequence or string. Please check your playbook"):
        play._validate_hosts('attribute', 'name', 123)

def test_validate_hosts_valid_list():
    play = MockPlay({'hosts': True})
    play._validate_hosts('attribute', 'name', ['host1', 'host2'])

def test_validate_hosts_valid_string():
    play = MockPlay({'hosts': True})
    play._validate_hosts('attribute', 'name', 'host1')
