# file sanic/headers.py:139-157
# lines [139, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 154, 155, 156, 157]
# branches ['142->143', '142->157', '143->142', '143->144', '145->146', '145->147', '147->148', '147->149', '149->150', '149->151', '151->152', '151->154']

import pytest
from sanic.headers import fwd_normalize
from urllib.parse import quote

@pytest.mark.parametrize("fwd, expected", [
    ([("by", "123.123.123.123"), ("for", "456.456.456.456"), ("host", "EXAMPLE.COM"), ("proto", "HTTP"), ("port", "8080"), ("path", "/foo bar")], 
     {"by": "123.123.123.123", "for": "456.456.456.456", "host": "example.com", "proto": "http", "port": 8080, "path": "/foo bar"}),
    ([("by", "123.123.123.123"), ("for", None), ("host", "EXAMPLE.COM"), ("proto", "HTTP"), ("port", "not_an_int"), ("path", "/foo bar"), ("unknown", "value")], 
     {"by": "123.123.123.123", "host": "example.com", "proto": "http", "path": "/foo bar", "unknown": "value"}),
])
def test_fwd_normalize(fwd, expected):
    assert fwd_normalize(fwd) == expected

@pytest.mark.parametrize("fwd, expected", [
    ([("port", "not_an_int")], {}),
    ([("path", quote("/foo bar"))], {"path": "/foo bar"}),
])
def test_fwd_normalize_exceptions(fwd, expected):
    assert fwd_normalize(fwd) == expected
