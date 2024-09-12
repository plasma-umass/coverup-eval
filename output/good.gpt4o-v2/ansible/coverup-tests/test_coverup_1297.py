# file: lib/ansible/playbook/play.py:104-119
# asked: {"lines": [], "branches": [[106, 0]]}
# gained: {"lines": [], "branches": [[106, 0]]}

import pytest
from ansible.playbook.play import Play
from ansible.errors import AnsibleParserError
from ansible.module_utils.common.collections import is_sequence
from ansible.module_utils.six import binary_type, text_type

class MockPlay(Play):
    def __init__(self, ds):
        super().__init__()
        self._ds = ds

def test_validate_hosts_no_hosts_key():
    play = MockPlay({})
    # This should pass without any exception since 'hosts' is not in self._ds
    play._validate_hosts('attribute', 'name', 'some_value')

def test_validate_hosts_empty_list():
    play = MockPlay({'hosts': []})
    with pytest.raises(AnsibleParserError, match="Hosts list cannot be empty. Please check your playbook"):
        play._validate_hosts('attribute', 'name', [])

def test_validate_hosts_none_value():
    play = MockPlay({'hosts': [None]})
    with pytest.raises(AnsibleParserError, match="Hosts list cannot contain values of 'None'. Please check your playbook"):
        play._validate_hosts('attribute', 'name', [None])

def test_validate_hosts_invalid_host_value():
    play = MockPlay({'hosts': [123]})
    with pytest.raises(AnsibleParserError, match="Hosts list contains an invalid host value: '123'"):
        play._validate_hosts('attribute', 'name', [123])

def test_validate_hosts_invalid_type():
    play = MockPlay({'hosts': 123})
    with pytest.raises(AnsibleParserError, match="Hosts list must be a sequence or string. Please check your playbook"):
        play._validate_hosts('attribute', 'name', 123)
