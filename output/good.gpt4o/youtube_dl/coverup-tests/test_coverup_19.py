# file youtube_dl/extractor/zdf.py:318-320
# lines [320]
# branches []

import pytest
from youtube_dl.extractor.zdf import ZDFChannelIE, ZDFIE

@pytest.fixture
def mock_zdfie_suitable(mocker):
    return mocker.patch('youtube_dl.extractor.zdf.ZDFIE.suitable')

def test_zdfchannelie_suitable_false(mock_zdfie_suitable):
    mock_zdfie_suitable.return_value = True
    assert not ZDFChannelIE.suitable('http://example.com')

def test_zdfchannelie_suitable_super(mock_zdfie_suitable, mocker):
    mock_zdfie_suitable.return_value = False
    mock_super_suitable = mocker.patch('youtube_dl.extractor.common.InfoExtractor.suitable', return_value=True)
    assert ZDFChannelIE.suitable('http://example.com')
    mock_super_suitable.assert_called_once_with('http://example.com')
