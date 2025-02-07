# file: semantic_release/hvcs.py:442-452
# asked: {"lines": [442, 451, 452], "branches": []}
# gained: {"lines": [442, 451, 452], "branches": []}

import pytest
from unittest.mock import MagicMock, patch
from semantic_release.hvcs import check_build_status, get_hvcs

@pytest.fixture
def mock_get_hvcs(monkeypatch):
    mock_hvcs = MagicMock()
    mock_hvcs.check_build_status.return_value = True
    monkeypatch.setattr('semantic_release.hvcs.get_hvcs', lambda: mock_hvcs)
    return mock_hvcs

def test_check_build_status(mock_get_hvcs):
    owner = "test_owner"
    repository = "test_repo"
    ref = "test_ref"

    result = check_build_status(owner, repository, ref)

    mock_get_hvcs.check_build_status.assert_called_once_with(owner, repository, ref)
    assert result is True
