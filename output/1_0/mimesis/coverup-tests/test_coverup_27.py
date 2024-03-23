# file mimesis/enums.py:109-119
# lines [109, 110, 112, 113, 114, 115, 116, 117, 118, 119]
# branches []

import pytest
from mimesis.enums import FileType

def test_file_type_enum():
    assert FileType.SOURCE == FileType('source')
    assert FileType.TEXT == FileType('text')
    assert FileType.DATA == FileType('data')
    assert FileType.AUDIO == FileType('audio')
    assert FileType.VIDEO == FileType('video')
    assert FileType.IMAGE == FileType('image')
    assert FileType.EXECUTABLE == FileType('executable')
    assert FileType.COMPRESSED == FileType('compressed')

    # Test that all enum values are covered
    for file_type in FileType:
        assert file_type in [
            FileType.SOURCE,
            FileType.TEXT,
            FileType.DATA,
            FileType.AUDIO,
            FileType.VIDEO,
            FileType.IMAGE,
            FileType.EXECUTABLE,
            FileType.COMPRESSED,
        ]
