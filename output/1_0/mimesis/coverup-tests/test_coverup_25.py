# file mimesis/exceptions.py:77-81
# lines [77, 78, 80, 81]
# branches []

import pytest
from mimesis.exceptions import UnacceptableField

def test_unacceptable_field_exception():
    with pytest.raises(UnacceptableField) as exc_info:
        raise UnacceptableField()
    assert str(exc_info.value) == 'Unacceptable field format, use **provider.method**.'
