# file lib/ansible/playbook/play.py:183-191
# lines [183, 188, 189, 190, 191]
# branches []

import pytest
from unittest.mock import Mock, patch
from ansible.playbook.play import Play
from ansible.errors import AnsibleParserError

@pytest.fixture
def mock_load_list_of_blocks(mocker):
    return mocker.patch('ansible.playbook.play.load_list_of_blocks')

def test_load_post_tasks_success(mock_load_list_of_blocks):
    mock_load_list_of_blocks.return_value = 'mocked_blocks'
    play = Play()
    play._variable_manager = Mock()
    play._loader = Mock()
    play._ds = Mock()

    result = play._load_post_tasks('attr', 'ds')
    assert result == 'mocked_blocks'

def test_load_post_tasks_failure(mock_load_list_of_blocks):
    mock_load_list_of_blocks.side_effect = AssertionError('mocked error')
    play = Play()
    play._variable_manager = Mock()
    play._loader = Mock()
    play._ds = Mock()

    with pytest.raises(AnsibleParserError) as excinfo:
        play._load_post_tasks('attr', 'ds')
    assert str(excinfo.value) == "A malformed block was encountered while loading post_tasks. mocked error"
    assert excinfo.value.obj == play._ds
    assert isinstance(excinfo.value.orig_exc, AssertionError)
