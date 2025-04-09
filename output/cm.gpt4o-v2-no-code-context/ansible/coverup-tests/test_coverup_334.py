# file: lib/ansible/playbook/play.py:121-131
# asked: {"lines": [121, 123, 124, 126, 127, 129, 131], "branches": [[123, 124], [123, 126], [126, 127], [126, 129]]}
# gained: {"lines": [121, 123, 124, 126, 127, 129, 131], "branches": [[123, 124], [123, 126], [126, 127], [126, 129]]}

import pytest
from unittest.mock import patch

# Assuming the Play class is imported from ansible.playbook.play
from ansible.playbook.play import Play

class TestPlay:
    
    @pytest.fixture
    def play_instance(self):
        return Play()

    def test_get_name_with_name(self, play_instance):
        play_instance.name = "Test Play"
        assert play_instance.get_name() == "Test Play"

    def test_get_name_with_hosts_sequence(self, play_instance):
        play_instance.name = None
        play_instance.hosts = ["host1", "host2"]
        with patch('ansible.playbook.play.is_sequence', return_value=True):
            assert play_instance.get_name() == "host1,host2"

    def test_get_name_with_single_host(self, play_instance):
        play_instance.name = None
        play_instance.hosts = "host1"
        with patch('ansible.playbook.play.is_sequence', return_value=False):
            assert play_instance.get_name() == "host1"

    def test_get_name_with_no_hosts(self, play_instance):
        play_instance.name = None
        play_instance.hosts = None
        with patch('ansible.playbook.play.is_sequence', return_value=False):
            assert play_instance.get_name() == ""
