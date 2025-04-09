# file lib/ansible/playbook/play.py:193-205
# lines [193, 198, 199, 200, 201, 202, 204, 205]
# branches []

import pytest
from unittest.mock import Mock, patch
from ansible.playbook.play import Play
from ansible.errors import AnsibleParserError

@pytest.fixture
def mock_load_list_of_blocks(mocker):
    return mocker.patch('ansible.playbook.play.load_list_of_blocks')

@pytest.fixture
def play_instance():
    class MockBase:
        pass

    class MockTaggable:
        pass

    class MockCollectionSearch:
        pass

    class MockVariableManager:
        pass

    class MockLoader:
        pass

    class MockPlay(MockBase, MockTaggable, MockCollectionSearch):
        def __init__(self):
            self.handlers = []
            self._variable_manager = MockVariableManager()
            self._loader = MockLoader()
            self._ds = {}

        def _extend_value(self, current_value, new_value, prepend=False):
            if prepend:
                current_value[:0] = new_value
            else:
                current_value.extend(new_value)
            return current_value

        _load_handlers = Play._load_handlers

    return MockPlay()

def test_load_handlers_success(play_instance, mock_load_list_of_blocks):
    mock_load_list_of_blocks.return_value = ['handler1', 'handler2']
    result = play_instance._load_handlers('handlers', ['handler1', 'handler2'])
    assert result == ['handler1', 'handler2']
    assert play_instance.handlers == ['handler1', 'handler2']

def test_load_handlers_malformed_block(play_instance, mock_load_list_of_blocks):
    mock_load_list_of_blocks.side_effect = AssertionError("Malformed block")
    with pytest.raises(AnsibleParserError) as excinfo:
        play_instance._load_handlers('handlers', ['malformed_handler'])
    assert "A malformed block was encountered while loading handlers" in str(excinfo.value)
    assert excinfo.value.obj == play_instance._ds
    assert isinstance(excinfo.value.orig_exc, AssertionError)
