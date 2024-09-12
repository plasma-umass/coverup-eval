# file: youtube_dl/extractor/ufctv.py:7-10
# asked: {"lines": [7, 8, 9, 10], "branches": []}
# gained: {"lines": [7, 8, 9, 10], "branches": []}

import pytest
from youtube_dl.extractor.ufctv import UFCTVIE
from youtube_dl.extractor.imggaming import ImgGamingBaseIE

def test_ufctvie_class_attributes():
    assert UFCTVIE._VALID_URL == ImgGamingBaseIE._VALID_URL_TEMPL % r'(?:(?:app|www)\.)?(?:ufc\.tv|(?:ufc)?fightpass\.com)|ufcfightpass\.img(?:dge|gaming)\.com'
    assert UFCTVIE._NETRC_MACHINE == 'ufctv'
    assert UFCTVIE._REALM == 'ufc'
