# file semantic_release/hvcs.py:245-272
# lines [267, 268]
# branches ['263->272', '266->267']

import pytest
from unittest.mock import patch
from semantic_release.hvcs import Github, logger

@pytest.fixture
def mock_logger_debug(mocker):
    return mocker.patch.object(logger, 'debug')

@pytest.fixture
def mock_create_release(mocker):
    return mocker.patch('semantic_release.hvcs.Github.create_release', return_value=False)

@pytest.fixture
def mock_get_release(mocker):
    return mocker.patch('semantic_release.hvcs.Github.get_release', return_value='123')

@pytest.fixture
def mock_edit_release(mocker):
    return mocker.patch('semantic_release.hvcs.Github.edit_release', return_value=True)

def test_post_release_changelog_existing_release(
    mock_logger_debug, mock_create_release, mock_get_release, mock_edit_release
):
    owner = 'owner'
    repo = 'repo'
    version = '1.0.0'
    changelog = 'Some changes'

    success = Github.post_release_changelog(owner, repo, version, changelog)

    mock_create_release.assert_called_once_with(owner, repo, f'v{version}', changelog)
    mock_get_release.assert_called_once_with(owner, repo, f'v{version}')
    mock_edit_release.assert_called_once_with(owner, repo, '123', changelog)
    mock_logger_debug.assert_any_call("Unsuccessful, looking for an existing release to update")
    mock_logger_debug.assert_any_call("Updating release 123")

    assert success is True
