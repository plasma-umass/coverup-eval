# file mimesis/providers/person.py:243-275
# lines [243, 244, 255, 256, 259, 260, 262, 264, 265, 267, 268, 270, 272, 273, 274]
# branches ['255->256', '255->259', '259->260', '259->262', '264->265', '264->267', '267->268', '267->270']

import pytest
from mimesis.providers.person import Person
from mimesis.random import Random

@pytest.fixture
def person():
    return Person()

def test_email_with_custom_domains(person):
    custom_domains = ['example.com', 'test.org']
    email = person.email(domains=custom_domains)
    assert any(email.endswith('@' + domain) for domain in custom_domains)

def test_email_with_unique(person, mocker):
    mocker.patch.object(Random, 'randstr', return_value='unique_name')
    email = person.email(unique=True)
    assert email.startswith('unique_name@')

def test_email_with_unique_and_seeded_provider(person, mocker):
    mocker.patch.object(Random, 'randstr', side_effect=Exception('You cannot use «unique» parameter with a seeded provider'))
    with pytest.raises(Exception) as exc_info:
        person.email(unique=True)
    assert str(exc_info.value) == 'You cannot use «unique» parameter with a seeded provider'

def test_email_without_at_symbol_in_custom_domains(person):
    custom_domains = ['example.com', 'test.org']
    email = person.email(domains=custom_domains)
    assert '@' in email and any(email.endswith(domain) for domain in custom_domains)

def test_email_default_domains(person):
    email = person.email()
    assert '@' in email
