# file httpie/utils.py:77-89
# lines [77, 84, 85, 86, 87, 88, 89]
# branches ['85->exit', '85->86', '87->88', '87->89']

import pytest
import mimetypes
from httpie.utils import get_content_type

def test_get_content_type(mocker):
    # Mocking mimetypes.guess_type to control its output
    mocker.patch('mimetypes.guess_type', return_value=('text/plain', 'utf-8'))
    
    # Test case where both mime and encoding are returned
    filename = 'example.txt'
    expected_content_type = 'text/plain; charset=utf-8'
    assert get_content_type(filename) == expected_content_type
    
    # Test case where only mime is returned
    mocker.patch('mimetypes.guess_type', return_value=('text/plain', None))
    expected_content_type = 'text/plain'
    assert get_content_type(filename) == expected_content_type
    
    # Test case where neither mime nor encoding is returned
    mocker.patch('mimetypes.guess_type', return_value=(None, None))
    assert get_content_type(filename) is None
