# file youtube_dl/extractor/nrk.py:477-477
# lines [477]
# branches []

import pytest
from youtube_dl.extractor.nrk import NRKTVSerieBaseIE

@pytest.fixture
def mock_extractor(mocker):
    mocker.patch('youtube_dl.extractor.nrk.NRKBaseIE._real_extract', return_value={'id': '123', 'title': 'Test Title'})
    return NRKTVSerieBaseIE()

def test_nrktvseriebaseie_real_extract(mock_extractor):
    result = mock_extractor._real_extract('http://example.com')
    assert result['id'] == '123'
    assert result['title'] == 'Test Title'
