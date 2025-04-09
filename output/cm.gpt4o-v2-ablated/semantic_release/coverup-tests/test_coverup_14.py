# file: semantic_release/hvcs.py:469-481
# asked: {"lines": [469, 481], "branches": []}
# gained: {"lines": [469, 481], "branches": []}

import pytest
from unittest.mock import Mock, patch
from semantic_release.hvcs import upload_to_release

@pytest.fixture
def mock_get_hvcs(monkeypatch):
    mock_hvcs = Mock()
    monkeypatch.setattr('semantic_release.hvcs.get_hvcs', lambda: mock_hvcs)
    return mock_hvcs

def test_upload_to_release_success(mock_get_hvcs):
    mock_get_hvcs.upload_dists.return_value = True
    result = upload_to_release('owner', 'repo', '1.0.0', 'path/to/dist')
    assert result is True
    mock_get_hvcs.upload_dists.assert_called_once_with('owner', 'repo', '1.0.0', 'path/to/dist')

def test_upload_to_release_failure(mock_get_hvcs):
    mock_get_hvcs.upload_dists.return_value = False
    result = upload_to_release('owner', 'repo', '1.0.0', 'path/to/dist')
    assert result is False
    mock_get_hvcs.upload_dists.assert_called_once_with('owner', 'repo', '1.0.0', 'path/to/dist')
