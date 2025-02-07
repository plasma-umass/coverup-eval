# file: semantic_release/dist.py:12-17
# asked: {"lines": [12, 13, 14, 15, 16, 17], "branches": []}
# gained: {"lines": [12, 13, 14, 15, 16, 17], "branches": []}

import pytest
from unittest.mock import patch

@pytest.fixture
def mock_config():
    with patch('semantic_release.dist.config') as mock_config:
        yield mock_config

def test_should_build_with_build_command(mock_config):
    mock_config.get.side_effect = lambda key: {
        'upload_to_pypi': True,
        'upload_to_release': False,
        'build_command': 'build'
    }[key]
    
    from semantic_release.dist import should_build
    assert should_build() is True

def test_should_build_without_build_command(mock_config):
    mock_config.get.side_effect = lambda key: {
        'upload_to_pypi': True,
        'upload_to_release': False,
        'build_command': 'false'
    }[key]
    
    from semantic_release.dist import should_build
    assert should_build() is False

def test_should_build_without_upload_pypi_and_release(mock_config):
    mock_config.get.side_effect = lambda key: {
        'upload_to_pypi': False,
        'upload_to_release': False,
        'build_command': 'build'
    }[key]
    
    from semantic_release.dist import should_build
    assert should_build() is False

def test_should_build_with_upload_release(mock_config):
    mock_config.get.side_effect = lambda key: {
        'upload_to_pypi': False,
        'upload_to_release': True,
        'build_command': 'build'
    }[key]
    
    from semantic_release.dist import should_build
    assert should_build() is True
