# file: src/blib2to3/pgen2/tokenize.py:305-377
# asked: {"lines": [305, 323, 324, 325, 327, 328, 329, 330, 331, 333, 334, 335, 336, 337, 338, 339, 340, 341, 342, 343, 344, 346, 348, 349, 351, 352, 353, 355, 356, 357, 358, 359, 360, 361, 363, 364, 365, 366, 367, 369, 370, 371, 373, 374, 375, 377], "branches": [[339, 340], [339, 341], [348, 349], [348, 353], [349, 351], [349, 352], [356, 357], [356, 360], [360, 361], [360, 363], [364, 365], [364, 366], [366, 367], [366, 369], [370, 371], [370, 373], [374, 375], [374, 377]]}
# gained: {"lines": [305, 323, 324, 325, 327, 328, 329, 333, 334, 335, 338, 339, 340, 341, 342, 343, 344, 346, 348, 349, 351, 353, 355, 356, 357, 358, 359, 360, 363, 364, 365, 366, 367, 369, 370, 373, 374, 377], "branches": [[339, 340], [339, 341], [348, 349], [348, 353], [349, 351], [356, 357], [356, 360], [360, 363], [364, 365], [364, 366], [366, 367], [366, 369], [370, 373], [374, 377]]}

import pytest
from codecs import BOM_UTF8
from blib2to3.pgen2.tokenize import detect_encoding

def test_detect_encoding_utf8_bom():
    def readline():
        yield BOM_UTF8 + b'print("Hello World")\n'
        yield b''

    lines = readline()
    encoding, read_lines = detect_encoding(lambda: next(lines))
    assert encoding == 'utf-8-sig'
    assert read_lines == [b'print("Hello World")\n']

def test_detect_encoding_no_bom_no_cookie():
    def readline():
        yield b'print("Hello World")\n'
        yield b''

    lines = readline()
    encoding, read_lines = detect_encoding(lambda: next(lines))
    assert encoding == 'utf-8'
    assert read_lines == [b'print("Hello World")\n']

def test_detect_encoding_with_cookie():
    def readline():
        yield b'# -*- coding: latin-1 -*-\n'
        yield b'print("Hello World")\n'

    lines = readline()
    encoding, read_lines = detect_encoding(lambda: next(lines))
    assert encoding == 'iso-8859-1'
    assert read_lines == [b'# -*- coding: latin-1 -*-\n']

def test_detect_encoding_with_invalid_cookie():
    def readline():
        yield b'# -*- coding: unknown -*-\n'
        yield b'print("Hello World")\n'

    lines = readline()
    with pytest.raises(SyntaxError, match="unknown encoding: unknown"):
        detect_encoding(lambda: next(lines))

def test_detect_encoding_with_bom_and_cookie():
    def readline():
        yield BOM_UTF8 + b'# -*- coding: latin-1 -*-\n'
        yield b'print("Hello World")\n'

    lines = readline()
    with pytest.raises(SyntaxError, match="encoding problem: utf-8"):
        detect_encoding(lambda: next(lines))

def test_detect_encoding_blank_line():
    def readline():
        yield b'\n'
        yield b'print("Hello World")\n'

    lines = readline()
    encoding, read_lines = detect_encoding(lambda: next(lines))
    assert encoding == 'utf-8'
    assert read_lines == [b'\n', b'print("Hello World")\n']
