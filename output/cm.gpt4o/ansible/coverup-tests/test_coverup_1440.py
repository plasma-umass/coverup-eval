# file lib/ansible/galaxy/api.py:431-440
# lines [436, 437, 438, 439, 440]
# branches []

import pytest
from unittest import mock
from ansible.galaxy.api import GalaxyAPI

@pytest.fixture
def mock_open_url(mocker):
    return mocker.patch('ansible.galaxy.api.open_url')

@pytest.fixture
def mock_urljoin(mocker):
    return mocker.patch('ansible.galaxy.api._urljoin', return_value='http://example.com/api/v1/tokens')

@pytest.fixture
def mock_user_agent(mocker):
    return mocker.patch('ansible.galaxy.api.user_agent', return_value='test-agent')

@pytest.fixture
def mock_to_text(mocker):
    return mocker.patch('ansible.galaxy.api.to_text', return_value='{"token": "fake-token"}')

@pytest.fixture
def mock_call_galaxy(mocker):
    return mocker.patch('ansible.galaxy.api.GalaxyAPI._call_galaxy', return_value={'available_versions': {'v1': 'v1'}})

@pytest.fixture
def galaxy_api(mock_call_galaxy):
    api = GalaxyAPI(galaxy='test-galaxy', name='test-name', url='http://example.com')
    api._available_api_versions = {'v1': 'v1'}
    return api

def test_authenticate(galaxy_api, mock_open_url, mock_urljoin, mock_user_agent, mock_to_text):
    github_token = 'fake-github-token'
    mock_open_url.return_value.read.return_value = '{"token": "fake-token"}'
    
    result = galaxy_api.authenticate(github_token)
    
    mock_urljoin.assert_called_once_with(galaxy_api.api_server, galaxy_api.available_api_versions['v1'], "tokens")
    mock_open_url.assert_called_once_with(
        'http://example.com/api/v1/tokens/',
        data='github_token=fake-github-token',
        validate_certs=galaxy_api.validate_certs,
        method="POST",
        http_agent='test-agent'
    )
    mock_to_text.assert_called_once_with(mock_open_url.return_value.read.return_value, errors='surrogate_or_strict')
    
    assert result == {"token": "fake-token"}
