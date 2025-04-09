# file lib/ansible/playbook/play.py:322-323
# lines [323]
# branches []

import pytest
from ansible.playbook.play import Play

# Assuming that the Play class is part of a larger Ansible codebase and has dependencies
# that need to be mocked for isolation. If not, the test can be simplified.

@pytest.fixture
def mock_play(mocker):
    # Mocking the Play class' __init__ to avoid side effects
    mocker.patch.object(Play, '__init__', return_value=None)
    play = Play()
    play.handlers = ['handler1', 'handler2', 'handler3']
    return play

def test_get_handlers(mock_play):
    # Test to ensure that get_handlers method returns a copy of the handlers list
    handlers = mock_play.get_handlers()
    assert handlers == ['handler1', 'handler2', 'handler3']
    # Verify that it's a copy by modifying the original list and checking the result
    mock_play.handlers.append('handler4')
    assert handlers == ['handler1', 'handler2', 'handler3']
