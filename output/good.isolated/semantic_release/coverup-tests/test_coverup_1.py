# file semantic_release/hvcs.py:52-64
# lines [52, 64]
# branches []

import mimetypes
import pytest
from semantic_release.hvcs import _fix_mime_types

def test_fix_mime_types(mocker):
    # Mock the add_type method to ensure it is called with the correct parameters
    mock_add_type = mocker.patch('mimetypes.add_type')

    # Call the function that should fix the mime types
    _fix_mime_types()

    # Assert that the correct MIME type was added for the .md extension
    mock_add_type.assert_called_once_with("text/markdown", ".md")

    # Clean up by removing the mocked MIME type
    mimetypes.init()
