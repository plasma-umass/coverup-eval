# file: lib/ansible/playbook/play.py:104-119
# asked: {"lines": [], "branches": [[106, 0]]}
# gained: {"lines": [], "branches": [[106, 0]]}

import pytest
from ansible.playbook.play import Play
from ansible.errors import AnsibleParserError

class MockPlay(Play):
    def __init__(self, ds):
        super().__init__()
        self._ds = ds

def test_validate_hosts_with_hosts_key_and_empty_value():
    play = MockPlay({'hosts': True})
    with pytest.raises(AnsibleParserError, match="Hosts list cannot be empty. Please check your playbook"):
        play._validate_hosts('attribute', 'name', [])

def test_validate_hosts_with_hosts_key_and_none_value():
    play = MockPlay({'hosts': True})
    with pytest.raises(AnsibleParserError, match="Hosts list cannot contain values of 'None'. Please check your playbook"):
        play._validate_hosts('attribute', 'name', [None])

def test_validate_hosts_with_hosts_key_and_invalid_host_value():
    play = MockPlay({'hosts': True})
    with pytest.raises(AnsibleParserError, match="Hosts list contains an invalid host value: '123'"):
        play._validate_hosts('attribute', 'name', [123])

def test_validate_hosts_with_hosts_key_and_valid_string():
    play = MockPlay({'hosts': True})
    try:
        play._validate_hosts('attribute', 'name', ['valid_host'])
    except AnsibleParserError:
        pytest.fail("AnsibleParserError raised unexpectedly")

def test_validate_hosts_with_hosts_key_and_valid_binary_type():
    play = MockPlay({'hosts': True})
    try:
        play._validate_hosts('attribute', 'name', [b'valid_host'])
    except AnsibleParserError:
        pytest.fail("AnsibleParserError raised unexpectedly")

def test_validate_hosts_with_hosts_key_and_invalid_type():
    play = MockPlay({'hosts': True})
    with pytest.raises(AnsibleParserError, match="Hosts list must be a sequence or string. Please check your playbook."):
        play._validate_hosts('attribute', 'name', 123)

def test_validate_hosts_without_hosts_key():
    play = MockPlay({})
    try:
        play._validate_hosts('attribute', 'name', 'some_value')
    except AnsibleParserError:
        pytest.fail("AnsibleParserError raised unexpectedly")
