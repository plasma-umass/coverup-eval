# file: lib/ansible/playbook/play.py:104-119
# asked: {"lines": [], "branches": [[106, 0]]}
# gained: {"lines": [], "branches": [[106, 0]]}

import pytest
from ansible.playbook.play import Play
from ansible.errors import AnsibleParserError
from ansible.module_utils.six import binary_type, text_type

class MockPlay(Play):
    def __init__(self, ds):
        self._ds = ds

def test_validate_hosts_no_hosts_key():
    play = MockPlay({})
    # This should not raise any exception as 'hosts' is not in the dataset
    play._validate_hosts('hosts', 'hosts', None)

def test_validate_hosts_with_empty_hosts():
    play = MockPlay({'hosts': True})
    with pytest.raises(AnsibleParserError, match="Hosts list cannot be empty. Please check your playbook"):
        play._validate_hosts('hosts', 'hosts', [])

def test_validate_hosts_with_none_in_list():
    play = MockPlay({'hosts': True})
    with pytest.raises(AnsibleParserError, match="Hosts list cannot contain values of 'None'. Please check your playbook"):
        play._validate_hosts('hosts', 'hosts', [None])

def test_validate_hosts_with_invalid_type_in_list():
    play = MockPlay({'hosts': True})
    with pytest.raises(AnsibleParserError, match="Hosts list contains an invalid host value: '123'"):
        play._validate_hosts('hosts', 'hosts', [123])

def test_validate_hosts_with_invalid_type():
    play = MockPlay({'hosts': True})
    with pytest.raises(AnsibleParserError, match="Hosts list must be a sequence or string. Please check your playbook."):
        play._validate_hosts('hosts', 'hosts', 123)

def test_validate_hosts_with_valid_list():
    play = MockPlay({'hosts': True})
    play._validate_hosts('hosts', 'hosts', ['host1', 'host2'])

def test_validate_hosts_with_valid_string():
    play = MockPlay({'hosts': True})
    play._validate_hosts('hosts', 'hosts', 'host1')
