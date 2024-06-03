# file youtube_dl/extractor/nrk.py:497-499
# lines [499]
# branches []

import pytest
from youtube_dl.extractor.nrk import NRKTVSerieBaseIE

def test_catalog_name_podcast():
    assert NRKTVSerieBaseIE._catalog_name('podcast') == 'podcast'

def test_catalog_name_podkast():
    assert NRKTVSerieBaseIE._catalog_name('podkast') == 'podcast'

def test_catalog_name_series():
    assert NRKTVSerieBaseIE._catalog_name('other') == 'series'
