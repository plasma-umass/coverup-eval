# file lib/ansible/playbook/play.py:183-191
# lines [188, 189, 190, 191]
# branches []

import pytest
from ansible.errors import AnsibleParserError
from ansible.playbook.play import Play
from unittest.mock import MagicMock

# Assuming that load_list_of_blocks is a function that needs to be mocked
# and that it raises an AssertionError when a malformed block is encountered.

@pytest.fixture
def mock_load_list_of_blocks(mocker):
    return mocker.patch('ansible.playbook.play.load_list_of_blocks', side_effect=AssertionError("malformed block"))

def test_load_post_tasks_with_malformed_block(mock_load_list_of_blocks, mocker):
    play = Play()
    play._variable_manager = MagicMock()
    play._loader = MagicMock()
    play._ds = {'post_tasks': [{'malformed': 'block'}]}

    with pytest.raises(AnsibleParserError) as excinfo:
        play._load_post_tasks('post_tasks', play._ds['post_tasks'])

    assert "A malformed block was encountered while loading post_tasks" in str(excinfo.value)
    assert excinfo.value.obj == play._ds
    assert isinstance(excinfo.value.orig_exc, AssertionError)
