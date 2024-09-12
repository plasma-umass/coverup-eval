# file: httpie/uploads.py:101-118
# asked: {"lines": [101, 103, 104, 106, 107, 108, 110, 111, 112, 113, 115, 117, 118], "branches": [[110, 111], [110, 115], [112, 113], [112, 117]]}
# gained: {"lines": [101, 103, 104, 106, 107, 108, 110, 111, 112, 113, 115, 117, 118], "branches": [[110, 111], [110, 115], [112, 113]]}

import pytest
from requests_toolbelt import MultipartEncoder
from httpie.cli.dicts import MultipartRequestDataDict
from httpie.uploads import get_multipart_data_and_content_type

def test_get_multipart_data_and_content_type_with_boundary():
    data = MultipartRequestDataDict()
    data['field'] = 'value'
    boundary = 'test_boundary'
    encoder, content_type = get_multipart_data_and_content_type(data, boundary=boundary)
    
    assert isinstance(encoder, MultipartEncoder)
    assert encoder.boundary_value == boundary
    assert content_type == f'multipart/form-data; boundary={boundary}'

def test_get_multipart_data_and_content_type_with_content_type():
    data = MultipartRequestDataDict()
    data['field'] = 'value'
    content_type = 'multipart/form-data'
    encoder, content_type = get_multipart_data_and_content_type(data, content_type=content_type)
    
    assert isinstance(encoder, MultipartEncoder)
    assert 'boundary=' in content_type

def test_get_multipart_data_and_content_type_with_content_type_and_boundary():
    data = MultipartRequestDataDict()
    data['field'] = 'value'
    boundary = 'test_boundary'
    content_type = 'multipart/form-data'
    encoder, content_type = get_multipart_data_and_content_type(data, boundary=boundary, content_type=content_type)
    
    assert isinstance(encoder, MultipartEncoder)
    assert encoder.boundary_value == boundary
    assert content_type == f'multipart/form-data; boundary={boundary}'

def test_get_multipart_data_and_content_type_default():
    data = MultipartRequestDataDict()
    data['field'] = 'value'
    encoder, content_type = get_multipart_data_and_content_type(data)
    
    assert isinstance(encoder, MultipartEncoder)
    assert content_type == encoder.content_type
