# file: youtube_dl/extractor/zdf.py:322-378
# asked: {"lines": [323, 325, 327, 328, 329, 330, 332, 333], "branches": []}
# gained: {"lines": [323, 325, 327, 328, 329, 330, 332, 333], "branches": []}

import pytest
from youtube_dl.extractor.zdf import ZDFChannelIE
from youtube_dl.utils import orderedSet

@pytest.fixture
def zdf_channel_ie():
    return ZDFChannelIE()

def test_real_extract(zdf_channel_ie, mocker):
    url = 'https://www.zdf.de/some-channel'
    channel_id = 'some-channel'
    webpage = '''
    <html>
        <body>
            <div data-plusbar-url="http://example.com/video1.html"></div>
            <div data-plusbar-url="http://example.com/video2.html"></div>
        </body>
    </html>
    '''
    mocker.patch.object(zdf_channel_ie, '_match_id', return_value=channel_id)
    mocker.patch.object(zdf_channel_ie, '_download_webpage', return_value=webpage)
    mocker.patch.object(zdf_channel_ie, 'url_result', side_effect=lambda url, ie: {'url': url, 'ie_key': ie})
    mocker.patch.object(zdf_channel_ie, '_og_search_title', return_value='Test Channel')

    result = zdf_channel_ie._real_extract(url)

    assert result['entries'] == [
        {'url': 'http://example.com/video1.html', 'ie_key': 'ZDF'},
        {'url': 'http://example.com/video2.html', 'ie_key': 'ZDF'}
    ]
    assert result['id'] == channel_id
    assert result['title'] == 'Test Channel'
