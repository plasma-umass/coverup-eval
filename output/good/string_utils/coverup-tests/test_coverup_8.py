# file string_utils/manipulation.py:246-248
# lines [246, 247, 248]
# branches []

import pytest
from string_utils.manipulation import __StringFormatter
from unittest.mock import patch
from uuid import uuid4

def test_placeholder_key():
    with patch('string_utils.manipulation.uuid4') as mock_uuid4:
        mock_uuid4.return_value = uuid4()
        expected_uuid = mock_uuid4.return_value.hex
        placeholder_key = __StringFormatter._StringFormatter__placeholder_key()
        assert placeholder_key == f'${expected_uuid}$'
