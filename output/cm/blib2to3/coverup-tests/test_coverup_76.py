# file src/blib2to3/pgen2/tokenize.py:305-377
# lines [305, 323, 324, 325, 327, 328, 329, 330, 331, 333, 334, 335, 336, 337, 338, 339, 340, 341, 342, 343, 344, 346, 348, 349, 351, 352, 353, 355, 356, 357, 358, 359, 360, 361, 363, 364, 365, 366, 367, 369, 370, 371, 373, 374, 375, 377]
# branches ['339->340', '339->341', '348->349', '348->353', '349->351', '349->352', '356->357', '356->360', '360->361', '360->363', '364->365', '364->366', '366->367', '366->369', '370->371', '370->373', '374->375', '374->377']

import pytest
from blib2to3.pgen2.tokenize import detect_encoding, BOM_UTF8, cookie_re, blank_re
from typing import Callable, Tuple, List, Optional
from codecs import lookup, CodecInfo
import re

@pytest.fixture
def mock_readline(mocker):
    def _mock_readline(lines):
        return mocker.MagicMock(side_effect=lines + [StopIteration()])
    return _mock_readline

def test_detect_encoding_with_bom_and_cookie_disagree(mock_readline):
    # Mock readline to simulate file with BOM and different encoding cookie
    lines = [
        BOM_UTF8 + b'# coding: latin-1\n',
        b'print("Hello, world!")\n'
    ]
    readline = mock_readline(lines)

    # Test that a SyntaxError is raised when BOM and cookie disagree
    with pytest.raises(SyntaxError, match="encoding problem: utf-8"):
        detect_encoding(readline)

def test_detect_encoding_with_invalid_cookie(mock_readline):
    # Mock readline to simulate file with invalid encoding cookie
    lines = [
        b'# coding: invalid-encoding\n',
        b'print("Hello, world!")\n'
    ]
    readline = mock_readline(lines)

    # Test that a SyntaxError is raised for an invalid charset
    with pytest.raises(SyntaxError, match="unknown encoding: invalid-encoding"):
        detect_encoding(readline)

def test_detect_encoding_with_only_cookie(mock_readline):
    # Mock readline to simulate file with only a valid encoding cookie
    lines = [
        b'# coding: latin-1\n',
        b'print("Hello, world!")\n'
    ]
    readline = mock_readline(lines)

    # Test that the correct encoding is detected from the cookie
    encoding, read_lines = detect_encoding(readline)
    assert encoding == 'iso-8859-1'
    assert read_lines == [lines[0]]

def test_detect_encoding_with_no_cookie_and_non_blank_line(mock_readline):
    # Mock readline to simulate file with no encoding cookie and a non-blank first line
    lines = [
        b'print("Hello, world!")\n',
        b'# coding: latin-1\n'
    ]
    readline = mock_readline(lines)

    # Test that the default encoding is returned and only the first line is read
    encoding, read_lines = detect_encoding(readline)
    assert encoding == 'utf-8'
    assert read_lines == [lines[0]]

def test_detect_encoding_with_blank_first_line_and_cookie_in_second_line(mock_readline):
    # Mock readline to simulate file with a blank first line and a valid encoding cookie in the second line
    lines = [
        b'\n',
        b'# coding: latin-1\n'
    ]
    readline = mock_readline(lines)

    # Test that the correct encoding is detected from the second line
    encoding, read_lines = detect_encoding(readline)
    assert encoding == 'iso-8859-1'
    assert read_lines == lines

def test_detect_encoding_with_blank_first_line_and_no_second_line(mock_readline):
    # Mock readline to simulate file with a blank first line and no second line
    lines = [
        b'\n'
    ]
    readline = mock_readline(lines)

    # Test that the default encoding is returned and only the first line is read
    encoding, read_lines = detect_encoding(readline)
    assert encoding == 'utf-8'
    assert read_lines == lines

def test_detect_encoding_with_no_lines(mock_readline):
    # Mock readline to simulate an empty file
    readline = mock_readline([])

    # Test that the default encoding is returned and no lines are read
    encoding, read_lines = detect_encoding(readline)
    assert encoding == 'utf-8'
    assert read_lines == []
