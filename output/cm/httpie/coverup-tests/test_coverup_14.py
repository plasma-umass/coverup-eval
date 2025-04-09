# file httpie/utils.py:77-89
# lines [77, 84, 85, 86, 87, 88, 89]
# branches ['85->exit', '85->86', '87->88', '87->89']

import mimetypes
import pytest
from httpie.utils import get_content_type
from unittest.mock import patch

# Test function to cover the branch where encoding is not None
def test_get_content_type_with_encoding(tmp_path):
    # Create a temporary file with a known mimetype and encoding
    file = tmp_path / "test.gz"
    file.write_text("test content", encoding="utf-8")

    # Patch mimetypes.guess_type to return a known encoding
    with patch("mimetypes.guess_type", return_value=("application/gzip", "gzip")) as mock_guess_type:
        content_type = get_content_type(str(file))
        mock_guess_type.assert_called_once_with(str(file), strict=False)
        assert content_type == "application/gzip; charset=gzip"

# Test function to cover the branch where encoding is None
def test_get_content_type_without_encoding(tmp_path):
    # Create a temporary file with a known mimetype
    file = tmp_path / "test.txt"
    file.write_text("test content", encoding="utf-8")

    # Patch mimetypes.guess_type to return no encoding
    with patch("mimetypes.guess_type", return_value=("text/plain", None)) as mock_guess_type:
        content_type = get_content_type(str(file))
        mock_guess_type.assert_called_once_with(str(file), strict=False)
        assert content_type == "text/plain"
