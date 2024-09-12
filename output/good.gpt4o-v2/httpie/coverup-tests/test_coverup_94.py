# file: httpie/cli/requestitems.py:128-131
# asked: {"lines": [128, 129, 130, 131], "branches": []}
# gained: {"lines": [128, 129, 130, 131], "branches": []}

import pytest
from httpie.cli.argtypes import KeyValueArg
from httpie.cli.requestitems import process_data_embed_raw_json_file_arg
from httpie.cli.exceptions import ParseError
import json
import tempfile
import os

def test_process_data_embed_raw_json_file_arg_valid_json():
    # Create a temporary file with valid JSON content
    with tempfile.NamedTemporaryFile(delete=False, mode='w', encoding='utf-8') as temp_file:
        json_content = '{"key": "value"}'
        temp_file.write(json_content)
        temp_file_path = temp_file.name

    try:
        arg = KeyValueArg(key='test', value=temp_file_path, sep='=', orig='test')
        result = process_data_embed_raw_json_file_arg(arg)
        assert result == json.loads(json_content)
    finally:
        os.remove(temp_file_path)

def test_process_data_embed_raw_json_file_arg_invalid_json():
    # Create a temporary file with invalid JSON content
    with tempfile.NamedTemporaryFile(delete=False, mode='w', encoding='utf-8') as temp_file:
        temp_file.write('invalid json')
        temp_file_path = temp_file.name

    try:
        arg = KeyValueArg(key='test', value=temp_file_path, sep='=', orig='test')
        with pytest.raises(ParseError):
            process_data_embed_raw_json_file_arg(arg)
    finally:
        os.remove(temp_file_path)

def test_process_data_embed_raw_json_file_arg_non_utf8_file():
    # Create a temporary file with non-UTF8 content
    with tempfile.NamedTemporaryFile(delete=False, mode='wb') as temp_file:
        temp_file.write(b'\x80\x81\x82')
        temp_file_path = temp_file.name

    try:
        arg = KeyValueArg(key='test', value=temp_file_path, sep='=', orig='test')
        with pytest.raises(ParseError):
            process_data_embed_raw_json_file_arg(arg)
    finally:
        os.remove(temp_file_path)

def test_process_data_embed_raw_json_file_arg_file_not_found():
    arg = KeyValueArg(key='test', value='/non/existent/file/path', sep='=', orig='test')
    with pytest.raises(ParseError):
        process_data_embed_raw_json_file_arg(arg)
