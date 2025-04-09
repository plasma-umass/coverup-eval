# file: tornado/escape.py:275-377
# asked: {"lines": [275, 277, 278, 279, 280, 311, 312, 314, 315, 316, 317, 318, 320, 321, 323, 324, 325, 327, 328, 330, 333, 334, 335, 336, 337, 339, 341, 342, 347, 348, 349, 350, 351, 354, 355, 357, 358, 360, 361, 362, 364, 365, 369, 371, 376, 377], "branches": [[311, 312], [311, 314], [317, 318], [317, 320], [320, 321], [320, 323], [324, 325], [324, 327], [327, 328], [327, 330], [334, 335], [334, 371], [336, 337], [336, 339], [342, 347], [342, 354], [354, 355], [354, 357], [357, 358], [357, 371], [360, 361], [360, 362], [364, 365], [364, 369]]}
# gained: {"lines": [275, 277, 278, 279, 280, 311, 312, 314, 315, 316, 317, 318, 320, 323, 324, 325, 327, 328, 330, 333, 334, 335, 336, 337, 339, 341, 342, 347, 348, 349, 350, 351, 354, 357, 358, 360, 362, 364, 369, 371, 376, 377], "branches": [[311, 312], [311, 314], [317, 318], [317, 320], [320, 323], [324, 325], [324, 327], [327, 328], [327, 330], [334, 335], [334, 371], [336, 337], [336, 339], [342, 347], [354, 357], [357, 358], [360, 362], [364, 369]]}

import pytest
from tornado.escape import linkify

def test_linkify_basic():
    text = "Check this out: http://example.com"
    result = linkify(text)
    assert result == 'Check this out: <a href="http://example.com">http://example.com</a>'

def test_linkify_with_shorten():
    text = "Check this out: http://example.com/this/is/a/very/long/url/that/needs/to/be/shortened"
    result = linkify(text, shorten=True)
    assert '...' in result

def test_linkify_with_extra_params():
    text = "Check this out: http://example.com"
    result = linkify(text, extra_params='rel="nofollow"')
    assert result == 'Check this out: <a href="http://example.com" rel="nofollow">http://example.com</a>'

def test_linkify_with_extra_params_callable():
    def extra_params_cb(url):
        if url.startswith("http://example.com"):
            return 'class="internal"'
        else:
            return 'class="external" rel="nofollow"'
    text = "Check this out: http://example.com"
    result = linkify(text, extra_params=extra_params_cb)
    assert result == 'Check this out: <a href="http://example.com" class="internal">http://example.com</a>'

def test_linkify_require_protocol():
    text = "Check this out: www.example.com"
    result = linkify(text, require_protocol=True)
    assert result == 'Check this out: www.example.com'

def test_linkify_permitted_protocols():
    text = "Check this out: ftp://example.com"
    result = linkify(text, permitted_protocols=["http", "https", "ftp"])
    assert result == 'Check this out: <a href="ftp://example.com">ftp://example.com</a>'

def test_linkify_disallowed_protocol():
    text = "Check this out: javascript:alert('XSS')"
    result = linkify(text)
    assert result == "Check this out: javascript:alert(&#39;XSS&#39;)"

def test_linkify_shorten_with_protocol():
    text = "Check this out: http://example.com/this/is/a/very/long/url/that/needs/to/be/shortened"
    result = linkify(text, shorten=True)
    assert '...' in result
    assert 'title="http://example.com/this/is/a/very/long/url/that/needs/to/be/shortened"' in result

def test_linkify_shorten_without_protocol():
    text = "Check this out: www.example.com/this/is/a/very/long/url/that/needs/to/be/shortened"
    result = linkify(text, shorten=True)
    assert '...' in result
    assert 'title="http://www.example.com/this/is/a/very/long/url/that/needs/to/be/shortened"' in result
