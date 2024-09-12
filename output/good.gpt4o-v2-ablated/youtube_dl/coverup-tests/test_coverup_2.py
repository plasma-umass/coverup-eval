# file: youtube_dl/extractor/safari.py:28-29
# asked: {"lines": [28, 29], "branches": []}
# gained: {"lines": [28, 29], "branches": []}

import pytest
from youtube_dl.extractor.safari import SafariBaseIE

class MockSafariBaseIE(SafariBaseIE):
    def _login(self):
        self.logged_in = True

@pytest.fixture
def safari_base_ie():
    return MockSafariBaseIE()

def test_real_initialize(safari_base_ie, mocker):
    mock_login = mocker.patch.object(safari_base_ie, '_login', wraps=safari_base_ie._login)
    safari_base_ie._real_initialize()
    mock_login.assert_called_once()
    assert safari_base_ie.logged_in
