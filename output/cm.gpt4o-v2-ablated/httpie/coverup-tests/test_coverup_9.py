# file: httpie/uploads.py:101-118
# asked: {"lines": [101, 103, 104, 106, 107, 108, 110, 111, 112, 113, 115, 117, 118], "branches": [[110, 111], [110, 115], [112, 113], [112, 117]]}
# gained: {"lines": [101, 103, 104, 106, 107, 108, 110, 111, 112, 113, 115, 117, 118], "branches": [[110, 111], [110, 115], [112, 113], [112, 117]]}

import pytest
from httpie.uploads import get_multipart_data_and_content_type
from requests_toolbelt.multipart.encoder import MultipartEncoder

def test_get_multipart_data_and_content_type_no_boundary_no_content_type():
    data = {'field1': 'value1', 'field2': 'value2'}
    encoder, content_type = get_multipart_data_and_content_type(data)
    assert isinstance(encoder, MultipartEncoder)
    assert 'multipart/form-data' in content_type
    assert f'boundary={encoder.boundary_value}' in content_type

def test_get_multipart_data_and_content_type_with_boundary_no_content_type():
    data = {'field1': 'value1', 'field2': 'value2'}
    boundary = 'testboundary'
    encoder, content_type = get_multipart_data_and_content_type(data, boundary=boundary)
    assert isinstance(encoder, MultipartEncoder)
    assert encoder.boundary_value == boundary
    assert 'multipart/form-data' in content_type
    assert f'boundary={boundary}' in content_type

def test_get_multipart_data_and_content_type_no_boundary_with_content_type():
    data = {'field1': 'value1', 'field2': 'value2'}
    content_type = 'multipart/form-data'
    encoder, content_type = get_multipart_data_and_content_type(data, content_type=content_type)
    assert isinstance(encoder, MultipartEncoder)
    assert 'multipart/form-data' in content_type
    assert f'boundary={encoder.boundary_value}' in content_type

def test_get_multipart_data_and_content_type_with_boundary_with_content_type():
    data = {'field1': 'value1', 'field2': 'value2'}
    boundary = 'testboundary'
    content_type = 'multipart/form-data'
    encoder, content_type = get_multipart_data_and_content_type(data, boundary=boundary, content_type=content_type)
    assert isinstance(encoder, MultipartEncoder)
    assert encoder.boundary_value == boundary
    assert 'multipart/form-data' in content_type
    assert f'boundary={boundary}' in content_type

def test_get_multipart_data_and_content_type_with_content_type_with_existing_boundary():
    data = {'field1': 'value1', 'field2': 'value2'}
    content_type = 'multipart/form-data; boundary=existingboundary'
    encoder, content_type = get_multipart_data_and_content_type(data, content_type=content_type)
    assert isinstance(encoder, MultipartEncoder)
    assert 'multipart/form-data' in content_type
    assert 'boundary=existingboundary' in content_type
    assert 'boundary=' + encoder.boundary_value not in content_type
