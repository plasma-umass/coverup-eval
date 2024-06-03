# file flutils/codecs/raw_utf8_escape.py:147-155
# lines [147, 148, 149, 150, 151, 152, 154, 155]
# branches ['148->149', '148->155']

import pytest
import codecs
from typing import Optional
from flutils.codecs.raw_utf8_escape import _get_codec_info

NAME = "raw_utf8_escape"

def encode(input, errors='strict'):
    return input.encode('utf-8'), len(input)

def decode(input, errors='strict'):
    return input.decode('utf-8'), len(input)

def test_get_codec_info(mocker):
    # Mock the encode and decode functions to match the ones used in the module
    mocker.patch('flutils.codecs.raw_utf8_escape.encode', encode)
    mocker.patch('flutils.codecs.raw_utf8_escape.decode', decode)

    # Test when name matches
    codec_info = _get_codec_info(NAME)
    assert codec_info is not None
    assert codec_info.name == NAME
    assert codec_info.encode == encode
    assert codec_info.decode == decode

    # Test when name does not match
    codec_info = _get_codec_info("other_name")
    assert codec_info is None
