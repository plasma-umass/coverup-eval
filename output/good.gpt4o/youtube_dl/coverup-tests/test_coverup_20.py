# file youtube_dl/extractor/tvplay.py:378-380
# lines [380]
# branches []

import pytest
from youtube_dl.extractor.tvplay import TVPlayIE, ViafreeIE

@pytest.fixture
def mock_tvplayie_suitable(mocker):
    return mocker.patch('youtube_dl.extractor.tvplay.TVPlayIE.suitable')

def test_viafreeie_suitable_false(mock_tvplayie_suitable):
    mock_tvplayie_suitable.return_value = True
    assert not ViafreeIE.suitable('http://example.com')

def test_viafreeie_suitable_super(mock_tvplayie_suitable, mocker):
    mock_tvplayie_suitable.return_value = False
    mock_super_suitable = mocker.patch('youtube_dl.extractor.common.InfoExtractor.suitable', return_value=True)
    assert ViafreeIE.suitable('http://example.com')
    mock_super_suitable.assert_called_once_with('http://example.com')
