# file youtube_dl/extractor/safari.py:28-29
# lines [28, 29]
# branches []

import pytest
from youtube_dl.extractor.safari import SafariBaseIE

class MockSafariBaseIE(SafariBaseIE):
    def _login(self):
        pass  # Mock the login method to avoid actual network calls

@pytest.fixture
def mock_safari_base_ie(mocker):
    mocker.patch.object(MockSafariBaseIE, '_login')
    return MockSafariBaseIE()

def test_safari_base_ie_real_initialize(mock_safari_base_ie):
    mock_safari_base_ie._real_initialize()
    mock_safari_base_ie._login.assert_called_once()
