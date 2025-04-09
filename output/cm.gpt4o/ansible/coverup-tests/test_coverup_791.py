# file lib/ansible/playbook/play.py:101-102
# lines [101, 102]
# branches []

import pytest
from unittest.mock import patch

# Assuming the Play class is defined in ansible.playbook.play module
from ansible.playbook.play import Play

class TestPlay:
    @patch('ansible.playbook.play.Play.get_name', return_value='test_play')
    def test_repr(self, mock_get_name):
        play = Play()
        assert repr(play) == 'test_play'
        mock_get_name.assert_called_once()

    def test_cleanup(self):
        # Ensure no side effects
        assert not hasattr(Play, 'some_non_existent_attribute')
