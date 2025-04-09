# file youtube_dl/postprocessor/common.py:64-65
# lines [65]
# branches []

import pytest
from unittest import mock
from youtube_dl.postprocessor.common import PostProcessor

def cli_configuration_args(params, key, default):
    return params.get(key, default)

class TestPostProcessor:
    @pytest.fixture
    def mock_downloader(self):
        class MockDownloader:
            params = {}
        return MockDownloader()

    def test_configuration_args_with_default(self, mock_downloader):
        pp = PostProcessor()
        pp._downloader = mock_downloader
        mock_downloader.params = {}
        default_args = ['--default']
        result = pp._configuration_args(default_args)
        assert result == default_args

    def test_configuration_args_with_params(self, mock_downloader):
        pp = PostProcessor()
        pp._downloader = mock_downloader
        mock_downloader.params = {'postprocessor_args': ['--param']}
        result = pp._configuration_args(['--default'])
        assert result == ['--param']
