# file: httpie/uploads.py:101-118
# asked: {"lines": [], "branches": [[112, 117]]}
# gained: {"lines": [], "branches": [[112, 117]]}

import pytest
from httpie.uploads import get_multipart_data_and_content_type
from requests_toolbelt.multipart.encoder import MultipartEncoder

def test_get_multipart_data_and_content_type_with_boundary_in_content_type():
    data = {'field1': 'value1', 'field2': 'value2'}
    boundary = 'testboundary'
    content_type = 'multipart/form-data; boundary=testboundary'
    
    encoder, returned_content_type = get_multipart_data_and_content_type(data, boundary, content_type)
    
    assert isinstance(encoder, MultipartEncoder)
    assert returned_content_type == content_type
    assert encoder.boundary_value == boundary

def test_get_multipart_data_and_content_type_without_boundary_in_content_type():
    data = {'field1': 'value1', 'field2': 'value2'}
    boundary = 'testboundary'
    content_type = 'multipart/form-data'
    
    encoder, returned_content_type = get_multipart_data_and_content_type(data, boundary, content_type)
    
    assert isinstance(encoder, MultipartEncoder)
    assert 'boundary=' in returned_content_type
    assert encoder.boundary_value in returned_content_type

def test_get_multipart_data_and_content_type_without_content_type():
    data = {'field1': 'value1', 'field2': 'value2'}
    boundary = 'testboundary'
    
    encoder, returned_content_type = get_multipart_data_and_content_type(data, boundary)
    
    assert isinstance(encoder, MultipartEncoder)
    assert returned_content_type == encoder.content_type
    assert encoder.boundary_value == boundary
