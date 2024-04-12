# file httpie/uploads.py:37-98
# lines [81, 82, 83]
# branches []

import io
import pytest
from httpie.uploads import prepare_request_body

class FakeSuperLen:
    def __len__(self):
        return 1

@pytest.fixture
def file_like_object_with_super_len(mocker):
    file_like = io.BytesIO(b"test data")
    mocker.patch('httpie.uploads.super_len', return_value=FakeSuperLen())
    return file_like

def test_prepare_request_body_with_file_like_object_and_callback(file_like_object_with_super_len, mocker):
    callback = mocker.Mock()
    body = prepare_request_body(
        body=file_like_object_with_super_len,
        body_read_callback=callback,
        chunked=False,
        offline=False
    )
    assert body.read() == b"test data"
    callback.assert_called_once_with(b"test data")
