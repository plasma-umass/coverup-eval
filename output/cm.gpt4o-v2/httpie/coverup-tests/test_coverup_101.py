# file: httpie/cli/requestitems.py:31-81
# asked: {"lines": [37, 38, 39, 40, 41, 43, 44, 45, 47, 48, 49, 51, 52, 53, 55, 56, 57, 59, 60, 61, 63, 64, 65, 67, 68, 69, 73, 74, 75, 76, 78, 79, 81], "branches": [[73, 74], [73, 81], [78, 73], [78, 79]]}
# gained: {"lines": [37, 38, 39, 40, 41, 43, 44, 45, 47, 48, 49, 51, 52, 53, 55, 56, 57, 59, 60, 61, 63, 64, 65, 67, 68, 69, 73, 74, 75, 76, 78, 79, 81], "branches": [[73, 74], [73, 81], [78, 73], [78, 79]]}

import pytest
from httpie.cli.requestitems import RequestItems
from httpie.cli.argtypes import KeyValueArg
from httpie.cli.constants import (
    SEPARATOR_HEADER, SEPARATOR_HEADER_EMPTY, SEPARATOR_QUERY_PARAM,
    SEPARATOR_FILE_UPLOAD, SEPARATOR_DATA_STRING, SEPARATOR_DATA_EMBED_FILE_CONTENTS,
    SEPARATOR_DATA_RAW_JSON, SEPARATOR_DATA_EMBED_RAW_JSON_FILE, SEPARATORS_GROUP_MULTIPART
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
        KeyValueArg(key='Header1', value='value1', sep=SEPARATOR_HEADER, orig='Header1:value1'),
        KeyValueArg(key='Header2', value=None, sep=SEPARATOR_HEADER_EMPTY, orig='Header2;'),
        KeyValueArg(key='param1', value='value1', sep=SEPARATOR_QUERY_PARAM, orig='param1==value1'),
        KeyValueArg(key='file1', value='@file.txt', sep=SEPARATOR_FILE_UPLOAD, orig='file1@file.txt'),
        KeyValueArg(key='data1', value='value1', sep=SEPARATOR_DATA_STRING, orig='data1=value1'),
        KeyValueArg(key='data2', value='@file.txt', sep=SEPARATOR_DATA_EMBED_FILE_CONTENTS, orig='data2=@file.txt'),
        KeyValueArg(key='data3', value='value3', sep=SEPARATOR_DATA_RAW_JSON, orig='data3:=value3'),
        KeyValueArg(key='data4', value='@file.json', sep=SEPARATOR_DATA_EMBED_RAW_JSON_FILE, orig='data4=@file.json')
    ]

    request_items = RequestItems.from_args(args)

    assert request_items.headers['Header1'] == 'value1'
    assert request_items.headers['Header2'] is None
    assert request_items.params['param1'] == 'value1'
    assert request_items.files['file1'] == '@file.txt'
    assert request_items.data['data1'] == 'value1'
    assert request_items.data['data2'] == '@file.txt'
    assert request_items.data['data3'] == 'value3'
    assert request_items.data['data4'] == '@file.json'

    for arg in args:
        if arg.sep in SEPARATORS_GROUP_MULTIPART:
            assert request_items.multipart_data[arg.key] == arg.value
