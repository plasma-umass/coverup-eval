# file: youtube_dl/postprocessor/common.py:64-65
# asked: {"lines": [65], "branches": []}
# gained: {"lines": [65], "branches": []}

import pytest
from youtube_dl.postprocessor.common import PostProcessor
from youtube_dl.utils import cli_configuration_args

class MockDownloader:
    def __init__(self, params):
        self.params = params

@pytest.fixture
def mock_downloader():
    return MockDownloader(params={})

def test_configuration_args_with_default(mock_downloader):
    pp = PostProcessor()
    pp._downloader = mock_downloader
    result = pp._configuration_args(default=['default_arg'])
    assert result == ['default_arg']

def test_configuration_args_with_params(mock_downloader):
    mock_downloader.params['postprocessor_args'] = ['param_arg']
    pp = PostProcessor()
    pp._downloader = mock_downloader
    result = pp._configuration_args(default=['default_arg'])
    assert result == ['param_arg']

def test_configuration_args_with_empty_params(mock_downloader):
    mock_downloader.params['postprocessor_args'] = []
    pp = PostProcessor()
    pp._downloader = mock_downloader
    result = pp._configuration_args(default=['default_arg'])
    assert result == []

def test_configuration_args_with_no_postprocessor_args(mock_downloader):
    pp = PostProcessor()
    pp._downloader = mock_downloader
    result = pp._configuration_args(default=['default_arg'])
    assert result == ['default_arg']
