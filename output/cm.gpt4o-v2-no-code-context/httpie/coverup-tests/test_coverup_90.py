# file: httpie/output/streams.py:173-199
# asked: {"lines": [186, 187, 189, 190, 191, 192, 193, 194, 196, 197, 199], "branches": [[189, 190], [189, 196], [190, 191], [190, 194], [192, 193], [192, 194], [196, 197], [196, 199]]}
# gained: {"lines": [186, 187, 189, 190, 191, 192, 193, 194, 196, 197, 199], "branches": [[189, 190], [189, 196], [190, 191], [190, 194], [192, 193], [192, 194], [196, 197], [196, 199]]}

import pytest
from httpie.output.streams import BufferedPrettyStream, BinarySuppressedError
from unittest.mock import Mock, patch

@pytest.fixture
def mock_msg():
    msg = Mock()
    msg.iter_body = Mock(return_value=[b'chunk1', b'chunk2\0chunk3'])
    msg.content_type = 'application/octet-stream'
    return msg

@pytest.fixture
def mock_converter():
    converter = Mock()
    converter.convert = Mock(return_value=('new_mime', b'converted_body'))
    return converter

@pytest.fixture
def mock_conversion(mock_converter):
    conversion = Mock()
    conversion.get_converter = Mock(return_value=mock_converter)
    return conversion

@pytest.fixture
def mock_formatting():
    return Mock()

def test_iter_body_binary_suppressed_error(mock_msg, mock_formatting):
    stream = BufferedPrettyStream(msg=mock_msg, conversion=Mock(get_converter=Mock(return_value=None)), formatting=mock_formatting)
    stream.mime = 'application/octet-stream'
    
    with pytest.raises(BinarySuppressedError):
        list(stream.iter_body())

def test_iter_body_with_conversion(mock_msg, mock_conversion, mock_formatting):
    stream = BufferedPrettyStream(msg=mock_msg, conversion=mock_conversion, formatting=mock_formatting)
    stream.mime = 'application/json'
    
    with patch.object(stream, 'process_body', return_value=b'processed_body') as mock_process_body:
        result = list(stream.iter_body())
    
    mock_conversion.get_converter.assert_called_once_with('application/json')
    mock_conversion.get_converter().convert.assert_called_once_with(b'chunk1chunk2\0chunk3')
    mock_process_body.assert_called_once_with(b'converted_body')
    assert result == [b'processed_body']

def test_iter_body_without_conversion(mock_msg, mock_formatting):
    mock_msg.iter_body = Mock(return_value=[b'chunk1', b'chunk2'])
    stream = BufferedPrettyStream(msg=mock_msg, conversion=Mock(get_converter=Mock(return_value=None)), formatting=mock_formatting)
    stream.mime = 'text/plain'
    
    with patch.object(stream, 'process_body', return_value=b'processed_body') as mock_process_body:
        result = list(stream.iter_body())
    
    mock_process_body.assert_called_once_with(b'chunk1chunk2')
    assert result == [b'processed_body']
