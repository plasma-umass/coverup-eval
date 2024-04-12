# file tornado/escape.py:275-377
# lines [275, 277, 278, 279, 280, 311, 312, 314, 315, 316, 317, 318, 320, 321, 323, 324, 325, 327, 328, 330, 333, 334, 335, 336, 337, 339, 341, 342, 347, 348, 349, 350, 351, 354, 355, 357, 358, 360, 361, 362, 364, 365, 369, 371, 376, 377]
# branches ['311->312', '311->314', '317->318', '317->320', '320->321', '320->323', '324->325', '324->327', '327->328', '327->330', '334->335', '334->371', '336->337', '336->339', '342->347', '342->354', '354->355', '354->357', '357->358', '357->371', '360->361', '360->362', '364->365', '364->369']

import pytest
from tornado.escape import linkify, xhtml_escape

def test_linkify_with_callable_extra_params_and_require_protocol():
    def extra_params_cb(url):
        if url.startswith("http://example.com"):
            return 'class="internal"'
        else:
            return 'class="external" rel="nofollow"'

    # Test with require_protocol=True and a callable extra_params
    result = linkify("Check out example.com and http://example.com",
                     extra_params=extra_params_cb,
                     require_protocol=True)
    assert 'class="internal"' in result
    assert 'Check out example.com' in result
    assert '<a href="http://example.com" class="internal">http://example.com</a>' in result

    # Test with require_protocol=False and a callable extra_params
    result = linkify("Check out example.com and http://example.com",
                     extra_params=extra_params_cb,
                     require_protocol=False)
    assert 'class="internal"' in result
    assert '<a href="http://example.com" class="internal">http://example.com</a>' in result
    assert '<a href="http://example.com" class="external" rel="nofollow">example.com</a>' not in result

def test_linkify_with_permitted_protocols():
    # Test with a non-permitted protocol
    result = linkify("Check out javascript:alert('Hello World');",
                     permitted_protocols=["http", "https"])
    assert 'href="' not in result
    assert xhtml_escape("javascript:alert('Hello World');") in result

    # Test with a permitted protocol
    result = linkify("Visit http://example.com",
                     permitted_protocols=["http", "https"])
    assert '<a href="http://example.com"' in result
    assert "http://example.com" in result
