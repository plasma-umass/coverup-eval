# file: lib/ansible/playbook/play.py:104-119
# asked: {"lines": [104, 106, 107, 108, 110, 112, 113, 114, 115, 116, 118, 119], "branches": [[106, 0], [106, 107], [107, 108], [107, 110], [110, 112], [110, 118], [112, 0], [112, 113], [113, 114], [113, 115], [115, 112], [115, 116], [118, 0], [118, 119]]}
# gained: {"lines": [104, 106, 107, 108, 110, 112, 113, 114, 115, 116, 118, 119], "branches": [[106, 107], [107, 108], [107, 110], [110, 112], [110, 118], [112, 0], [112, 113], [113, 114], [113, 115], [115, 112], [115, 116], [118, 0], [118, 119]]}

import pytest
from ansible.playbook.play import Play
from ansible.errors import AnsibleParserError
from ansible.module_utils.six import string_types

class TestPlay:
    @pytest.fixture
    def play_instance(self):
        class MockPlay(Play):
            def __init__(self, ds):
                self._ds = ds
        return MockPlay

    def test_validate_hosts_empty_list(self, play_instance):
        play = play_instance({'hosts': []})
        with pytest.raises(AnsibleParserError, match="Hosts list cannot be empty. Please check your playbook"):
            play._validate_hosts('hosts', 'hosts', [])

    def test_validate_hosts_none_in_list(self, play_instance):
        play = play_instance({'hosts': [None]})
        with pytest.raises(AnsibleParserError, match="Hosts list cannot contain values of 'None'. Please check your playbook"):
            play._validate_hosts('hosts', 'hosts', [None])

    def test_validate_hosts_invalid_type_in_list(self, play_instance):
        play = play_instance({'hosts': [123]})
        with pytest.raises(AnsibleParserError, match="Hosts list contains an invalid host value: '123'"):
            play._validate_hosts('hosts', 'hosts', [123])

    def test_validate_hosts_invalid_type(self, play_instance):
        play = play_instance({'hosts': 123})
        with pytest.raises(AnsibleParserError, match="Hosts list must be a sequence or string. Please check your playbook."):
            play._validate_hosts('hosts', 'hosts', 123)

    def test_validate_hosts_valid_list(self, play_instance):
        play = play_instance({'hosts': ['host1', 'host2']})
        try:
            play._validate_hosts('hosts', 'hosts', ['host1', 'host2'])
        except AnsibleParserError:
            pytest.fail("AnsibleParserError raised unexpectedly")

    def test_validate_hosts_valid_string(self, play_instance):
        play = play_instance({'hosts': 'host1'})
        try:
            play._validate_hosts('hosts', 'hosts', 'host1')
        except AnsibleParserError:
            pytest.fail("AnsibleParserError raised unexpectedly")
