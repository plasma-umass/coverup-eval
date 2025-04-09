# file: lib/ansible/playbook/play.py:87-99
# asked: {"lines": [87, 88, 90, 91, 92, 93, 95, 96, 98, 99], "branches": []}
# gained: {"lines": [87, 88, 90, 91, 92, 93, 95, 96, 98, 99], "branches": []}

import pytest
from ansible.playbook.play import Play
from ansible import context

@pytest.fixture
def mock_context(mocker):
    mocker.patch.object(context.CLIARGS, 'get', side_effect=lambda key, default=None: {
        'tags': ['test_tag'],
        'skip_tags': ['skip_test_tag']
    }.get(key, default))

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
