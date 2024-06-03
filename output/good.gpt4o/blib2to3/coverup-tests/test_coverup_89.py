# file src/blib2to3/pgen2/tokenize.py:305-377
# lines [330, 331, 336, 337, 361, 371]
# branches ['360->361', '370->371']

import pytest
from blib2to3.pgen2.tokenize import detect_encoding
from io import BytesIO

def test_detect_encoding_empty_input():
    def readline():
        raise StopIteration

    encoding, lines = detect_encoding(readline)
    assert encoding == "utf-8"
    assert lines == []

def test_detect_encoding_non_ascii():
    def readline():
        return b'\x80'

    encoding, lines = detect_encoding(readline)
    assert encoding == "utf-8"
    assert lines == [b'\x80']

def test_detect_encoding_blank_line():
    lines = [b'\n', b'']
    it = iter(lines)

    def readline():
        return next(it)

    encoding, lines = detect_encoding(readline)
    assert encoding == "utf-8"
    assert lines == [b'\n']

def test_detect_encoding_second_line_empty():
    lines = [b'# coding: utf-8\n', b'']
    it = iter(lines)

    def readline():
        return next(it)

    encoding, lines = detect_encoding(readline)
    assert encoding == "utf-8"
    assert lines == [b'# coding: utf-8\n']

@pytest.fixture
def mock_readline(mocker):
    return mocker.patch('blib2to3.pgen2.tokenize.detect_encoding')

def test_detect_encoding_cleanup(mock_readline):
    mock_readline.side_effect = [b'# coding: utf-8\n', b'']
    encoding, lines = detect_encoding(mock_readline)
    assert encoding == "utf-8"
    assert lines == [b'# coding: utf-8\n']
