# file lib/ansible/playbook/play.py:312-313
# lines [312, 313]
# branches []

import pytest
from ansible.playbook.play import Play

# Assuming the Play class is part of a larger Ansible codebase and has dependencies
# that need to be mocked for isolated testing.

@pytest.fixture
def mock_base(mocker):
    mocker.patch('ansible.playbook.play.Base')
    mocker.patch('ansible.playbook.play.Taggable')
    mocker.patch('ansible.playbook.play.CollectionSearch')

def test_play_get_vars(mock_base):
    # Setup the Play instance
    play = Play()

    # Set some variables to the play instance
    expected_vars = {'key1': 'value1', 'key2': 'value2'}
    play.vars = expected_vars

    # Call get_vars and assert the returned vars are a copy of the original
    vars_copy = play.get_vars()
    assert vars_copy == expected_vars
    assert vars_copy is not expected_vars  # Ensure it's a copy, not the same object

    # Cleanup is handled by pytest's fixture scope
