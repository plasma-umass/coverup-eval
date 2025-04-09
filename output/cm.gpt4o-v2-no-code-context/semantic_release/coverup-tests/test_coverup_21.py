# file: semantic_release/hvcs.py:52-64
# asked: {"lines": [52, 64], "branches": []}
# gained: {"lines": [52, 64], "branches": []}

import pytest
import mimetypes

def test_fix_mime_types(monkeypatch):
    from semantic_release.hvcs import _fix_mime_types

    # Backup the original MIME type for .md if it exists
    original_md_type = mimetypes.guess_type("file.md")[0]

    # Ensure the .md type is not set to "text/markdown" before running the function
    mimetypes.add_type("application/octet-stream", ".md")
    assert mimetypes.guess_type("file.md")[0] == "application/octet-stream"

    # Run the function to fix MIME types
    _fix_mime_types()

    # Verify that the MIME type for .md is now set to "text/markdown"
    assert mimetypes.guess_type("file.md")[0] == "text/markdown"

    # Restore the original MIME type for .md if it was set
    if original_md_type:
        mimetypes.add_type(original_md_type, ".md")
    else:
        mimetypes.types_map.pop(".md", None)
