# file: lib/ansible/playbook/play_context.py:128-154
# asked: {"lines": [128, 133, 135, 136, 138, 139, 141, 143, 144, 147, 150, 151, 153, 154], "branches": [[135, 136], [135, 138], [150, 151], [150, 153], [153, 0], [153, 154]]}
# gained: {"lines": [128, 133, 135, 136, 138, 139, 141, 143, 144, 147, 150, 151, 153, 154], "branches": [[135, 136], [135, 138], [150, 151], [150, 153], [153, 0], [153, 154]]}

import pytest
from unittest import mock

# Assuming the PlayContext class is imported from ansible.playbook.play_context
from ansible.playbook.play_context import PlayContext

class TestPlayContext:
    
    @pytest.fixture
    def mock_context(self, monkeypatch):
        mock_context = mock.Mock()
        monkeypatch.setattr('ansible.playbook.play_context.context', mock_context)
        return mock_context

    def test_play_context_init_no_passwords_no_play(self, mock_context):
        mock_context.CLIARGS = False
        pc = PlayContext()
        assert pc.password == ''
        assert pc.become_pass == ''
        assert pc._become_plugin is None
        assert pc.prompt == ''
        assert pc.success_key == ''
        assert pc.connection_lockfd is None

    def test_play_context_init_with_passwords_no_play(self, mock_context):
        mock_context.CLIARGS = False
        passwords = {'conn_pass': 'test_conn_pass', 'become_pass': 'test_become_pass'}
        pc = PlayContext(passwords=passwords)
        assert pc.password == 'test_conn_pass'
        assert pc.become_pass == 'test_become_pass'
        assert pc._become_plugin is None
        assert pc.prompt == ''
        assert pc.success_key == ''
        assert pc.connection_lockfd is None

    def test_play_context_init_with_connection_lockfd(self, mock_context):
        mock_context.CLIARGS = False
        connection_lockfd = 123
        pc = PlayContext(connection_lockfd=connection_lockfd)
        assert pc.connection_lockfd == 123

    def test_play_context_init_with_cliargs(self, mock_context):
        mock_context.CLIARGS = True
        with mock.patch.object(PlayContext, 'set_attributes_from_cli') as mock_set_cli:
            pc = PlayContext()
            mock_set_cli.assert_called_once()

    def test_play_context_init_with_play(self, mock_context):
        mock_context.CLIARGS = False
        play = mock.Mock()
        with mock.patch.object(PlayContext, 'set_attributes_from_play') as mock_set_play:
            pc = PlayContext(play=play)
            mock_set_play.assert_called_once_with(play)
