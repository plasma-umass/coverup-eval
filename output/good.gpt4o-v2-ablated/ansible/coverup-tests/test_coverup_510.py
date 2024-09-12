# file: lib/ansible/playbook/play.py:163-171
# asked: {"lines": [168, 169, 170, 171], "branches": []}
# gained: {"lines": [168, 169, 170, 171], "branches": []}

import pytest
from ansible.playbook.play import Play
from ansible.errors import AnsibleParserError
from ansible.utils.display import Display
from unittest.mock import Mock, patch

@pytest.fixture
def mock_load_list_of_blocks(mocker):
    return mocker.patch('ansible.playbook.play.load_list_of_blocks')

@pytest.fixture
def play_instance():
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

    class MockPlay(MockBase, MockTaggable, MockCollectionSearch, Play):
        def __init__(self):
            self._variable_manager = MockVariableManager()
            self._loader = MockLoader()
            self._ds = {}

    return MockPlay()

def test_load_tasks_success(play_instance, mock_load_list_of_blocks):
    mock_load_list_of_blocks.return_value = 'mocked_blocks'
    ds = [{'name': 'task1'}, {'name': 'task2'}]
    result = play_instance._load_tasks('tasks', ds)
    assert result == 'mocked_blocks'
    mock_load_list_of_blocks.assert_called_once_with(ds=ds, play=play_instance, variable_manager=play_instance._variable_manager, loader=play_instance._loader)

def test_load_tasks_assertion_error(play_instance, mock_load_list_of_blocks):
    mock_load_list_of_blocks.side_effect = AssertionError('mocked assertion error')
    ds = [{'name': 'task1'}, {'name': 'task2'}]
    with pytest.raises(AnsibleParserError) as excinfo:
        play_instance._load_tasks('tasks', ds)
    assert 'A malformed block was encountered while loading tasks: mocked assertion error' in str(excinfo.value)
    assert excinfo.value.obj == play_instance._ds
    assert excinfo.value.orig_exc.args[0] == 'mocked assertion error'
    mock_load_list_of_blocks.assert_called_once_with(ds=ds, play=play_instance, variable_manager=play_instance._variable_manager, loader=play_instance._loader)
