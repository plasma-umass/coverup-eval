# file: lib/ansible/playbook/play.py:163-171
# asked: {"lines": [163, 168, 169, 170, 171], "branches": []}
# gained: {"lines": [163], "branches": []}

import pytest
from unittest.mock import MagicMock, patch
from ansible.errors import AnsibleParserError
from ansible.module_utils._text import to_native
from ansible.playbook.helpers import load_list_of_blocks
from ansible.playbook.play import Play

class MockVariableManager:
    pass

class MockLoader:
    pass

class MockBase:
    pass

class MockTaggable:
    pass

class MockCollectionSearch:
    pass

class TestPlay(MockBase, MockTaggable, MockCollectionSearch):
    def __init__(self):
        self._variable_manager = MockVariableManager()
        self._loader = MockLoader()
        self._ds = {}

    @patch('ansible.playbook.helpers.load_list_of_blocks')
    def test_load_tasks_success(self, mock_load_list_of_blocks):
        mock_load_list_of_blocks.return_value = 'mocked_blocks'
        play = Play()
        play._variable_manager = self._variable_manager
        play._loader = self._loader
        result = play._load_tasks('attr', 'ds')
        assert result == 'mocked_blocks'
        mock_load_list_of_blocks.assert_called_once_with(ds='ds', play=play, variable_manager=self._variable_manager, loader=self._loader)

    @patch('ansible.playbook.helpers.load_list_of_blocks')
    def test_load_tasks_assertion_error(self, mock_load_list_of_blocks):
        mock_load_list_of_blocks.side_effect = AssertionError('mocked error')
        play = Play()
        play._variable_manager = self._variable_manager
        play._loader = self._loader
        with pytest.raises(AnsibleParserError) as excinfo:
            play._load_tasks('attr', 'ds')
        assert 'A malformed block was encountered while loading tasks: mocked error' in str(excinfo.value)
        mock_load_list_of_blocks.assert_called_once_with(ds='ds', play=play, variable_manager=self._variable_manager, loader=self._loader)
