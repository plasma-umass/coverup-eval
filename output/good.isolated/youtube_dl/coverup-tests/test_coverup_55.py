# file youtube_dl/extractor/nrk.py:497-499
# lines [499]
# branches []

import pytest
from youtube_dl.extractor.nrk import NRKTVSerieBaseIE

@pytest.fixture
def nrk_tv_serie_base_ie():
    return NRKTVSerieBaseIE()

def test_catalog_name_podcast(nrk_tv_serie_base_ie):
    assert nrk_tv_serie_base_ie._catalog_name('podcast') == 'podcast'
    assert nrk_tv_serie_base_ie._catalog_name('podkast') == 'podcast'

def test_catalog_name_series(nrk_tv_serie_base_ie):
    assert nrk_tv_serie_base_ie._catalog_name('series') == 'series'
    assert nrk_tv_serie_base_ie._catalog_name('anything_else') == 'series'
