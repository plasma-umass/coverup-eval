# file httpie/core.py:112-125
# lines [112, 116, 117, 118, 119, 121, 122, 123, 125]
# branches []

import argparse
import pytest
import requests
from httpie.core import get_output_options

OUT_REQ_HEAD = 'H'
OUT_REQ_BODY = 'B'
OUT_RESP_HEAD = 'h'
OUT_RESP_BODY = 'b'

@pytest.fixture
def args(request):
    parser = argparse.ArgumentParser()
    parser.add_argument('--output-options', default='', type=str)
    namespace = parser.parse_args(request.param)
    return namespace

@pytest.mark.parametrize('args, message, expected', [
    (['--output-options=HB'], requests.PreparedRequest(), (True, True)),
    (['--output-options='], requests.PreparedRequest(), (False, False)),
    (['--output-options=hb'], requests.Response(), (True, True)),
    (['--output-options='], requests.Response(), (False, False)),
], indirect=['args'])
def test_get_output_options(args, message, expected, mocker):
    mocker.patch('httpie.core.OUT_REQ_HEAD', new=OUT_REQ_HEAD)
    mocker.patch('httpie.core.OUT_REQ_BODY', new=OUT_REQ_BODY)
    mocker.patch('httpie.core.OUT_RESP_HEAD', new=OUT_RESP_HEAD)
    mocker.patch('httpie.core.OUT_RESP_BODY', new=OUT_RESP_BODY)
    
    output_options = get_output_options(args, message)
    assert output_options == expected
