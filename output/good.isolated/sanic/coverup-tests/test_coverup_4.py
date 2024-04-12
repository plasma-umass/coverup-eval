# file sanic/response.py:459-496
# lines [459, 461, 462, 463, 464, 485, 486, 487, 491, 492, 493, 494, 495]
# branches ['485->486', '485->491']

import pytest
from sanic.response import stream, StreamingHTTPResponse
from unittest.mock import Mock
from warnings import catch_warnings, simplefilter

@pytest.mark.asyncio
async def test_stream_deprecated_chunked_argument():
    async def sample_streaming_fn(response):
        await response.write('foo')
        await response.write('bar')

    with catch_warnings(record=True) as w:
        simplefilter("always")
        response = stream(sample_streaming_fn, chunked=True)
        assert len(w) == 1
        assert issubclass(w[-1].category, DeprecationWarning)
        assert "The chunked argument has been deprecated" in str(w[-1].message)

    assert isinstance(response, StreamingHTTPResponse)
    assert response.status == 200
    assert response.content_type == "text/plain; charset=utf-8"
