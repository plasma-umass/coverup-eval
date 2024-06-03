# file httpie/cli/requestitems.py:31-81
# lines [31, 32, 35, 37, 38, 39, 40, 41, 43, 44, 45, 47, 48, 49, 51, 52, 53, 55, 56, 57, 59, 60, 61, 63, 64, 65, 67, 68, 69, 73, 74, 75, 76, 78, 79, 81]
# branches ['73->74', '73->81', '78->73', '78->79']

import pytest
from unittest.mock import Mock
from httpie.cli.requestitems import RequestItems
from httpie.cli.argtypes import KeyValueArg

# Mocking the functions and constants used in the RequestItems class
process_header_arg = Mock(return_value='header_value')
process_empty_header_arg = Mock(return_value='empty_header_value')
process_query_param_arg = Mock(return_value='query_param_value')
process_file_upload_arg = Mock(return_value='file_upload_value')
process_data_item_arg = Mock(return_value='data_item_value')
process_data_embed_file_contents_arg = Mock(return_value='data_embed_file_contents_value')
process_data_raw_json_embed_arg = Mock(return_value='data_raw_json_embed_value')
process_data_embed_raw_json_file_arg = Mock(return_value='data_embed_raw_json_file_value')

SEPARATOR_HEADER = ':'
SEPARATOR_HEADER_EMPTY = ';'
SEPARATOR_QUERY_PARAM = '=='
SEPARATOR_FILE_UPLOAD = '@'
SEPARATOR_DATA_STRING = '='
SEPARATOR_DATA_EMBED_FILE_CONTENTS = '=@'
SEPARATOR_DATA_RAW_JSON = ':='
SEPARATOR_DATA_EMBED_RAW_JSON_FILE = ':=@'
SEPARATORS_GROUP_MULTIPART = {SEPARATOR_FILE_UPLOAD, SEPARATOR_DATA_EMBED_FILE_CONTENTS}

@pytest.fixture
def mock_request_items(mocker):
    mocker.patch('httpie.cli.requestitems.process_header_arg', process_header_arg)
    mocker.patch('httpie.cli.requestitems.process_empty_header_arg', process_empty_header_arg)
    mocker.patch('httpie.cli.requestitems.process_query_param_arg', process_query_param_arg)
    mocker.patch('httpie.cli.requestitems.process_file_upload_arg', process_file_upload_arg)
    mocker.patch('httpie.cli.requestitems.process_data_item_arg', process_data_item_arg)
    mocker.patch('httpie.cli.requestitems.process_data_embed_file_contents_arg', process_data_embed_file_contents_arg)
    mocker.patch('httpie.cli.requestitems.process_data_raw_json_embed_arg', process_data_raw_json_embed_arg)
    mocker.patch('httpie.cli.requestitems.process_data_embed_raw_json_file_arg', process_data_embed_raw_json_file_arg)
    mocker.patch('httpie.cli.requestitems.SEPARATOR_HEADER', SEPARATOR_HEADER)
    mocker.patch('httpie.cli.requestitems.SEPARATOR_HEADER_EMPTY', SEPARATOR_HEADER_EMPTY)
    mocker.patch('httpie.cli.requestitems.SEPARATOR_QUERY_PARAM', SEPARATOR_QUERY_PARAM)
    mocker.patch('httpie.cli.requestitems.SEPARATOR_FILE_UPLOAD', SEPARATOR_FILE_UPLOAD)
    mocker.patch('httpie.cli.requestitems.SEPARATOR_DATA_STRING', SEPARATOR_DATA_STRING)
    mocker.patch('httpie.cli.requestitems.SEPARATOR_DATA_EMBED_FILE_CONTENTS', SEPARATOR_DATA_EMBED_FILE_CONTENTS)
    mocker.patch('httpie.cli.requestitems.SEPARATOR_DATA_RAW_JSON', SEPARATOR_DATA_RAW_JSON)
    mocker.patch('httpie.cli.requestitems.SEPARATOR_DATA_EMBED_RAW_JSON_FILE', SEPARATOR_DATA_EMBED_RAW_JSON_FILE)
    mocker.patch('httpie.cli.requestitems.SEPARATORS_GROUP_MULTIPART', SEPARATORS_GROUP_MULTIPART)

def test_request_items_from_args(mock_request_items):
    request_item_args = [
        KeyValueArg(key='header_key', value='header_value', sep=SEPARATOR_HEADER, orig='header_key:header_value'),
        KeyValueArg(key='empty_header_key', value='empty_header_value', sep=SEPARATOR_HEADER_EMPTY, orig='empty_header_key;empty_header_value'),
        KeyValueArg(key='query_param_key', value='query_param_value', sep=SEPARATOR_QUERY_PARAM, orig='query_param_key==query_param_value'),
        KeyValueArg(key='file_upload_key', value='file_upload_value', sep=SEPARATOR_FILE_UPLOAD, orig='file_upload_key@file_upload_value'),
        KeyValueArg(key='data_item_key', value='data_item_value', sep=SEPARATOR_DATA_STRING, orig='data_item_key=data_item_value'),
        KeyValueArg(key='data_embed_file_contents_key', value='data_embed_file_contents_value', sep=SEPARATOR_DATA_EMBED_FILE_CONTENTS, orig='data_embed_file_contents_key=@data_embed_file_contents_value'),
        KeyValueArg(key='data_raw_json_embed_key', value='data_raw_json_embed_value', sep=SEPARATOR_DATA_RAW_JSON, orig='data_raw_json_embed_key:=data_raw_json_embed_value'),
        KeyValueArg(key='data_embed_raw_json_file_key', value='data_embed_raw_json_file_value', sep=SEPARATOR_DATA_EMBED_RAW_JSON_FILE, orig='data_embed_raw_json_file_key:=@data_embed_raw_json_file_value'),
    ]

    instance = RequestItems.from_args(request_item_args, as_form=True)

    assert instance.headers['header_key'] == 'header_value'
    assert instance.headers['empty_header_key'] == 'empty_header_value'
    assert instance.params['query_param_key'] == 'query_param_value'
    assert instance.files['file_upload_key'] == 'file_upload_value'
    assert instance.data['data_item_key'] == 'data_item_value'
    assert instance.data['data_embed_file_contents_key'] == 'data_embed_file_contents_value'
    assert instance.data['data_raw_json_embed_key'] == 'data_raw_json_embed_value'
    assert instance.data['data_embed_raw_json_file_key'] == 'data_embed_raw_json_file_value'
    assert instance.multipart_data['file_upload_key'] == 'file_upload_value'
    assert instance.multipart_data['data_embed_file_contents_key'] == 'data_embed_file_contents_value'
