# file httpie/cli/requestitems.py:31-81
# lines [37, 38, 39, 40, 41, 43, 44, 45, 47, 48, 49, 51, 52, 53, 55, 56, 57, 59, 60, 61, 63, 64, 65, 67, 68, 69, 73, 74, 75, 76, 78, 79, 81]
# branches ['73->74', '73->81', '78->73', '78->79']

import pytest
from httpie.cli.requestitems import RequestItems, KeyValueArg
from httpie.cli.constants import (
    SEPARATOR_HEADER,
    SEPARATOR_HEADER_EMPTY,
    SEPARATOR_QUERY_PARAM,
    SEPARATOR_FILE_UPLOAD,
    SEPARATOR_DATA_STRING,
    SEPARATOR_DATA_EMBED_FILE_CONTENTS,
    SEPARATOR_DATA_RAW_JSON,
    SEPARATOR_DATA_EMBED_RAW_JSON_FILE,
)

@pytest.fixture
def mock_process_functions(mocker):
    mocker.patch('httpie.cli.requestitems.process_header_arg', return_value='processed_header')
    mocker.patch('httpie.cli.requestitems.process_empty_header_arg', return_value='processed_empty_header')
    mocker.patch('httpie.cli.requestitems.process_query_param_arg', return_value='processed_query_param')
    mocker.patch('httpie.cli.requestitems.process_file_upload_arg', return_value='processed_file_upload')
    mocker.patch('httpie.cli.requestitems.process_data_item_arg', return_value='processed_data_item')
    mocker.patch('httpie.cli.requestitems.process_data_embed_file_contents_arg', return_value='processed_data_embed')
    mocker.patch('httpie.cli.requestitems.process_data_raw_json_embed_arg', return_value='processed_data_raw_json')
    mocker.patch('httpie.cli.requestitems.process_data_embed_raw_json_file_arg', return_value='processed_data_embed_raw_json')

def test_request_items_from_args(mock_process_functions):
    request_item_args = [
        KeyValueArg(key='header', sep=SEPARATOR_HEADER, value='value', orig='header:value'),
        KeyValueArg(key='empty_header', sep=SEPARATOR_HEADER_EMPTY, value='value', orig='empty_header;'),
        KeyValueArg(key='query', sep=SEPARATOR_QUERY_PARAM, value='value', orig='query==value'),
        KeyValueArg(key='file', sep=SEPARATOR_FILE_UPLOAD, value='value', orig='file@value'),
        KeyValueArg(key='data_string', sep=SEPARATOR_DATA_STRING, value='value', orig='data_string=value'),
        KeyValueArg(key='data_embed', sep=SEPARATOR_DATA_EMBED_FILE_CONTENTS, value='value', orig='data_embed:=value'),
        KeyValueArg(key='data_raw_json', sep=SEPARATOR_DATA_RAW_JSON, value='value', orig='data_raw_json:=value'),
        KeyValueArg(key='data_embed_raw_json', sep=SEPARATOR_DATA_EMBED_RAW_JSON_FILE, value='value', orig='data_embed_raw_json:=@value'),
    ]
    request_items = RequestItems.from_args(request_item_args)

    assert request_items.headers['header'] == 'processed_header'
    assert request_items.headers['empty_header'] == 'processed_empty_header'
    assert request_items.params['query'] == 'processed_query_param'
    assert request_items.files['file'] == 'processed_file_upload'
    assert request_items.data['data_string'] == 'processed_data_item'
    assert request_items.data['data_embed'] == 'processed_data_embed'
    assert request_items.data['data_raw_json'] == 'processed_data_raw_json'
    assert request_items.data['data_embed_raw_json'] == 'processed_data_embed_raw_json'
