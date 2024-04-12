# file youtube_dl/extractor/nrk.py:501-530
# lines [501, 502, 503, 504, 505, 506, 507, 508, 510, 511, 512, 513, 514, 515, 516, 518, 519, 520, 521, 522, 523, 524, 525, 526, 527, 528, 529, 530]
# branches ['502->exit', '502->503', '504->505', '504->506', '507->508', '507->510', '515->516', '515->518', '523->524', '523->525', '529->502', '529->530']

import itertools
from youtube_dl.extractor.nrk import NRKTVSerieBaseIE
from youtube_dl.utils import try_get
from youtube_dl.compat import compat_str
import pytest

class MockNRKTVSerieBaseIE(NRKTVSerieBaseIE):
    def _call_api(self, *args, **kwargs):
        return None

@pytest.fixture
def mock_extractor(mocker):
    extractor = MockNRKTVSerieBaseIE()
    mocker.patch.object(extractor, '_call_api', return_value=None)
    return extractor

def test_entries_break_on_non_dict_embedded(mock_extractor):
    data = {'_embedded': 'not a dict'}
    display_id = 'test'
    entries = list(mock_extractor._entries(data, display_id))
    assert not entries

def test_entries_break_on_missing_assets_key(mock_extractor):
    data = {'_embedded': {}}
    display_id = 'test'
    entries = list(mock_extractor._entries(data, display_id))
    assert not entries

def test_entries_break_on_missing_next_url_path(mock_extractor):
    data = {
        '_embedded': {
            'test_assets': {
                '_embedded': {
                    'test_assets': []
                }
            }
        }
    }
    display_id = 'test'
    entries = list(mock_extractor._entries(data, display_id))
    assert not entries

def test_entries_break_on_call_api_returning_none(mock_extractor):
    data = {
        '_embedded': {
            'test_assets': {
                '_embedded': {
                    'test_assets': []
                },
                '_links': {
                    'next': {
                        'href': 'next_url'
                    }
                }
            }
        }
    }
    display_id = 'test'
    entries = list(mock_extractor._entries(data, display_id))
    assert not entries
