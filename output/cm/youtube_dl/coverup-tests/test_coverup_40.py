# file youtube_dl/extractor/soundgasm.py:9-54
# lines [25, 26, 28, 30, 31, 32, 34, 35, 36, 38, 39, 41, 43, 44, 46, 47, 48, 49, 50, 51, 52, 53]
# branches []

import pytest
from youtube_dl.extractor.soundgasm import SoundgasmIE

@pytest.fixture
def soundgasm_ie(mocker):
    # Mock the _download_webpage method to return a fixed HTML content
    mocker.patch('youtube_dl.extractor.common.InfoExtractor._download_webpage', return_value='''
        <div class="jp-title">Test Title</div>
        <div class="jp-description">Test Description</div>
        <script type="text/javascript">
        m4a: "http://testserver/test_audio.m4a"
        </script>
    ''')

    # Mock the _html_search_regex method to return a fixed audio URL
    mocker.patch('youtube_dl.extractor.common.InfoExtractor._html_search_regex', side_effect=[
        'http://testserver/test_audio.m4a',  # audio URL
        'Test Description'  # description
    ])

    # Mock the _search_regex method to return a fixed title
    mocker.patch('youtube_dl.extractor.common.InfoExtractor._search_regex', side_effect=[
        'Test Title',  # title
        'test_audio'  # audio id
    ])

    return SoundgasmIE()

def test_soundgasm_extraction(soundgasm_ie):
    # Test URL that matches the _VALID_URL pattern
    test_url = 'http://soundgasm.net/u/testuser/TestTitle'

    # Extract information
    result = soundgasm_ie._real_extract(test_url)

    # Assertions to check if the extracted information is correct
    assert result['id'] == 'test_audio'
    assert result['display_id'] == 'TestTitle'
    assert result['url'] == 'http://testserver/test_audio.m4a'
    assert result['vcodec'] == 'none'
    assert result['title'] == 'Test Title'
    assert result['description'] == 'Test Description'
    assert result['uploader'] == 'testuser'
