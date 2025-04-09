# file: youtube_dl/extractor/nrk.py:802-827
# asked: {"lines": [824, 827], "branches": []}
# gained: {"lines": [824, 827], "branches": []}

import pytest
from youtube_dl.extractor.nrk import NRKPlaylistIE

class TestNRKPlaylistIE:
    
    @pytest.fixture
    def nrk_playlist_ie(self):
        return NRKPlaylistIE()

    def test_extract_title(self, nrk_playlist_ie, mocker):
        mocker.patch.object(nrk_playlist_ie, '_og_search_title', return_value='Test Title')
        webpage = '<html><head><meta property="og:title" content="Test Title"></head></html>'
        title = nrk_playlist_ie._extract_title(webpage)
        assert title == 'Test Title'
        nrk_playlist_ie._og_search_title.assert_called_once_with(webpage, fatal=False)

    def test_extract_description(self, nrk_playlist_ie, mocker):
        mocker.patch.object(nrk_playlist_ie, '_og_search_description', return_value='Test Description')
        webpage = '<html><head><meta property="og:description" content="Test Description"></head></html>'
        description = nrk_playlist_ie._extract_description(webpage)
        assert description == 'Test Description'
        nrk_playlist_ie._og_search_description.assert_called_once_with(webpage)
