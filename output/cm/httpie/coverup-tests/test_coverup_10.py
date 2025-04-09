# file httpie/uploads.py:101-118
# lines [101, 103, 104, 106, 107, 108, 110, 111, 112, 113, 115, 117, 118]
# branches ['110->111', '110->115', '112->113', '112->117']

import pytest
from httpie.uploads import get_multipart_data_and_content_type
from requests_toolbelt.multipart.encoder import MultipartEncoder

@pytest.fixture
def mock_encoder(mocker):
    mock = mocker.MagicMock(spec=MultipartEncoder)
    mock.content_type = 'multipart/form-data; boundary=test_boundary'
    type(mock).boundary_value = mocker.PropertyMock(return_value='test_boundary')
    mocker.patch('httpie.uploads.MultipartEncoder', return_value=mock)
    return mock

def test_get_multipart_data_and_content_type_with_content_type_no_boundary(mock_encoder):
    data = {'field': 'value'}
    content_type = 'multipart/form-data'
    encoder, content_type = get_multipart_data_and_content_type(data, content_type=content_type)
    assert isinstance(encoder, MultipartEncoder)
    assert 'boundary=test_boundary' in content_type
    assert 'multipart/form-data; boundary=test_boundary' == content_type

def test_get_multipart_data_and_content_type_without_content_type(mock_encoder):
    data = {'field': 'value'}
    encoder, content_type = get_multipart_data_and_content_type(data)
    assert isinstance(encoder, MultipartEncoder)
    assert 'multipart/form-data; boundary=test_boundary' == content_type
