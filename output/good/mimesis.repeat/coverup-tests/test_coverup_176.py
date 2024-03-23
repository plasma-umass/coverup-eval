# file mimesis/providers/person.py:243-275
# lines [256]
# branches ['255->256']

import pytest
from mimesis.providers import Person
from mimesis.exceptions import NonEnumerableError

def test_email_with_unique_and_seeded_provider(mocker):
    # Mock the Person class
    mocker.patch.object(Person, '__init__', lambda self: None)
    person = Person()
    person.seed = 123
    person.random = mocker.Mock()

    # Test that ValueError is raised when unique is True and provider is seeded
    with pytest.raises(ValueError):
        person.email(unique=True)

    # Clean up by unseeding the provider
    person.seed = None
