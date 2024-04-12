# file youtube_dl/postprocessor/common.py:64-65
# lines [65]
# branches []

import pytest
from youtube_dl.postprocessor.common import PostProcessor

# Mocking the necessary parts of youtube_dl
class MockDownloader:
    def __init__(self, params):
        self.params = params

@pytest.fixture
def mock_cli_configuration_args(mocker):
    mocker.patch('youtube_dl.postprocessor.common.cli_configuration_args', return_value=['--custom-arg'])

def test_postprocessor_configuration_args(mock_cli_configuration_args):
    # Setup
    params = {'postprocessor_args': ['--custom-arg']}
    downloader = MockDownloader(params)
    pp = PostProcessor(downloader)

    # Test
    args = pp._configuration_args()
    
    # Verify
    assert args == ['--custom-arg'], "The postprocessor_args were not correctly retrieved"

    # Cleanup is not necessary as we are using mocks and not affecting global state
