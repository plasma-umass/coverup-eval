# file: httpie/cli/requestitems.py:31-81
# asked: {"lines": [37, 38, 39, 40, 41, 43, 44, 45, 47, 48, 49, 51, 52, 53, 55, 56, 57, 59, 60, 61, 63, 64, 65, 67, 68, 69, 73, 74, 75, 76, 78, 79, 81], "branches": [[73, 74], [73, 81], [78, 73], [78, 79]]}
# gained: {"lines": [37, 38, 39, 40, 41, 43, 44, 45, 47, 48, 49, 51, 52, 53, 55, 56, 57, 59, 60, 61, 63, 64, 65, 67, 68, 69, 73, 74, 75, 76, 78, 79, 81], "branches": [[73, 74], [73, 81], [78, 73], [78, 79]]}

import pytest
from httpie.cli.requestitems import RequestItems
from httpie.cli.argtypes import KeyValueArg
from httpie.cli.constants import (
    SEPARATOR_HEADER,
    SEPARATOR_HEADER_EMPTY,
    SEPARATOR_QUERY_PARAM,
    SEPARATOR_FILE_UPLOAD,
    SEPARATOR_DATA_STRING,
    SEPARATOR_DATA_EMBED_FILE_CONTENTS,
    SEPARATOR_DATA_RAW_JSON,
    SEPARATOR_DATA_EMBED_RAW_JSON_FILE,
    SEPARATORS_GROUP_MULTIPART,
)

def process_header_arg(arg):
    return arg.value

def process_empty_header_arg(arg):
    return None

def process_query_param_arg(arg):
    return arg.value

def process_file_upload_arg(arg):
    return arg.value

def process_data_item_arg(arg):
    return arg.value

def process_data_embed_file_contents_arg(arg):
    return arg.value

def process_data_raw_json_embed_arg(arg):
    return arg.value

def process_data_embed_raw_json_file_arg(arg):
    return arg.value

@pytest.fixture
def mock_processors(monkeypatch):
    monkeypatch.setattr('httpie.cli.requestitems.process_header_arg', process_header_arg)
    monkeypatch.setattr('httpie.cli.requestitems.process_empty_header_arg', process_empty_header_arg)
    monkeypatch.setattr('httpie.cli.requestitems.process_query_param_arg', process_query_param_arg)
    monkeypatch.setattr('httpie.cli.requestitems.process_file_upload_arg', process_file_upload_arg)
    monkeypatch.setattr('httpie.cli.requestitems.process_data_item_arg', process_data_item_arg)
    monkeypatch.setattr('httpie.cli.requestitems.process_data_embed_file_contents_arg', process_data_embed_file_contents_arg)
    monkeypatch.setattr('httpie.cli.requestitems.process_data_raw_json_embed_arg', process_data_raw_json_embed_arg)
    monkeypatch.setattr('httpie.cli.requestitems.process_data_embed_raw_json_file_arg', process_data_embed_raw_json_file_arg)

def test_request_items_from_args(mock_processors):
    args = [
        KeyValueArg(key='Content-Type', value='application/json', sep=SEPARATOR_HEADER, orig='Content-Type:application/json'),
        KeyValueArg(key='X-Empty-Header', value='', sep=SEPARATOR_HEADER_EMPTY, orig='X-Empty-Header:'),
        KeyValueArg(key='param', value='value', sep=SEPARATOR_QUERY_PARAM, orig='param=value'),
        KeyValueArg(key='file', value='file.txt', sep=SEPARATOR_FILE_UPLOAD, orig='file@file.txt'),
        KeyValueArg(key='data', value='value', sep=SEPARATOR_DATA_STRING, orig='data=value'),
        KeyValueArg(key='embed', value='file.txt', sep=SEPARATOR_DATA_EMBED_FILE_CONTENTS, orig='embed@file.txt'),
        KeyValueArg(key='json', value='{"key": "value"}', sep=SEPARATOR_DATA_RAW_JSON, orig='json:{"key": "value"}'),
        KeyValueArg(key='jsonfile', value='file.json', sep=SEPARATOR_DATA_EMBED_RAW_JSON_FILE, orig='jsonfile@file.json'),
    ]

    instance = RequestItems.from_args(args)

    assert instance.headers['Content-Type'] == 'application/json'
    assert instance.headers['X-Empty-Header'] is None
    assert instance.params['param'] == 'value'
    assert instance.files['file'] == 'file.txt'
    assert instance.data['data'] == 'value'
    assert instance.data['embed'] == 'file.txt'
    assert instance.data['json'] == '{"key": "value"}'
    assert instance.data['jsonfile'] == 'file.json'

    for arg in args:
        if arg.sep in SEPARATORS_GROUP_MULTIPART:
            assert instance.multipart_data[arg.key] == arg.value
