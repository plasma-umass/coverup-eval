# file httpie/sessions.py:100-102
# lines [102]
# branches []

import pytest
from httpie.sessions import Session, BaseConfigDict, RequestHeadersDict

def test_session_headers_property(mocker):
    # Mock the BaseConfigDict to return a specific headers dictionary
    mock_headers = {'User-Agent': 'test-agent'}
    mocker.patch.object(BaseConfigDict, '__getitem__', return_value=mock_headers)
    
    # Create a Session instance with a dummy path
    session = Session(path='dummy_path')
    
    # Access the headers property to trigger the code on line 102
    headers = session.headers
    
    # Verify that the headers property returns a RequestHeadersDict with the correct headers
    assert isinstance(headers, RequestHeadersDict)
    assert headers == mock_headers
