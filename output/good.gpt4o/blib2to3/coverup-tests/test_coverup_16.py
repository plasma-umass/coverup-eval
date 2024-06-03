# file src/blib2to3/pgen2/tokenize.py:305-377
# lines [305, 323, 324, 325, 327, 328, 329, 330, 331, 333, 334, 335, 336, 337, 338, 339, 340, 341, 342, 343, 344, 346, 348, 349, 351, 352, 353, 355, 356, 357, 358, 359, 360, 361, 363, 364, 365, 366, 367, 369, 370, 371, 373, 374, 375, 377]
# branches ['339->340', '339->341', '348->349', '348->353', '349->351', '349->352', '356->357', '356->360', '360->361', '360->363', '364->365', '364->366', '366->367', '366->369', '370->371', '370->373', '374->375', '374->377']

import pytest
from blib2to3.pgen2.tokenize import detect_encoding
from io import BytesIO

def test_detect_encoding_utf8_bom():
    def readline():
        lines = [
            b'\xef\xbb\xbf# coding: utf-8\n',
            b'print("Hello, world!")\n'
        ]
        for line in lines:
            yield line
    readline_gen = readline()
    result = detect_encoding(lambda: next(readline_gen))
    assert result == ('utf-8-sig', [b'# coding: utf-8\n'])

def test_detect_encoding_invalid_cookie():
    def readline():
        lines = [
            b'# coding: invalid-encoding\n',
            b'print("Hello, world!")\n'
        ]
        for line in lines:
            yield line
    readline_gen = readline()
    with pytest.raises(SyntaxError, match="unknown encoding: invalid-encoding"):
        detect_encoding(lambda: next(readline_gen))

def test_detect_encoding_conflicting_bom_and_cookie():
    def readline():
        lines = [
            b'\xef\xbb\xbf# coding: latin-1\n',
            b'print("Hello, world!")\n'
        ]
        for line in lines:
            yield line
    readline_gen = readline()
    with pytest.raises(SyntaxError, match="encoding problem: utf-8"):
        detect_encoding(lambda: next(readline_gen))

def test_detect_encoding_no_cookie():
    def readline():
        lines = [
            b'print("Hello, world!")\n'
        ]
        for line in lines:
            yield line
    readline_gen = readline()
    result = detect_encoding(lambda: next(readline_gen))
    assert result == ('utf-8', [b'print("Hello, world!")\n'])

def test_detect_encoding_blank_line():
    def readline():
        lines = [
            b'\n',
            b'# coding: utf-8\n',
            b'print("Hello, world!")\n'
        ]
        for line in lines:
            yield line
    readline_gen = readline()
    result = detect_encoding(lambda: next(readline_gen))
    assert result == ('utf-8', [b'\n', b'# coding: utf-8\n'])

def test_detect_encoding_blank_line_no_cookie():
    def readline():
        lines = [
            b'\n',
            b'print("Hello, world!")\n'
        ]
        for line in lines:
            yield line
    readline_gen = readline()
    result = detect_encoding(lambda: next(readline_gen))
    assert result == ('utf-8', [b'\n', b'print("Hello, world!")\n'])
