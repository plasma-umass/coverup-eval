# file youtube_dl/extractor/safari.py:129-176
# lines [130, 132, 133, 134, 135, 136, 138, 140, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 157, 158, 159, 160, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 174, 175, 176]
# branches ['133->134', '133->138', '144->145', '144->148', '163->164', '163->174', '169->170', '169->174', '171->172', '171->174']

import pytest
from youtube_dl.extractor.safari import SafariIE
from unittest.mock import MagicMock

@pytest.fixture
def safari_extractor():
    extractor = SafariIE()
    extractor._PARTNER_ID = '12345'
    extractor._UICONF_ID = '67890'
    extractor._API_BASE = 'https://api.example.com'
    extractor.LOGGED_IN = True
    return extractor

def test_safari_extractor_real_extract(mocker, safari_extractor):
    # Mocking the necessary methods and properties
    mocker.patch('youtube_dl.extractor.safari.SafariIE._download_webpage_handle', return_value=('webpage', MagicMock(geturl=lambda: 'https://example.com/course_id/part')))
    mocker.patch('youtube_dl.extractor.safari.SafariIE._search_regex', side_effect=lambda *args, **kwargs: kwargs.get('default') or '123')
    mocker.patch('youtube_dl.extractor.safari.SafariIE._download_json', return_value={'session': 'session_id'})
    mocker.patch('youtube_dl.extractor.safari.SafariIE.url_result')

    # Mocking the re.match to simulate a URL match
    mock_match = MagicMock()
    mock_match.group.side_effect = lambda x: {'reference_id': None, 'course_id': 'course_id', 'part': 'part'}.get(x)
    mocker.patch('re.match', return_value=mock_match)

    # Running the test
    test_url = 'https://example.com/course_id/part'
    safari_extractor._real_extract(test_url)

    # Assertions to check if the code coverage is improved
    safari_extractor._download_webpage_handle.assert_called_once_with(test_url, 'course_id-part')
    assert safari_extractor._search_regex.call_count == 3
    safari_extractor._download_json.assert_called_once_with(
        'https://api.example.com/player/kaltura_session/?reference_id=123',
        'course_id-part', 'Downloading kaltura session JSON',
        'Unable to download kaltura session JSON', fatal=False,
        headers={'Accept': 'application/json'}
    )
    safari_extractor.url_result.assert_called_once()
    result_url, result_ie = safari_extractor.url_result.call_args[0]
    assert 'https://cdnapisec.kaltura.com/html5/html5lib/v2.37.1/mwEmbedFrame.php' in result_url
    assert 'Kaltura' == result_ie
