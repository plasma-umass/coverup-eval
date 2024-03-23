# file semantic_release/hvcs.py:245-272
# lines [245, 246, 247, 259, 260, 261, 263, 264, 265, 266, 267, 268, 270, 272]
# branches ['263->264', '263->272', '266->267', '266->270']

import pytest
from unittest.mock import patch
from semantic_release.hvcs import Github

@pytest.fixture
def mock_github(mocker):
    mocker.patch('semantic_release.hvcs.Github.create_release', return_value=False)
    mocker.patch('semantic_release.hvcs.Github.get_release', return_value=None)
    mocker.patch('semantic_release.hvcs.Github.edit_release', return_value=True)

def test_post_release_changelog_failure_then_success(mock_github):
    owner = 'owner'
    repo = 'repo'
    version = '1.0.0'
    changelog = 'Some changes'

    with patch('semantic_release.hvcs.logger') as mock_logger:
        success = Github.post_release_changelog(owner, repo, version, changelog)

    assert not success
    mock_logger.debug.assert_any_call("Attempting to create release for v1.0.0")
    mock_logger.debug.assert_any_call("Unsuccessful, looking for an existing release to update")
    mock_logger.debug.assert_any_call("Existing release not found")
