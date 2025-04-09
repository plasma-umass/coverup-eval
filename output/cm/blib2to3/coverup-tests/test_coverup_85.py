# file src/blib2to3/pgen2/tokenize.py:305-377
# lines [336, 337, 352, 377]
# branches ['349->352', '374->377']

import pytest
from blib2to3.pgen2.tokenize import detect_encoding
from blib2to3.pgen2.tokenize import cookie_re, BOM_UTF8
from io import BytesIO

def test_detect_encoding():
    # Test for UnicodeDecodeError, which should return None (lines 336-337)
    def mock_readline_unicode_error():
        non_ascii_bytes = b'\x80abc'
        yield non_ascii_bytes
        while True:
            yield b''
    mock_file_unicode_error = mock_readline_unicode_error()
    readline_unicode_error = lambda: next(mock_file_unicode_error)
    encoding, lines = detect_encoding(readline_unicode_error)
    assert encoding == 'utf-8'
    assert lines == [b'\x80abc']

    # Test for bom_found but codec.name != "utf-8" (lines 349-352)
    def mock_readline_bom_not_utf8():
        yield BOM_UTF8 + b'# coding: latin-1\n'
        yield b'print("Hello, world!")\n'
    mock_file_bom_not_utf8 = mock_readline_bom_not_utf8()
    readline_bom_not_utf8 = lambda: next(mock_file_bom_not_utf8)
    with pytest.raises(SyntaxError, match="encoding problem: utf-8"):
        detect_encoding(readline_bom_not_utf8)

    # Test for no bom, no cookie, no blank line (line 377)
    def mock_readline_no_bom_no_cookie():
        yield b'print("Hello, world!")\n'
        while True:
            yield b''
    mock_file_no_bom_no_cookie = mock_readline_no_bom_no_cookie()
    readline_no_bom_no_cookie = lambda: next(mock_file_no_bom_no_cookie)
    encoding, lines = detect_encoding(readline_no_bom_no_cookie)
    assert encoding == 'utf-8'
    assert lines == [b'print("Hello, world!")\n']

# Run the test function
test_detect_encoding()
