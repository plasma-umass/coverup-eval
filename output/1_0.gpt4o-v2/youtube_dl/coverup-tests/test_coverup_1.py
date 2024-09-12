# file: youtube_dl/extractor/ufctv.py:13-16
# asked: {"lines": [13, 14, 15, 16], "branches": []}
# gained: {"lines": [13, 14, 15, 16], "branches": []}

import pytest
from youtube_dl.extractor.ufctv import UFCArabiaIE
from youtube_dl.extractor.imggaming import ImgGamingBaseIE

def test_ufcarabia_ie_attributes():
    assert hasattr(UFCArabiaIE, '_VALID_URL')
    assert UFCArabiaIE._VALID_URL == ImgGamingBaseIE._VALID_URL_TEMPL % r'(?:(?:app|www)\.)?ufcarabia\.(?:ae|com)'
    assert hasattr(UFCArabiaIE, '_NETRC_MACHINE')
    assert UFCArabiaIE._NETRC_MACHINE == 'ufcarabia'
    assert hasattr(UFCArabiaIE, '_REALM')
    assert UFCArabiaIE._REALM == 'admufc'
