# file lib/ansible/playbook/play.py:87-99
# lines [87, 88, 90, 91, 92, 93, 95, 96, 98, 99]
# branches []

import pytest
from unittest.mock import patch, MagicMock

# Assuming the Play class is imported from ansible.playbook.play
from ansible.playbook.play import Play

@pytest.fixture
def mock_context(mocker):
    mock_context = mocker.patch('ansible.playbook.play.context', autospec=True)
    mock_context.CLIARGS = {
        'tags': ['test_tag'],
        'skip_tags': ['skip_test_tag']
    }
    return mock_context

def test_play_initialization(mock_context):
    play = Play()
    
    assert play._included_conditional is None
    assert play._included_path is None
    assert play._removed_hosts == []
    assert play.ROLE_CACHE == {}
    assert play.only_tags == {'test_tag'}
    assert play.skip_tags == {'skip_test_tag'}
    assert play._action_groups == {}
    assert play._group_actions == {}

@pytest.fixture(autouse=True)
def cleanup():
    yield
    # Cleanup code if necessary
