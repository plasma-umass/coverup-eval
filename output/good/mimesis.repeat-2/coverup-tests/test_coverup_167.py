# file mimesis/providers/person.py:466-475
# lines [474, 475]
# branches []

import pytest
from mimesis.providers import Person
from mimesis.enums import Gender
from unittest.mock import patch

def test_person_language():
    # Setup a Person instance
    person = Person()

    # Patch the internal data to contain a predictable language list
    with patch.object(person, '_data', {'language': ['English', 'Spanish']}):
        # Call the method under test
        language = person.language()

        # Assert that the returned language is one of the ones we patched in
        assert language in ['English', 'Spanish']

# The cleanup is handled by the context manager, so no further action is required.
