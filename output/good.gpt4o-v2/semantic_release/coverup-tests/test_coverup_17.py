# file: semantic_release/hvcs.py:52-64
# asked: {"lines": [52, 64], "branches": []}
# gained: {"lines": [52, 64], "branches": []}

import pytest
import mimetypes
from semantic_release.hvcs import _fix_mime_types

def test_fix_mime_types(monkeypatch):
    # Backup the original types
    original_types = mimetypes.types_map.copy()

    # Apply the fix
    _fix_mime_types()

    # Assert the MIME type for .md is correctly set
    assert mimetypes.guess_type('file.md')[0] == 'text/markdown'

    # Restore the original types to avoid state pollution
    monkeypatch.setattr(mimetypes, 'types_map', original_types)
