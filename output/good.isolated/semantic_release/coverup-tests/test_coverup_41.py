# file semantic_release/dist.py:20-22
# lines [20, 21, 22]
# branches []

import pytest
from unittest.mock import patch
from semantic_release.dist import should_remove_dist

@pytest.fixture
def mock_should_build(mocker):
    return mocker.patch('semantic_release.dist.should_build', return_value=True)

@pytest.fixture
def mock_config_get(mocker):
    return mocker.patch('semantic_release.settings.config.get')

def test_should_remove_dist_when_config_set_and_should_build_true(mock_should_build, mock_config_get):
    mock_config_get.return_value = True
    assert should_remove_dist() is True
    mock_config_get.assert_called_once_with("remove_dist")
    mock_should_build.assert_called_once()

def test_should_remove_dist_when_config_not_set(mock_should_build, mock_config_get):
    mock_config_get.return_value = False
    assert should_remove_dist() is False
    mock_config_get.assert_called_once_with("remove_dist")
    mock_should_build.assert_not_called()
