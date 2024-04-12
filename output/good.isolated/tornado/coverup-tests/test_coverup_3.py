# file tornado/httpclient.py:358-549
# lines [358, 361, 362, 363, 364, 365, 366, 367, 368, 369, 370, 371, 372, 373, 374, 375, 376, 377, 378, 379, 380, 381, 382, 383, 384, 385, 386, 387, 388, 391, 392, 393, 394, 511, 512, 513, 514, 516, 517, 518, 519, 520, 521, 522, 523, 524, 525, 526, 527, 528, 529, 530, 531, 532, 533, 534, 536, 537, 538, 539, 540, 541, 542, 543, 544, 545, 546, 547, 548, 549]
# branches ['512->513', '512->516', '533->534', '533->536']

import datetime
import pytest
from tornado import httputil
from tornado.httpclient import HTTPRequest

@pytest.fixture
def cleanup():
    # Fixture to perform cleanup after tests
    yield
    # No cleanup actions needed for this test case

@pytest.mark.usefixtures("cleanup")
def test_httprequest_if_modified_since():
    # Test the if_modified_since branch of HTTPRequest
    timestamp = datetime.datetime(2021, 1, 1)
    request = HTTPRequest(
        url="http://example.com",
        if_modified_since=timestamp
    )
    assert request.headers["If-Modified-Since"] == httputil.format_timestamp(timestamp)

@pytest.mark.usefixtures("cleanup")
def test_httprequest_decompress_response():
    # Test the decompress_response branch of HTTPRequest
    request = HTTPRequest(
        url="http://example.com",
        decompress_response=True
    )
    assert request.decompress_response is True

    request = HTTPRequest(
        url="http://example.com",
        use_gzip=True
    )
    assert request.decompress_response is True

    request = HTTPRequest(
        url="http://example.com",
        decompress_response=False
    )
    assert request.decompress_response is False

    request = HTTPRequest(
        url="http://example.com",
        use_gzip=False
    )
    assert request.decompress_response is False

    request = HTTPRequest(
        url="http://example.com",
        decompress_response=None,
        use_gzip=None
    )
    assert request.decompress_response is None
