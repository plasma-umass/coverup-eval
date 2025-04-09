# file: semantic_release/hvcs.py:469-481
# asked: {"lines": [469, 481], "branches": []}
# gained: {"lines": [469, 481], "branches": []}

import pytest
from unittest.mock import patch, MagicMock
from semantic_release.hvcs import upload_to_release, get_hvcs
from semantic_release.errors import ImproperConfigurationError

@pytest.fixture
def mock_get_hvcs(monkeypatch):
    mock_hvcs = MagicMock()
    mock_hvcs.upload_dists.return_value = True
    monkeypatch.setattr('semantic_release.hvcs.get_hvcs', lambda: mock_hvcs)
    return mock_hvcs

def test_upload_to_release_success(mock_get_hvcs):
    owner = "test_owner"
    repository = "test_repo"
    version = "1.0.0"
    path = "/fake/path"

    result = upload_to_release(owner, repository, version, path)

    mock_get_hvcs.upload_dists.assert_called_once_with(owner, repository, version, path)
    assert result is True

def test_upload_to_release_improper_configuration(monkeypatch):
    monkeypatch.setattr('semantic_release.hvcs.get_hvcs', lambda: (_ for _ in ()).throw(ImproperConfigurationError('Invalid HVCS')))

    owner = "test_owner"
    repository = "test_repo"
    version = "1.0.0"
    path = "/fake/path"

    with pytest.raises(ImproperConfigurationError, match='Invalid HVCS'):
        upload_to_release(owner, repository, version, path)
