# file: youtube_dl/extractor/safari.py:28-29
# asked: {"lines": [28, 29], "branches": []}
# gained: {"lines": [28, 29], "branches": []}

import pytest
from youtube_dl.extractor.safari import SafariBaseIE

class MockSafariBaseIE(SafariBaseIE):
    def _login(self):
        self.login_called = True

@pytest.fixture
def mock_safari_base_ie():
    return MockSafariBaseIE()

def test_real_initialize(mock_safari_base_ie):
    mock_safari_base_ie._real_initialize()
    assert mock_safari_base_ie.login_called
