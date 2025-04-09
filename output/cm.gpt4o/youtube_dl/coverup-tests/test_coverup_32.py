# file youtube_dl/downloader/f4m.py:246-247
# lines [247]
# branches []

import pytest
from youtube_dl.downloader.f4m import _add_ns

def test_add_ns():
    # Test with default version
    result = _add_ns('testprop')
    assert result == '{http://ns.adobe.com/f4m/1.0}testprop'
    
    # Test with specific version
    result = _add_ns('testprop', 2)
    assert result == '{http://ns.adobe.com/f4m/2.0}testprop'
    
    # Test with another specific version
    result = _add_ns('testprop', 3)
    assert result == '{http://ns.adobe.com/f4m/3.0}testprop'
