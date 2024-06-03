# file semantic_release/hvcs.py:442-452
# lines [442, 451, 452]
# branches []

import pytest
from unittest.mock import patch, MagicMock
from semantic_release.hvcs import check_build_status

@pytest.fixture
def mock_get_hvcs(mocker):
    mock = mocker.patch('semantic_release.hvcs.get_hvcs')
    hvcs_instance = MagicMock()
    mock.return_value = hvcs_instance
    return hvcs_instance

def test_check_build_status_success(mock_get_hvcs):
    owner = "test_owner"
    repository = "test_repo"
    ref = "test_ref"
    
    mock_get_hvcs.check_build_status.return_value = True
    
    result = check_build_status(owner, repository, ref)
    
    mock_get_hvcs.check_build_status.assert_called_once_with(owner, repository, ref)
    assert result is True

def test_check_build_status_failure(mock_get_hvcs):
    owner = "test_owner"
    repository = "test_repo"
    ref = "test_ref"
    
    mock_get_hvcs.check_build_status.return_value = False
    
    result = check_build_status(owner, repository, ref)
    
    mock_get_hvcs.check_build_status.assert_called_once_with(owner, repository, ref)
    assert result is False
