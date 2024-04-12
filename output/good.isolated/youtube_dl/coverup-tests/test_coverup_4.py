# file youtube_dl/extractor/tvplay.py:338-377
# lines [338, 339, 345, 346, 347, 348, 349, 350, 351, 352, 353, 354, 355, 356, 358, 359, 361, 363, 364, 365, 367, 368, 369, 370, 371, 372, 373, 374, 376]
# branches []

import pytest
from youtube_dl.extractor.tvplay import ViafreeIE

@pytest.fixture
def viafree_extractor():
    return ViafreeIE()

def test_viafree_extractor_valid_url(viafree_extractor):
    valid_urls = [
        'http://www.viafree.no/programmer/underholdning/det-beste-vorspielet/sesong-2/episode-1',
        'http://www.viafree.se/program/reality/sommaren-med-youtube-stjarnorna/sasong-1/avsnitt-1',
        'http://www.viafree.se/program/reality/sommaren-med-youtube-stjarnorna/sasong-1/avsnitt-2',
        'http://www.viafree.se/program/livsstil/husraddarna/sasong-2/avsnitt-2',
        'http://www.viafree.dk/programmer/reality/paradise-hotel/saeson-7/episode-5'
    ]
    for url in valid_urls:
        assert viafree_extractor.suitable(url), f"URL should be suitable: {url}"

def test_viafree_extractor_invalid_url(viafree_extractor):
    invalid_urls = [
        'http://www.viafree.com/invalid/programmer/underholdning/det-beste-vorspielet/sesong-2/episode-1',
        'http://www.viafree.it/program/reality/sommaren-med-youtube-stjarnorna/sasong-1/avsnitt-1',
        'http://www.viafree.jp/program/reality/sommaren-med-youtube-stjarnorna/sasong-1/avsnitt-2',
        'http://www.viafree.br/program/livsstil/husraddarna/sasong-2/avsnitt-2',
        'http://www.viafree.cn/programmer/reality/paradise-hotel/saeson-7/episode-5'
    ]
    for url in invalid_urls:
        assert not viafree_extractor.suitable(url), f"URL should not be suitable: {url}"
