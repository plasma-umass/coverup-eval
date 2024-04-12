# file semantic_release/hvcs.py:274-314
# lines [274, 275, 276, 277, 291, 293, 294, 295, 297, 298, 299, 300, 301, 302, 304, 307, 308, 311, 312, 313, 314]
# branches ['294->295', '294->297']

import os
import pytest
from unittest.mock import Mock
from requests.exceptions import HTTPError
from semantic_release.hvcs import Github

@pytest.fixture
def mock_github_session(mocker):
    mock = mocker.patch('semantic_release.hvcs.Github.session', autospec=True)
    mock.return_value.post.return_value = Mock(status_code=200, url='http://fake_url')
    return mock.return_value

@pytest.fixture
def mock_open(mocker):
    mock = mocker.patch('semantic_release.hvcs.open', mocker.mock_open(read_data=b'fake_content'))
    return mock

@pytest.fixture
def mock_logger(mocker):
    return mocker.patch('semantic_release.hvcs.logger', autospec=True)

@pytest.fixture
def mock_mimetypes(mocker):
    mocker.patch('semantic_release.hvcs.mimetypes.guess_type', return_value=(None, None))

def test_upload_asset_success(mock_github_session, mock_open, mock_logger, mock_mimetypes):
    assert Github.upload_asset('owner', 'repo', 1, 'file.txt', 'label') is True
    mock_github_session.post.assert_called_once()
    mock_logger.debug.assert_called_once()
    mock_logger.warning.assert_not_called()

def test_upload_asset_http_error(mock_github_session, mock_open, mock_logger, mock_mimetypes):
    mock_github_session.post.side_effect = HTTPError('error')
    assert Github.upload_asset('owner', 'repo', 1, 'file.txt', 'label') is False
    mock_github_session.post.assert_called_once()
    mock_logger.warning.assert_called_once()
    mock_logger.debug.assert_not_called()
