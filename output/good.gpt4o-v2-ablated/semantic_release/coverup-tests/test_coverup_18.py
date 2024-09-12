# file: semantic_release/hvcs.py:52-64
# asked: {"lines": [52, 64], "branches": []}
# gained: {"lines": [52, 64], "branches": []}

import mimetypes
import pytest

def test_fix_mime_types(monkeypatch):
    from semantic_release.hvcs import _fix_mime_types

    # Backup the original MIME type for .md if it exists
    original_md_type = mimetypes.guess_type("file.md")[0]

    # Apply the fix
    _fix_mime_types()

    # Assert that the MIME type for .md is now "text/markdown"
    assert mimetypes.guess_type("file.md")[0] == "text/markdown"

    # Clean up by restoring the original MIME type for .md
    if original_md_type:
        mimetypes.add_type(original_md_type, ".md")
    else:
        mimetypes.types_map.pop(".md", None)
