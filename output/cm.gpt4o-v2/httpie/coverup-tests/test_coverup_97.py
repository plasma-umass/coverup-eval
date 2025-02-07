# file: httpie/uploads.py:101-118
# asked: {"lines": [], "branches": [[112, 117]]}
# gained: {"lines": [], "branches": [[112, 117]]}

import pytest
from requests_toolbelt import MultipartEncoder
from httpie.cli.dicts import MultipartRequestDataDict
from httpie.uploads import get_multipart_data_and_content_type

def test_get_multipart_data_and_content_type_with_boundary_in_content_type():
    data = MultipartRequestDataDict()
    data['field'] = 'value'
    boundary = 'test_boundary'
    content_type = 'multipart/form-data; boundary=test_boundary'
    
    encoder, returned_content_type = get_multipart_data_and_content_type(data, boundary, content_type)
    
    assert isinstance(encoder, MultipartEncoder)
    assert returned_content_type == content_type

def test_get_multipart_data_and_content_type_without_boundary_in_content_type():
    data = MultipartRequestDataDict()
    data['field'] = 'value'
    boundary = 'test_boundary'
    content_type = 'multipart/form-data'
    
    encoder, returned_content_type = get_multipart_data_and_content_type(data, boundary, content_type)
    
    assert isinstance(encoder, MultipartEncoder)
    assert 'boundary=' in returned_content_type
    assert returned_content_type.startswith(content_type)

def test_get_multipart_data_and_content_type_without_content_type():
    data = MultipartRequestDataDict()
    data['field'] = 'value'
    boundary = 'test_boundary'
    
    encoder, returned_content_type = get_multipart_data_and_content_type(data, boundary)
    
    assert isinstance(encoder, MultipartEncoder)
    assert returned_content_type == encoder.content_type
