# file httpie/uploads.py:101-118
# lines []
# branches ['112->117']

import pytest
from httpie.uploads import get_multipart_data_and_content_type
from requests_toolbelt.multipart.encoder import MultipartEncoder

@pytest.fixture
def cleanup():
    # Fixture to clean up any side effects after the test
    yield
    # Here you can add any cleanup code if needed

def test_get_multipart_data_and_content_type_with_boundary_in_content_type(cleanup):
    # Given
    data = {'key': 'value'}
    boundary = 'testboundary'
    content_type = 'multipart/form-data; boundary=existingboundary'

    # When
    encoder, actual_content_type = get_multipart_data_and_content_type(data, boundary, content_type)

    # Then
    assert isinstance(encoder, MultipartEncoder)
    assert actual_content_type == content_type
    assert 'boundary=' in actual_content_type
    assert actual_content_type.endswith('existingboundary')
