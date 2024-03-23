# file mimesis/providers/person.py:243-275
# lines [243, 244, 255, 256, 259, 260, 262, 264, 265, 267, 268, 270, 272, 273, 274]
# branches ['255->256', '255->259', '259->260', '259->262', '264->265', '264->267', '267->268', '267->270']

import pytest
from mimesis.providers import Person

def test_person_email_unique_with_seed():
    # Create a Person instance with a seed
    person = Person(seed=42)

    # Test that ValueError is raised when unique is True and the provider was seeded
    with pytest.raises(ValueError):
        person.email(unique=True)

def test_person_email_custom_domains():
    # Create a Person instance without a seed
    person = Person()

    # Test that custom domain is used
    custom_domains = ['custom.com']
    email = person.email(domains=custom_domains)
    domain = email.split('@')[-1]
    assert domain in custom_domains

def test_person_email_default_domains():
    # Create a Person instance without a seed
    person = Person()

    # Test that default domain is used when no custom domains are provided
    email = person.email()
    domain = email.split('@')[-1]
    assert domain.endswith('.com')

def test_person_email_unique_without_seed():
    # Create a Person instance without a seed
    person = Person()

    # Test that unique email is generated
    email1 = person.email(unique=True)
    email2 = person.email(unique=True)
    assert email1 != email2
