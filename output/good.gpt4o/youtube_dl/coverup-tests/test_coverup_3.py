# file youtube_dl/extractor/safari.py:28-29
# lines [28, 29]
# branches []

import pytest
from youtube_dl.extractor.safari import SafariBaseIE
from youtube_dl.extractor.common import InfoExtractor

class MockSafariBaseIE(SafariBaseIE):
    def _login(self):
        self.logged_in = True

@pytest.fixture
def mock_safari_base_ie(mocker):
    mocker.patch('youtube_dl.extractor.safari.SafariBaseIE._login', new=MockSafariBaseIE._login)
    return SafariBaseIE()

def test_safari_base_ie_real_initialize(mock_safari_base_ie):
    mock_safari_base_ie._real_initialize()
    assert hasattr(mock_safari_base_ie, 'logged_in')
    assert mock_safari_base_ie.logged_in
