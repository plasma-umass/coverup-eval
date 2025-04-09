# file lib/ansible/playbook/play.py:312-313
# lines [313]
# branches []

import pytest
from ansible.playbook.play import Play

# Assuming the Play class is part of a larger module and has dependencies that need to be mocked
# We will use pytest-mock to create the necessary mocks

@pytest.fixture
def mock_base(mocker):
    mocker.patch('ansible.playbook.play.Base', autospec=True)

@pytest.fixture
def mock_taggable(mocker):
    mocker.patch('ansible.playbook.play.Taggable', autospec=True)

@pytest.fixture
def mock_collection_search(mocker):
    mocker.patch('ansible.playbook.play.CollectionSearch', autospec=True)

def test_play_get_vars(mock_base, mock_taggable, mock_collection_search):
    # Given a Play instance with some vars
    play = Play()
    expected_vars = {'key1': 'value1', 'key2': 'value2'}
    play.vars = expected_vars

    # When calling get_vars
    result_vars = play.get_vars()

    # Then the result should be a copy of the vars
    assert result_vars == expected_vars
    assert result_vars is not expected_vars  # Ensuring a copy is returned, not the original

    # Cleanup is handled by pytest fixtures automatically
