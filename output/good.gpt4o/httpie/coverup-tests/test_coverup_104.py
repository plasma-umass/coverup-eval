# file httpie/uploads.py:101-118
# lines []
# branches ['112->117']

import pytest
from httpie.uploads import get_multipart_data_and_content_type
from requests_toolbelt.multipart.encoder import MultipartEncoder

def test_get_multipart_data_and_content_type_with_boundary_in_content_type():
    data = {'field1': 'value1', 'field2': 'value2'}
    boundary = 'testboundary'
    content_type = 'multipart/form-data; boundary=testboundary'

    encoder = MultipartEncoder(fields=data.items(), boundary=boundary)
    result_data, result_content_type = get_multipart_data_and_content_type(data, boundary, content_type)

    assert isinstance(result_data, MultipartEncoder)
    assert result_data.fields == encoder.fields
    assert result_data.boundary == encoder.boundary
    assert result_content_type == content_type

def test_get_multipart_data_and_content_type_without_boundary_in_content_type():
    data = {'field1': 'value1', 'field2': 'value2'}
    boundary = 'testboundary'
    content_type = 'multipart/form-data'

    encoder = MultipartEncoder(fields=data.items(), boundary=boundary)
    result_data, result_content_type = get_multipart_data_and_content_type(data, boundary, content_type)

    assert isinstance(result_data, MultipartEncoder)
    assert result_data.fields == encoder.fields
    assert result_data.boundary == encoder.boundary
    assert result_content_type == f'{content_type}; boundary={encoder.boundary_value}'

def test_get_multipart_data_and_content_type_without_content_type():
    data = {'field1': 'value1', 'field2': 'value2'}
    boundary = 'testboundary'

    encoder = MultipartEncoder(fields=data.items(), boundary=boundary)
    result_data, result_content_type = get_multipart_data_and_content_type(data, boundary)

    assert isinstance(result_data, MultipartEncoder)
    assert result_data.fields == encoder.fields
    assert result_data.boundary == encoder.boundary
    assert result_content_type == encoder.content_type
