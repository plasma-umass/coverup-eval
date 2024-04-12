# file semantic_release/hvcs.py:442-452
# lines [442, 451, 452]
# branches []

import pytest
from unittest.mock import MagicMock
from semantic_release.hvcs import check_build_status, get_hvcs

@pytest.fixture
def mock_hvcs(mocker):
    hvcs_mock = MagicMock()
    mocker.patch('semantic_release.hvcs.get_hvcs', return_value=hvcs_mock)
    return hvcs_mock

def test_check_build_status(mock_hvcs):
    owner = "test_owner"
    repository = "test_repo"
    ref = "test_ref"
    mock_hvcs.check_build_status.return_value = True

    result = check_build_status(owner, repository, ref)

    assert result is True
    mock_hvcs.check_build_status.assert_called_once_with(owner, repository, ref)
