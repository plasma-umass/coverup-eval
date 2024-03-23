# file mimesis/enums.py:122-133
# lines [122, 123, 128, 129, 130, 131, 132, 133]
# branches []

import pytest
from mimesis.enums import MimeType

def test_mime_type_enum():
    # Test all enum values to ensure full coverage
    assert MimeType.APPLICATION.value == 'application'
    assert MimeType.AUDIO.value == 'audio'
    assert MimeType.IMAGE.value == 'image'
    assert MimeType.MESSAGE.value == 'message'
    assert MimeType.TEXT.value == 'text'
    assert MimeType.VIDEO.value == 'video'

    # Test that all enum keys are unique
    assert len(set(item.name for item in MimeType)) == len(MimeType)
    # Test that all enum values are unique
    assert len(set(item.value for item in MimeType)) == len(MimeType)
