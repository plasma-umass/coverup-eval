# file: src/blib2to3/pgen2/tokenize.py:305-377
# asked: {"lines": [323, 324, 325, 327, 328, 329, 330, 331, 333, 334, 335, 336, 337, 338, 339, 340, 341, 342, 343, 344, 346, 348, 349, 351, 352, 353, 355, 356, 357, 358, 359, 360, 361, 363, 364, 365, 366, 367, 369, 370, 371, 373, 374, 375, 377], "branches": [[339, 340], [339, 341], [348, 349], [348, 353], [349, 351], [349, 352], [356, 357], [356, 360], [360, 361], [360, 363], [364, 365], [364, 366], [366, 367], [366, 369], [370, 371], [370, 373], [374, 375], [374, 377]]}
# gained: {"lines": [323, 324, 325, 327, 328, 329, 333, 334, 335, 338, 339, 340, 341, 342, 343, 344, 346, 348, 349, 351, 352, 353, 355, 356, 357, 358, 359, 360, 363, 364, 365, 366, 367, 369, 370, 373, 374, 375, 377], "branches": [[339, 340], [339, 341], [348, 349], [348, 353], [349, 351], [349, 352], [356, 357], [356, 360], [360, 363], [364, 365], [364, 366], [366, 367], [366, 369], [370, 373], [374, 375], [374, 377]]}

import pytest
from codecs import BOM_UTF8
from unittest.mock import Mock, call
from blib2to3.pgen2.tokenize import detect_encoding

def test_detect_encoding_utf8_bom():
    readline = Mock(side_effect=[BOM_UTF8 + b'print("hello")\n', b''])
    encoding, lines = detect_encoding(readline)
    assert encoding == 'utf-8-sig'
    assert lines == [b'print("hello")\n']

def test_detect_encoding_no_bom_no_cookie():
    readline = Mock(side_effect=[b'print("hello")\n', b''])
    encoding, lines = detect_encoding(readline)
    assert encoding == 'utf-8'
    assert lines == [b'print("hello")\n']

def test_detect_encoding_with_cookie():
    readline = Mock(side_effect=[b'# -*- coding: latin-1 -*-\n', b''])
    encoding, lines = detect_encoding(readline)
    assert encoding == 'iso-8859-1'
    assert lines == [b'# -*- coding: latin-1 -*-\n']

def test_detect_encoding_bom_and_cookie_agree():
    readline = Mock(side_effect=[BOM_UTF8 + b'# -*- coding: utf-8 -*-\n', b''])
    encoding, lines = detect_encoding(readline)
    assert encoding == 'utf-8-sig'
    assert lines == [b'# -*- coding: utf-8 -*-\n']

def test_detect_encoding_bom_and_cookie_disagree():
    readline = Mock(side_effect=[BOM_UTF8 + b'# -*- coding: latin-1 -*-\n', b''])
    with pytest.raises(SyntaxError, match="encoding problem: utf-8"):
        detect_encoding(readline)

def test_detect_encoding_invalid_cookie():
    readline = Mock(side_effect=[b'# -*- coding: invalid -*-\n', b''])
    with pytest.raises(SyntaxError, match="unknown encoding: invalid"):
        detect_encoding(readline)

def test_detect_encoding_blank_line_then_cookie():
    readline = Mock(side_effect=[b'\n', b'# -*- coding: latin-1 -*-\n'])
    encoding, lines = detect_encoding(readline)
    assert encoding == 'iso-8859-1'
    assert lines == [b'\n', b'# -*- coding: latin-1 -*-\n']

def test_detect_encoding_blank_line_no_cookie():
    readline = Mock(side_effect=[b'\n', b'print("hello")\n'])
    encoding, lines = detect_encoding(readline)
    assert encoding == 'utf-8'
    assert lines == [b'\n', b'print("hello")\n']
