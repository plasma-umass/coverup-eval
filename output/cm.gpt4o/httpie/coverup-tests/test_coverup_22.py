# file httpie/uploads.py:101-118
# lines [101, 103, 104, 106, 107, 108, 110, 111, 112, 113, 115, 117, 118]
# branches ['110->111', '110->115', '112->113', '112->117']

import pytest
from httpie.uploads import get_multipart_data_and_content_type
from requests_toolbelt.multipart.encoder import MultipartEncoder

def test_get_multipart_data_and_content_type_with_boundary_and_content_type():
    data = {'field1': 'value1', 'field2': 'value2'}
    boundary = 'testboundary'
    content_type = 'multipart/form-data'

    encoder, returned_content_type = get_multipart_data_and_content_type(data, boundary, content_type)

    assert isinstance(encoder, MultipartEncoder)
    assert encoder.boundary_value == boundary
    assert returned_content_type == f'{content_type}; boundary={boundary}'

def test_get_multipart_data_and_content_type_without_boundary_with_content_type():
    data = {'field1': 'value1', 'field2': 'value2'}
    content_type = 'multipart/form-data'

    encoder, returned_content_type = get_multipart_data_and_content_type(data, content_type=content_type)

    assert isinstance(encoder, MultipartEncoder)
    assert 'boundary=' in returned_content_type
    assert returned_content_type.startswith(content_type)

def test_get_multipart_data_and_content_type_without_content_type():
    data = {'field1': 'value1', 'field2': 'value2'}

    encoder, returned_content_type = get_multipart_data_and_content_type(data)

    assert isinstance(encoder, MultipartEncoder)
    assert returned_content_type == encoder.content_type

def test_get_multipart_data_and_content_type_with_empty_content_type():
    data = {'field1': 'value1', 'field2': 'value2'}
    content_type = ''

    encoder, returned_content_type = get_multipart_data_and_content_type(data, content_type=content_type)

    assert isinstance(encoder, MultipartEncoder)
    assert 'boundary=' in returned_content_type
    assert returned_content_type.startswith('multipart/form-data')

@pytest.fixture(autouse=True)
def cleanup(mocker):
    yield
    mocker.stopall()
