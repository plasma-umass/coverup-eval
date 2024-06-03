# file httpie/uploads.py:23-34
# lines [23, 24, 26, 27, 29, 30, 31, 32, 33, 34]
# branches ['30->31', '32->33', '32->34']

import pytest
from httpie.uploads import ChunkedMultipartUploadStream
from requests_toolbelt.multipart.encoder import MultipartEncoder
import io

@pytest.fixture
def mock_encoder(mocker):
    encoder = mocker.Mock(spec=MultipartEncoder)
    encoder.read.side_effect = [
        b'chunk1', b'chunk2', b'chunk3', b''
    ]
    return encoder

def test_chunked_multipart_upload_stream(mock_encoder):
    stream = ChunkedMultipartUploadStream(mock_encoder)
    chunks = list(stream)
    
    assert chunks == [b'chunk1', b'chunk2', b'chunk3']
    assert mock_encoder.read.call_count == 4
    mock_encoder.read.assert_called_with(ChunkedMultipartUploadStream.chunk_size)
