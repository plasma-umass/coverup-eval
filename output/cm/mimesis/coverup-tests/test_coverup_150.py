# file mimesis/providers/person.py:223-241
# lines [233, 234, 236, 237, 238, 239, 241]
# branches ['236->237', '236->241']

import pytest
from mimesis.providers.person import Person
from unittest.mock import patch
import hashlib

def test_password_hashed():
    person = Person()
    length = 10
    with patch('mimesis.providers.person.hashlib.md5') as mock_md5:
        mock_md5.return_value.hexdigest.return_value = 'hashed_password'
        result = person.password(length=length, hashed=True)
        mock_md5.assert_called_once()
        mock_md5.return_value.update.assert_called_once()
        assert result == 'hashed_password'
