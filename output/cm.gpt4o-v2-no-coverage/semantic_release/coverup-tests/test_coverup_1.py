# file: semantic_release/hvcs.py:52-64
# asked: {"lines": [52, 64], "branches": []}
# gained: {"lines": [52, 64], "branches": []}

import pytest
import mimetypes
from semantic_release.hvcs import _fix_mime_types

def test_fix_mime_types(monkeypatch):
    # Backup the original types map
    original_types_map = mimetypes.types_map.copy()

    try:
        # Ensure the type is not already in the map
        if '.md' in mimetypes.types_map:
            del mimetypes.types_map['.md']

        # Run the function to fix mime types
        _fix_mime_types()

        # Assert that the mime type for .md is correctly set
        assert mimetypes.types_map['.md'] == 'text/markdown'
    finally:
        # Restore the original types map to avoid state pollution
        mimetypes.types_map.clear()
        mimetypes.types_map.update(original_types_map)
