# file: youtube_dl/extractor/safari.py:28-29
# asked: {"lines": [28, 29], "branches": []}
# gained: {"lines": [28, 29], "branches": []}

import pytest
from youtube_dl.extractor.safari import SafariBaseIE
from youtube_dl.utils import ExtractorError

class TestSafariBaseIE:
    @pytest.fixture
    def safari_ie(self, monkeypatch):
        ie = SafariBaseIE()

        def mock_get_login_info():
            return 'username', 'password'

        def mock_download_webpage_handle(url, *args, **kwargs):
            class MockResponse:
                def geturl(self):
                    return 'https://learning.oreilly.com/home/'

            return None, MockResponse()

        monkeypatch.setattr(ie, '_get_login_info', mock_get_login_info)
        monkeypatch.setattr(ie, '_download_webpage_handle', mock_download_webpage_handle)
        return ie

    def test_real_initialize(self, safari_ie):
        safari_ie._real_initialize()
        assert safari_ie.LOGGED_IN is True
