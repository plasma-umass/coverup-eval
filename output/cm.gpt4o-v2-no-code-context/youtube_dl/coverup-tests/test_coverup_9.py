# file: youtube_dl/extractor/zdf.py:318-320
# asked: {"lines": [320], "branches": []}
# gained: {"lines": [320], "branches": []}

import pytest
from youtube_dl.extractor.zdf import ZDFChannelIE, ZDFIE

class TestZDFChannelIE:
    @pytest.fixture
    def mock_zdfie_suitable(self, mocker):
        return mocker.patch('youtube_dl.extractor.zdf.ZDFIE.suitable')

    def test_zdfchannelie_suitable_false(self, mock_zdfie_suitable):
        mock_zdfie_suitable.return_value = True
        url = 'http://example.com'
        assert not ZDFChannelIE.suitable(url)

    def test_zdfchannelie_suitable_super(self, mock_zdfie_suitable, mocker):
        mock_zdfie_suitable.return_value = False
        mock_super_suitable = mocker.patch('youtube_dl.extractor.common.InfoExtractor.suitable', return_value=True)
        url = 'http://example.com'
        assert ZDFChannelIE.suitable(url)
        mock_super_suitable.assert_called_once_with(url)
