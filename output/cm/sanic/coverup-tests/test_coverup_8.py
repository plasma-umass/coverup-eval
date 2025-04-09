# file sanic/headers.py:33-52
# lines [33, 42, 43, 44, 45, 47, 48, 49, 51, 52]
# branches ['44->45', '44->47']

import pytest
from sanic.headers import parse_content_header

@pytest.mark.parametrize("header_value,expected_result", [
    (
        'form-data; name=upload; filename="file.txt"',
        ('form-data', {'name': 'upload', 'filename': 'file.txt'})
    ),
    (
        'text/plain; charset=us-ascii',
        ('text/plain', {'charset': 'us-ascii'})
    ),
    (
        'text/html',
        ('text/html', {})
    ),
    (
        'form-data; name=upload; filename="file.txt"; size=123',
        ('form-data', {'name': 'upload', 'filename': 'file.txt', 'size': '123'})
    ),
    (
        'form-data; name=upload; filename="file.txt"; size="123"',
        ('form-data', {'name': 'upload', 'filename': 'file.txt', 'size': '123'})
    ),
    (
        'form-data; name=upload; filename="file.txt"; size="123"; extra="value with spaces"',
        ('form-data', {'name': 'upload', 'filename': 'file.txt', 'size': '123', 'extra': 'value with spaces'})
    ),
    (
        'form-data; name=upload; filename="file.txt"; size="123"; extra="value with %22escaped quotes%22"',
        ('form-data', {'name': 'upload', 'filename': 'file.txt', 'size': '123', 'extra': 'value with "escaped quotes"'})
    ),
])
def test_parse_content_header(header_value, expected_result):
    result = parse_content_header(header_value)
    assert result == expected_result
