# file sanic/headers.py:33-52
# lines [33, 42, 43, 44, 45, 47, 48, 49, 51, 52]
# branches ['44->45', '44->47']

import pytest
from sanic.headers import parse_content_header

def test_parse_content_header():
    # Test case with no semicolon
    value, options = parse_content_header("text/plain")
    assert value == "text/plain"
    assert options == {}

    # Test case with semicolon and parameters
    value, options = parse_content_header('form-data; name=upload; filename="file.txt"')
    assert value == "form-data"
    assert options == {"name": "upload", "filename": "file.txt"}

    # Test case with special characters
    value, options = parse_content_header('form-data; name=upload; filename="file%22.txt"')
    assert value == "form-data"
    assert options == {"name": "upload", "filename": 'file".txt'}

    # Test case with no parameters after semicolon
    value, options = parse_content_header('form-data;')
    assert value == "form-data"
    assert options == {}

    # Test case with mixed case parameter names
    value, options = parse_content_header('form-data; Name=upload; FILENAME="file.txt"')
    assert value == "form-data"
    assert options == {"name": "upload", "filename": "file.txt"}

    # Test case with multiple semicolons
    value, options = parse_content_header('form-data; name=upload; filename="file.txt"; extra=param')
    assert value == "form-data"
    assert options == {"name": "upload", "filename": "file.txt", "extra": "param"}
