# file sanic/headers.py:33-52
# lines [33, 42, 43, 44, 45, 47, 48, 49, 51, 52]
# branches ['44->45', '44->47']

import pytest
from sanic.headers import parse_content_header

def test_parse_content_header():
    # Test case 1: Simple content type without options
    value, options = parse_content_header("text/html")
    assert value == "text/html"
    assert options == {}

    # Test case 2: Content type with options
    value, options = parse_content_header('form-data; name=upload; filename="file.txt"')
    assert value == "form-data"
    assert options == {"name": "upload", "filename": "file.txt"}

    # Test case 3: Content type with special characters
    value, options = parse_content_header('form-data; name=upload; filename="file%22.txt"')
    assert value == "form-data"
    assert options == {"name": "upload", "filename": 'file".txt'}

    # Test case 4: Content type with no semicolon
    value, options = parse_content_header("application/json")
    assert value == "application/json"
    assert options == {}

    # Test case 5: Content type with escaped quotes
    value, options = parse_content_header('form-data; name="upload"; filename="file.txt"')
    assert value == "form-data"
    assert options == {"name": "upload", "filename": "file.txt"}

    # Test case 6: Content type with multiple semicolons
    value, options = parse_content_header('form-data; name=upload; filename="file.txt"; type="text"')
    assert value == "form-data"
    assert options == {"name": "upload", "filename": "file.txt", "type": "text"}
