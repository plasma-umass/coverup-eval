# file tornado/escape.py:275-377
# lines [311, 312, 314, 315, 316, 317, 318, 320, 321, 323, 324, 325, 327, 328, 330, 333, 334, 335, 336, 337, 339, 341, 342, 347, 348, 349, 350, 351, 354, 355, 357, 358, 360, 361, 362, 364, 365, 369, 371, 376, 377]
# branches ['311->312', '311->314', '317->318', '317->320', '320->321', '320->323', '324->325', '324->327', '327->328', '327->330', '334->335', '334->371', '336->337', '336->339', '342->347', '342->354', '354->355', '354->357', '357->358', '357->371', '360->361', '360->362', '364->365', '364->369']

import pytest
from tornado.escape import linkify

def test_linkify():
    # Test with extra_params as a string
    text = "Check this link: http://example.com"
    result = linkify(text, extra_params='rel="nofollow"')
    assert result == 'Check this link: <a href="http://example.com" rel="nofollow">http://example.com</a>'

    # Test with extra_params as a callable
    def extra_params_cb(url):
        if url.startswith("http://example.com"):
            return 'class="internal"'
        else:
            return 'class="external" rel="nofollow"'
    
    result = linkify(text, extra_params=extra_params_cb)
    assert result == 'Check this link: <a href="http://example.com" class="internal">http://example.com</a>'

    # Test with require_protocol=True
    text = "Visit www.example.com"
    result = linkify(text, require_protocol=True)
    assert result == 'Visit www.example.com'

    # Test with permitted_protocols
    text = "Check this link: ftp://example.com"
    result = linkify(text, permitted_protocols=["http", "https"])
    assert result == 'Check this link: ftp://example.com'

    # Test with shorten=True
    text = "Check this very long link: http://example.com/this/is/a/very/long/url/that/needs/to/be/shortened"
    result = linkify(text, shorten=True)
    assert result.startswith('Check this very long link: <a href="http://example.com/this/is/a/very/long/url/that/needs/to/be/shortened"')
    assert 'title="http://example.com/this/is/a/very/long/url/that/needs/to/be/shortened"' in result
    assert 'http://example.com/this/is/a/very/long/url/that/needs/to/be/shortened' in result
