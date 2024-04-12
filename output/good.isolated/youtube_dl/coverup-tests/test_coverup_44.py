# file youtube_dl/extractor/nrk.py:596-612
# lines [597, 598, 599, 600, 601, 602, 604, 605, 606, 607, 609, 610, 611, 612]
# branches []

import pytest
from youtube_dl.extractor.nrk import NRKTVSeasonIE
from youtube_dl.utils import ExtractorError

def test_nrk_tv_season_extraction(mocker):
    # Mock the _VALID_URL regex match object with required groups
    mock_match = mocker.Mock()
    mock_match.group.return_value = 'mock_group_value'
    mocker.patch('re.match', return_value=mock_match)

    # Mock the _call_api method to return a fake response
    fake_api_response = {
        'titles': {'title': 'Fake Season Title'},
    }
    mocker.patch.object(NRKTVSeasonIE, '_call_api', return_value=fake_api_response)

    # Mock the _entries method to return a list of fake entries
    fake_entries = ['entry1', 'entry2']
    mocker.patch.object(NRKTVSeasonIE, '_entries', return_value=fake_entries)

    # Create an instance of the extractor
    extractor = NRKTVSeasonIE()

    # Call the _real_extract method with a fake URL
    result = extractor._real_extract('http://mock_url')

    # Assertions to check if the result is as expected
    assert result['id'] == 'mock_group_value/mock_group_value'
    assert result['title'] == 'Fake Season Title'
    assert result['entries'] == fake_entries

    # Clean up by stopping the patches
    mocker.stopall()
