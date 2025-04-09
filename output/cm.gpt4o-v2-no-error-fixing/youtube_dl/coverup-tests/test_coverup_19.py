# file: youtube_dl/downloader/f4m.py:246-247
# asked: {"lines": [247], "branches": []}
# gained: {"lines": [247], "branches": []}

import pytest
from youtube_dl.downloader.f4m import _add_ns

def test_add_ns_default_version():
    result = _add_ns('testProp')
    assert result == '{http://ns.adobe.com/f4m/1.0}testProp'

def test_add_ns_specific_version():
    result = _add_ns('testProp', 2)
    assert result == '{http://ns.adobe.com/f4m/2.0}testProp'
