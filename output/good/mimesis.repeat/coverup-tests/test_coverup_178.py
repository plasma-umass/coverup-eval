# file mimesis/providers/person.py:444-453
# lines [452, 453]
# branches []

import pytest
from mimesis.providers import Person
from mimesis import Generic
from unittest.mock import patch

def test_university_full_coverage():
    generic = Generic('en')
    person = Person()

    # Patch the generic data to control the output and ensure the test is repeatable
    with patch.object(generic, '_data', return_value={'university': ['MIT', 'Stanford']}):
        person._data = generic._data()
        university = person.university()
        assert university in ['MIT', 'Stanford']
